import jwt
import uuid
import json
import base64

from abc import ABCMeta
from typing import Optional, Dict, Any, Union, List

from django.conf import settings
from django.contrib.auth import authenticate
from django.utils.decorators import method_decorator

from rest_framework.serializers import ReturnDict

from drf_yasg.openapi import Schema
from drf_yasg.utils import swagger_auto_schema

from utils.time import compute_day
from utils.exception import ViewException
from utils.web.django.view import BaseView, rest_api, AsyncBaseView, async_rest_api
from utils.web.django.request import WebRequest
from utils.web.django.response import WebResponse
from utils.web.django.serializer import BaseSerializer
from utils.web.django.swagger import params, params_types, swagger_response, response_params

from ._model import BaseUserModel


class BaseUserLoginView(BaseView, metaclass=ABCMeta):
    require: List[str] = ["username", "password", "checkcode"]
    request_body: Schema = params(
        type=params_types.object,
        require=require
    ).schema({
        "username": params(params_types.string, description="用户名").schema(),
        "password": params(params_types.string, description="密码").schema(),
        "checkcode": params(params_types.string, description="校验码").schema()

    })
    get_response_body: Dict[Union[str, int], Schema] = {
        200: swagger_response().success({
            "code": response_params(params_types.string, description="校验码").response()
        })
    }
    post_response_body: Dict[Union[str, int], Schema] = {
        200: swagger_response().success({
            "user_info": response_params(params_types.object, description="用户信息").response(properties={
                "id": response_params(params_types.string, description="用户ID").response(),
                "register_time": response_params(params_types.string, description="注册时间").response(),
                "username": response_params(params_types.string, description="用户名").response(),
                "email": response_params(params_types.string, description="邮箱").response()
            }),
            "usertoken": response_params(params_types.string, description="token令牌").response()
        }),
        400: swagger_response().error()
    }

    def dispatch(self, request, *args, **kwargs):
        request.config = self.config
        return super().dispatch(request, *args, **kwargs)

    @swagger_auto_schema(responses=get_response_body)
    @method_decorator(rest_api())
    def get(self, request: WebRequest, id: Optional[str] = None) -> WebResponse:
        self.config.printf.info(f"request success!\npath is {request.path}\nmethod is get\nselect id is {id}")
        user_code: str = uuid.uuid4().hex[:12]
        request.session["user_code"] = user_code
        self.config.printf.success(f"current request user code's {user_code}")
        return WebResponse(data={"code": user_code})

    @swagger_auto_schema(request_body=request_body, responses=post_response_body)
    @method_decorator(rest_api("post"))
    def post(self, request: WebRequest) -> WebResponse:
        self.config.printf.info(f"request success!\npath is {request.path}\nmethod is get\nselect id is {id}")
        params: Dict[str, Any] = request.params
        try:
            self.check(params, ["username", "password", "checkcode"])
        except ViewException as e:
            self.show_exception(e)
            return WebResponse(status=403, error=e)
        usercode: Optional[str] = request.session.get("user_code")
        try:
            assert usercode, ViewException("user code not in session!")
        except ViewException as e:
            self.show_exception(e)
            return WebResponse(status=403, error=e)
        username: str = params.get("username")
        password: str = params.get("password")
        checkcode: str = params.get("checkcode")
        try:
            code: str = base64.b64decode(checkcode).decode("utf-8")
        except Exception as e:
            err_: ViewException = self.create_exception(e)
            self.show_exception(err_)
            return WebResponse(status=403, error=err_)
        checkcode_: str = code.split("_")[1]
        try:
            assert usercode == checkcode_, ViewException(
                "request checkcode value and session checkcode value not match!")
        except ViewException as e:
            self.show_exception(e)
            return WebResponse(status=403, error=e)
        user: Optional[BaseUserModel] = authenticate(username=username, password=password)
        try:
            assert user, ViewException("username or password no match!")
        except ViewException as e:
            self.show_exception(e)
            return WebResponse(status=403, error=e)
        serializer: BaseSerializer = self.serializer(instance=user)
        data: ReturnDict = serializer.data.copy()
        exp: float = compute_day(7).timestamp()
        payload: Dict[str, Union[str, float]] = {"exp": exp, "user": json.dumps(data)}
        token: str = jwt.encode(payload, settings.SECRET_KEY, algorithm="HS256")
        request.session.setdefault("usertoken", token)
        data.pop("password")
        data.pop("last_login")
        data.pop("is_superuser")
        data.pop("first_name")
        data.pop("last_name")
        data.pop("is_staff")
        data.pop("is_active")
        data.pop("date_joined")
        data.pop("is_delete")
        data.pop("groups")
        data.pop("user_permissions")
        return WebResponse(data={"user_info": data, "usertoken": token})


