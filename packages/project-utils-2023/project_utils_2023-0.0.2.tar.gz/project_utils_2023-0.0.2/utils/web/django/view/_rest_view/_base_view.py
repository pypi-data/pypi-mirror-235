import traceback

from abc import ABCMeta
from typing import Optional, List, Dict, Any, Union, Tuple

from django.db.models import Q
from django.db.models.query import QuerySet
from django.utils.decorators import method_decorator

from rest_framework.views import APIView
from rest_framework.serializers import ReturnDict, ReturnList

from utils.exception import ModelException, ViewException, DjangoWebException
from utils.web.django.conf import DjangoConfig
from utils.web.django.model import BaseModel
from utils.web.django.serializer import BaseSerializer
from utils.web.django.pagination import BasePageNumberPagination
from utils.web.django.request import WebRequest
from utils.web.django.response import ResponseModel as WebResponse
from utils.web.django.view._types import PARAMS_TYPE
from utils.web.django.view import rest_api


class BaseRestAPIView(APIView, metaclass=ABCMeta):
    config: DjangoConfig
    model: BaseModel
    serializer: BaseSerializer
    page_class: BasePageNumberPagination

    # 删除标记，False表示逻辑删除，True表示物理删除
    is_delete: bool = False
    # 过滤连接条件
    filter_condition: str = "OR"
    # 过滤符号
    filter_symbol: str = "contains"

    page_instance: BasePageNumberPagination
    is_page: bool

    def create_exception(self, e: Exception) -> ViewException:
        return ViewException(str(e), traceback.format_exc())

    def show_exception(self, e: DjangoWebException):
        self.config.printf.error(e.error_detail)
        self.config.printf.warning(e.error_summary)

    def __get_filter_field(self, params: PARAMS_TYPE) -> Dict[str, Any]:
        field: List[str] = self.model.get_fields()
        params_keys: List[str] = list(params.keys())
        filter_field: List[str] = list(set(field) & set(params_keys))
        filter_mapper: Dict[str, Any] = {key: params.get(key)[0] for key in filter_field}
        return filter_mapper

    def __filter(self, params: PARAMS_TYPE) -> QuerySet[BaseModel]:
        filter_field: Dict[str, Any] = self.__get_filter_field(params)
        instance: QuerySet[BaseModel] = self.model.objects.filter(is_delete=0)
        q: Q = Q()
        q.connector = self.filter_symbol
        for key, val in filter_field.items():
            if key == "is_delete":
                q.children.append((key, val))
            else:
                q.children.append((f"{key}__{self.filter_symbol}", val))
        return instance.filter(q)

    def before_select(self, request: WebRequest, instance: Union[QuerySet[BaseModel], BaseModel], many: bool) -> \
            Union[QuerySet[BaseModel], BaseModel]:
        return instance

    def __before_select(self, request: WebRequest, params: PARAMS_TYPE, many: bool, select_id: Optional[str]) -> \
            Union[QuerySet[BaseModel], BaseModel]:
        if many:
            instance: QuerySet[BaseModel] = self.__filter(params)
            self.is_page = True
        else:
            instance: BaseModel = self.model.get_one(select_id)
        try:
            instance: Union[QuerySet[BaseModel], BaseModel] = self.before_select(request, instance, many)
            if not many and instance.is_delete:
                raise Exception("not find!")
        except Exception as e:
            raise self.create_exception(e)
        if many and self.is_page:
            self.page_instance = self.page_class()
            instance: QuerySet[BaseModel] = self.page_instance.paginate_queryset(instance, request.request, view=self)
        return instance

    @method_decorator(rest_api())
    def get(self, request: WebRequest, id: Optional[str] = None) -> WebResponse:
        self.config.printf.info(f"request success!\npath is {request.path}\nmethod is get\nselect id is {id}")
        params: PARAMS_TYPE = request.params
        many: bool = id is None
        try:
            instance: QuerySet[BaseModel] = self.__before_select(request, params, many, id)
        except ViewException as e:
            self.show_exception(e)
            return WebResponse(status=410, error=e)
        serializer: BaseSerializer = self.serializer(instance=instance, many=many)
        data: Union[ReturnDict, ReturnList] = serializer.data.copy()
        try:
            data = self.__selected(request, data, many)
        except ViewException as e:
            self.show_exception(e)
            return WebResponse(status=410, error=e)
        return WebResponse(data=data)

    def __selected(self, request: WebRequest, data: Union[ReturnList, ReturnDict], many: bool) -> Union[
        ReturnDict, ReturnList]:
        try:
            data: Union[ReturnList, ReturnDict] = self.selected(request, data, many)
        except Exception as e:
            raise self.create_exception(e)
        if many and self.is_page:
            data: Dict[str, Any] = self.page_instance.get_paginated_response(data)
        return data

    def selected(self, request: WebRequest, data: Union[ReturnDict, ReturnList], many: bool) -> Union[
        ReturnDict, ReturnList]:
        return data

    def before_create(self, request: WebRequest, params: Dict[str, Any]) -> Dict[str, Any]:
        return params

    def __before_create(self, request: WebRequest, params: PARAMS_TYPE) -> Dict[str, Any]:
        try:
            return self.before_create(request, params)
        except Exception as e:
            raise self.create_exception(e)

    @method_decorator(rest_api("post"))
    def post(self, request: WebRequest) -> WebResponse:
        self.config.printf.info(f"request success!\npath is {request.path}\nmethod is post")
        params: PARAMS_TYPE = request.params
        try:
            data: Dict[str, Any] = self.__before_create(request, params)
        except ViewException as e:
            self.show_exception(e)
            return WebResponse(status=400, error=e)
        serializer: BaseSerializer = self.serializer(data=data)
        try:
            serializer.is_valid(raise_exception=True)
        except Exception as e:
            _e = self.create_exception(e)
            self.show_exception(_e)
            return WebResponse(status=401, error=_e)
        serializer.save()
        try:
            result: ReturnDict = self.__created(request, params, serializer)
        except ViewException as e:
            self.show_exception(e)
            return WebResponse(status=410, error=e)
        return WebResponse(data=result)

    def __created(self, request: WebRequest, params: PARAMS_TYPE, serializer: BaseSerializer) -> ReturnDict:
        try:
            return self.created(request, params, serializer.data.copy())
        except Exception as e:
            raise self.create_exception(e)

    def created(self, request: WebRequest, params: Dict[str, Any], data: ReturnDict) -> ReturnDict:
        return data

    def before_update(self, request: WebRequest, params: Dict[str, Any], instance: BaseModel) -> Tuple[
        Dict[str, Any], BaseModel]:
        return params, instance

    def __before_update(self, request: WebRequest, params: PARAMS_TYPE, instance: BaseModel) -> Tuple[
        Dict[str, Any], BaseModel]:
        try:
            return self.before_update(request, params, instance)
        except Exception as e:
            raise self.create_exception(e)

    @method_decorator(rest_api("put"))
    def put(self, request: WebRequest, id: Optional[str] = None) -> WebResponse:
        self.config.printf.info(f"request success!\npath is {request.path}\nmethod is put\nupdate id is {id}")
        try:
            assert id, ViewException("update id value isn't null!")
        except ViewException as e:
            self.show_exception(e)
            return WebResponse(status=400, error=e)
        try:
            instance: BaseModel = self.model.get_one(id)
        except ModelException as e:
            self.show_exception(e)
            return WebResponse(status=404, error=e)
        params: PARAMS_TYPE = request.params
        try:
            params, instance = self.__before_update(request, params, instance)
        except ViewException as e:
            self.show_exception(e)
            return WebResponse(status=401, error=e)
        serializer: BaseSerializer = self.serializer(instance=instance, data=params)
        try:
            serializer.is_valid(raise_exception=True)
        except Exception as e:
            _e: ViewException = self.create_exception(e)
            self.show_exception(_e)
            return WebResponse(status=402, error=_e)
        serializer.save()
        try:
            result: ReturnDict = self.__updated(request, serializer, params)
        except ViewException as e:
            self.show_exception(e)
            return WebResponse(status=410, error=e)
        return WebResponse(data=result)

    def __updated(self, request: WebRequest, serializer: BaseSerializer, params: PARAMS_TYPE) -> ReturnDict:
        try:
            return self.updated(request, serializer.data.copy(), params)
        except Exception as e:
            raise self.create_exception(e)

    def updated(self, request: WebRequest, data: ReturnDict, params: Dict[str, Any]) -> ReturnDict:
        return data

    def before_delete(self, request: WebRequest, params: Dict[str, Any], many: bool,
                      instance: Optional[BaseModel] = None) -> Union[QuerySet[BaseModel], BaseModel]:
        return instance

    def __before_delete(self, request: WebRequest, params: PARAMS_TYPE, many: bool,
                        delete_id: Optional[str] = None) -> Union[QuerySet[BaseModel], BaseModel]:
        instance: Optional[BaseModel] = None
        if not many:
            try:
                instance = self.model.get_one(delete_id)
            except ModelException as e:
                raise self.create_exception(e)
        try:
            return self.before_delete(request, params, many, instance)
        except Exception as e:
            raise self.create_exception(e)

    @method_decorator(rest_api("delete"))
    def delete(self, request: WebRequest, id: Optional[str] = None) -> WebResponse:
        self.config.printf.info(f"request success!\npath is {request.path}\nmethod is delete\ndelete id is {id}")
        many: bool = id is None
        params: PARAMS_TYPE = request.params
        try:
            delete: Union[QuerySet[BaseModel], BaseModel] = self.__before_delete(request, params, many, id)
        except ViewException as e:
            self.show_exception(e)
            return WebResponse(status=404, error=e)
        serializer: BaseSerializer = self.serializer(instance=delete, many=many)
        data: Union[ReturnList, ReturnDict] = serializer.data.copy()
        delete_count: int = 0
        if many:
            for delete_item in delete:
                delete_count += 1
                if self.is_delete:
                    delete_item.delete()
                else:
                    delete_item.is_delete = True
                    delete_item.save()
        else:
            delete_count += 1
            if self.is_delete:
                delete.delete()
            else:
                delete.is_delete = True
                delete.save()
        try:
            self.__deleted(request, params, data)
        except ViewException as e:
            self.show_exception(e)
            return WebResponse(status=410, error=e)
        return WebResponse(data={"delete_count": delete_count})

    def __deleted(self, request: WebRequest, params: PARAMS_TYPE, data: Union[ReturnList, ReturnDict]):
        try:
            self.deleted(request, params, data)
        except Exception as e:
            raise self.create_exception(e)

    def deleted(self, request: WebRequest, params: Dict[str, Any], data: Union[ReturnList, ReturnDict]):
        pass
