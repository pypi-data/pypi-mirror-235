import traceback

from abc import ABCMeta
from typing import Optional, Dict, Any, Union, Tuple, List

from django.db.models.query import QuerySet, Q
from django.utils.decorators import method_decorator

from rest_framework.serializers import ReturnDict, ReturnList

from drf_yasg.openapi import Schema, Parameter
from drf_yasg.utils import swagger_auto_schema

from utils.exception import ViewException, DjangoWebException, ModelException
from utils.web.django.utils import DjangoUtils
from utils.web.django.conf import DjangoConfig
from utils.web.django.model import BaseModel
from utils.web.django.serializer import BaseSerializer
from utils.web.django.pagination import BasePagination
from utils.web.django.request import WebRequest
from utils.web.django.response import WebResponse

from .. import async_rest_api
from ._async_view import AsyncAPIView
from .._types import PARAMS_TYPE

from ._swagger_base import SwaggerTypeBase


class AsyncBaseAPIView(AsyncAPIView, metaclass=ABCMeta):
    config: DjangoConfig
    model: BaseModel
    serializer: BaseSerializer
    page_class: BasePagination

    # 删除标记，False表示逻辑删除，True表示物理删除
    is_delete: bool = False
    # 过滤连接条件
    filter_condition: str = "OR"
    # 过滤符号
    filter_symbol: str = "contains"

    page_instance: BasePagination
    is_page: bool

    request_get: Optional[List[Parameter]] = None
    request_post: Optional[Schema] = None
    request_put: Optional[Schema] = None
    request_delete: Optional[Dict[str, Union[List[Parameter], Schema, None]]] = None
    swagger_type: SwaggerTypeBase = SwaggerTypeBase(request_get=request_get, request_post=request_post,
                                                    request_put=request_put, request_delete=request_delete)

    response_get: Dict[Union[str, int], Schema] = swagger_type.response()
    response_post: Dict[Union[str, int], Schema] = swagger_type.response()
    response_put: Dict[Union[str, int], Schema] = swagger_type.response()
    response_delete: Dict[Union[str, int], Schema] = swagger_type.response()

    async def __get_filter_field(self, params: PARAMS_TYPE) -> Dict[str, Any]:
        field: List[str] = await self.model.async_get_field()
        params_keys: List[str] = list(params.keys())
        filter_field: List[str] = list(set(field) & set(params_keys))
        filter_mapper: Dict[str, Any] = {key: params.get(key)[0] for key in filter_field}
        return filter_mapper

    async def create_exception(self, e: Exception) -> ViewException:
        return ViewException(str(e), traceback.format_exc())

    async def show_exception(self, e: DjangoWebException):
        self.config.printf.error(e.error_detail)
        self.config.printf.warning(e.error_summary)

    async def __filter(self, params: PARAMS_TYPE) -> QuerySet[BaseModel]:
        filter_field: Dict[str, Any] = await self.__get_filter_field(params)
        instance: QuerySet[BaseModel] = await self.model.async_filter(is_delete=0)
        q: Q = Q()
        q.connector = self.filter_symbol
        for key, val in filter_field.items():
            if key == "is_delete":
                q.children.append((key, val))
            else:
                q.children.append((f"{key}__{self.filter_symbol}", val))
        return await DjangoUtils.to_async_fun(instance.filter, q)

    async def before_select(self, request: WebRequest, instance: Union[QuerySet[BaseModel], BaseModel], many: bool) -> \
            Union[QuerySet[BaseModel], BaseModel]:
        return instance

    async def __before_select(self, request: WebRequest, params: PARAMS_TYPE, many: bool, select_id: Optional[str]) -> \
            Union[QuerySet[BaseModel], BaseModel]:
        if many:
            instance: QuerySet[BaseModel] = await self.__filter(params)
            self.is_page = True
        else:
            instance: BaseModel = await self.model.async_get_one(id=select_id)
            if instance.is_delete:
                raise Exception("not find!")
        try:
            instance: Union[QuerySet[BaseModel], BaseModel] = await self.before_select(request, instance, many)
        except Exception as e:
            raise await self.create_exception(e)
        if many and self.is_page:
            self.page_instance = self.page_class()
            instance = await self.page_instance.async_paginate_queryset(instance, request.request, self)
        return instance

    @swagger_auto_schema(
        manual_parameters=swagger_type.request_get,
        responses=response_get)
    @method_decorator(async_rest_api())
    async def get(self, request: WebRequest, id: Optional[str] = None) -> WebResponse:
        self.config.printf.info(f"request success!\npath is {request.path}\nmethod is get\nselect id is {id}")
        params: PARAMS_TYPE = request.params
        many: bool = id is None
        try:
            instance: Union[QuerySet[BaseModel], BaseModel] = await self.__before_select(request, params, many, id)
        except ViewException as e:
            await self.show_exception(e)
            return WebResponse(status=400, error=e)
        serializer: BaseSerializer = self.serializer(instance=instance, many=many)
        data: Union[ReturnList, ReturnDict] = serializer.data.copy()
        try:
            result: Union[ReturnList, ReturnDict] = await self.__selected(request, data, many)
        except ViewException as e:
            await self.show_exception(e)
            return WebResponse(status=410, error=e)
        return WebResponse(data=result)

    async def __selected(self, request: WebRequest, data: Union[ReturnList, ReturnDict], many: bool) -> Union[
        ReturnDict, ReturnList]:
        try:
            data: Union[ReturnList, ReturnDict] = await self.selected(request, data, many)
        except Exception as e:
            raise await self.create_exception(e)
        if many and self.is_page:
            data: Dict[str, Any] = await self.page_instance.get_paginated_data(data)
        return data

    async def selected(self, request: WebRequest, data: Union[ReturnDict, ReturnList], many: bool) -> Union[
        ReturnDict, ReturnList]:
        return data

    async def before_create(self, request: WebRequest, params: Dict[str, Any]) -> Dict[str, Any]:
        return params

    async def __before_create(self, request: WebRequest, params: PARAMS_TYPE) -> Dict[str, Any]:
        try:
            return await self.before_create(request, params)
        except Exception as e:
            raise await self.create_exception(e)

    @swagger_auto_schema(
        request_body=swagger_type.request_post,
        responses=response_post)
    @method_decorator(async_rest_api("post"))
    async def post(self, request: WebRequest) -> WebResponse:
        self.config.printf.info(f"request success!\npath is {request.path}\nmethod is post")
        params: PARAMS_TYPE = request.params
        try:
            data: Dict[str, Any] = await self.__before_create(request, params)
        except ViewException as e:
            await self.show_exception(e)
            return WebResponse(status=400, error=e)
        serializer: BaseSerializer = self.serializer(data=data)
        try:
            await DjangoUtils.to_async_fun(serializer.is_valid, raise_exception=True)
        except Exception as e:
            _e: ViewException = await self.create_exception(e)
            await self.show_exception(_e)
            return WebResponse(status=401, error=_e)
        await serializer.async_save()
        try:
            result: ReturnDict = await self.__created(request, params, serializer)
        except ViewException as e:
            await self.show_exception(e)
            return WebResponse(status=410, error=e)
        return WebResponse(data=result)

    async def __created(self, request: WebRequest, params: PARAMS_TYPE, serializer: BaseSerializer) -> ReturnDict:
        try:
            return await self.created(request, params, serializer.data.copy())
        except Exception as e:
            raise await self.create_exception(e)

    async def created(self, request: WebRequest, params: Dict[str, Any], data: ReturnDict) -> ReturnDict:
        return data

    async def before_update(self, request: WebRequest, params: Dict[str, Any], instance: BaseModel) -> Tuple[
        Dict[str, Any], BaseModel]:
        return params, instance

    async def __before_update(self, request: WebRequest, params: PARAMS_TYPE, instance: BaseModel) -> Tuple[
        Dict[str, Any], BaseModel]:
        try:
            return await self.before_update(request, params, instance)
        except Exception as e:
            raise await self.create_exception(e)

    @swagger_auto_schema(
        request_body=swagger_type.request_put,
        responses=response_put)
    @method_decorator(async_rest_api("put"))
    async def put(self, request: WebRequest, id: Optional[str] = None):
        self.config.printf.info(f"request success!\npath is {request.path}\nmethod is put\nupdate id is {id}")
        try:
            assert id, ViewException("update id value isn't null!")
        except ViewException as e:
            await self.show_exception(e)
            return WebResponse(status=400, error=e)
        try:
            instance: BaseModel = await self.model.async_get_one(id)
        except ModelException as e:
            await self.show_exception(e)
            return WebResponse(status=404, error=e)
        params: PARAMS_TYPE = request.params
        try:
            params, instance = await self.__before_update(request, params, instance)
        except ViewException as e:
            await self.show_exception(e)
            return WebResponse(status=400, error=e)
        serializer: BaseSerializer = self.serializer(instance=instance, data=params)
        try:
            await DjangoUtils.to_async_fun(serializer.is_valid, raise_exception=True)
        except Exception as e:
            _e: ViewException = await self.create_exception(e)
            await self.show_exception(_e)
            return WebResponse(status=403, error=_e)
        await serializer.async_save()
        try:
            result: ReturnDict = await self.__updated(request, serializer, params)
        except ViewException as e:
            await self.show_exception(e)
            return WebResponse(status=410, error=e)
        return WebResponse(data=result)

    async def __updated(self, request: WebRequest, serializer: BaseSerializer, params: PARAMS_TYPE) -> ReturnDict:
        try:
            return await self.updated(request, serializer.data.copy(), params)
        except Exception as e:
            raise await self.create_exception(e)

    async def updated(self, request: WebRequest, data: ReturnDict, params: Dict[str, Any]) -> ReturnDict:
        return data

    async def before_delete(self, request: WebRequest, params: Dict[str, Any], many: bool,
                            instance: Optional[BaseModel] = None) -> Union[QuerySet[BaseModel], BaseModel]:
        return instance

    async def __before_delete(self, request: WebRequest, params: PARAMS_TYPE, many: bool,
                              delete_id: Optional[str] = None) -> Union[QuerySet[BaseModel], BaseModel]:
        instance: Optional[BaseModel] = None
        if not many:
            try:
                instance: BaseModel = await self.model.async_get_one(id=delete_id)
            except ModelException as e:
                raise e

        try:
            return await self.before_delete(request, params, many, instance)
        except Exception as e:
            raise await self.create_exception(e)

    @swagger_auto_schema(
        manual_parameters=swagger_type.request_delete['query'],
        request_body=swagger_type.request_delete['params'],
        responses=response_delete)
    @method_decorator(async_rest_api("delete"))
    async def delete(self, request: WebRequest, id: Optional[str] = None):
        self.config.printf.info(f"request success!\npath is {request.path}\nmethod is delete\ndelete id is {id}")
        params: PARAMS_TYPE = request.params
        many: bool = id is None
        try:
            instance: Union[QuerySet[BaseModel], BaseModel] = await self.__before_delete(request, params, many,
                                                                                         delete_id=id)
        except ViewException as e:
            await self.show_exception(e)
            return WebResponse(status=400)
        serializer: BaseSerializer = self.serializer(instance=instance, many=many)
        data: Union[ReturnList, ReturnDict] = serializer.data.copy()
        delete_count: int = 0
        if many:
            for item in instance:
                delete_count += 1
                if self.is_delete:
                    await item.adelete()
                else:
                    item.is_delete = True
                    await item.asave()
        else:
            delete_count += 1
            if self.is_delete:
                await instance.adelete()
            else:
                instance.is_delete = True
                await instance.asave()
        try:
            await self.__deleted(request, params, data)
        except ViewException as e:
            await self.show_exception(e)
            return WebResponse(status=410, error=e)
        return WebResponse(data={"delete_count": delete_count})

    async def __deleted(self, request: WebRequest, params: PARAMS_TYPE, data: Union[ReturnList, ReturnDict]):
        try:
            await self.deleted(request, params, data)
        except Exception as e:
            raise await self.create_exception(e)

    async def deleted(self, request: WebRequest, params: Dict[str, Any], data: Union[ReturnList, ReturnDict]):
        pass

    async def check(self, params: PARAMS_TYPE, require_fields: List[str]):
        for field in require_fields:
            assert field in params, ViewException(f"field name's {field} field isn't exist!")

    async def pop(self, data: ReturnDict, pop_field: List[str]) -> ReturnDict:
        for field in pop_field:
            data.pop(field)
        return data