class AsyncBaseUserLoginView(AsyncBaseView, metaclass=ABCMeta):
    require: List[str] = ["username", "password", "checkcode"]
    request_body: Schema = params(
        type=params_types.object,
        require=require
    ).schema({
        "username": params(params_types.string, description="用户名").schema(),
        "password": params(params_types.string, description="密码").schema(),
        "checkcode": params(params_types.string, description="校验码").schema()

    })
    get_response_body: Dict[Union[str, int], Schema] = {
        200: swagger_response().success({
            "code": response_params(params_types.string, description="校验码").response()
        })
    }
    post_response_body: Dict[Union[str, int], Schema] = {
        200: swagger_response().success({
            "user_info": response_params(params_types.object, description="用户信息").response(properties={
                "id": response_params(params_types.string, description="用户ID").response(),
                "register_time": response_params(params_types.string, description="注册时间").response(),
                "username": response_params(params_types.string, description="用户名").response(),
                "email": response_params(params_types.string, description="邮箱").response()
            }),
            "usertoken": response_params(params_types.string, description="token令牌").response()
        }),
        400: swagger_response().error()
    }

    @swagger_auto_schema(responses=get_response_body)
    @method_decorator(async_rest_api())
    async def get(self, request: WebRequest, id: Optional[str] = None) -> WebResponse:
        self.config.printf.info(f"request success!\npath is {request.path}\nmethod is get\nselect id is {id}")
        user_code: str = uuid.uuid4().hex[:12]
        request.session["user_code"] = user_code
        self.config.printf.success(f"current request user code's {user_code}")
        return WebResponse(data={"code": user_code})

    @swagger_auto_schema(request_body=request_body, responses=post_response_body)
    @method_decorator(rest_api("post"))
    async def post(self, request: WebRequest) -> WebResponse:
        self.config.printf.info(f"request success!\npath is {request.path}\nmethod is get\nselect id is {id}")
        params: Dict[str, Any] = request.params
        try:
            await self.check(params, ["username", "password", "checkcode"])
        except ViewException as e:
            await self.show_exception(e)
            return WebResponse(status=403, error=e)
        usercode: Optional[str] = request.session.get("user_code")
        try:
            assert usercode, ViewException("user code not in session!")
        except ViewException as e:
            await self.show_exception(e)
            return WebResponse(status=403, error=e)
        username: str = params.get("username")
        password: str = params.get("password")
        checkcode: str = params.get("checkcode")
        try:
            code: str = base64.b64decode(checkcode).decode("utf-8")
        except Exception as e:
            err_: ViewException = await self.create_exception(e)
            await self.show_exception(err_)
            return WebResponse(status=403, error=err_)
        checkcode_: str = code.split("_")[1]
        try:
            assert usercode == checkcode_, ViewException(
                "request checkcode value and session checkcode value not match!")
        except ViewException as e:
            await self.show_exception(e)
            return WebResponse(status=403, error=e)
        user: Optional[BaseUserModel] = authenticate(username=username, password=password)
        try:
            assert user, ViewException("username or password no match!")
        except ViewException as e:
            await self.show_exception(e)
            return WebResponse(status=403, error=e)
        serializer: BaseSerializer = self.serializer(instance=user)
        data: ReturnDict = serializer.data.copy()
        exp: float = compute_day(7).timestamp()
        payload: Dict[str, Union[str, float]] = {"exp": exp, "user": json.dumps(data)}
        token: str = jwt.encode(payload, settings.SECRET_KEY, algorithm="HS256")
        request.session.setdefault("usertoken", token)
        data.pop("password")
        data.pop("last_login")
        data.pop("is_superuser")
        data.pop("first_name")
        data.pop("last_name")
        data.pop("is_staff")
        data.pop("is_active")
        data.pop("date_joined")
        data.pop("is_delete")
        data.pop("groups")
        data.pop("user_permissions")
        return WebResponse(data={"user_info": data, "usertoken": token})
