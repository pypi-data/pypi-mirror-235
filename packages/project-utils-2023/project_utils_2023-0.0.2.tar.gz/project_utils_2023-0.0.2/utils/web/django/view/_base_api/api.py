import functools

from loguru._logger import Logger

from utils.exception import ViewException
from utils.web.django.view._base_api.api_util import BaseAPIUtil
from utils.web.django.conf._django_config import DjangoConfig
from utils.web.django.view._types import *


def base_api(config: DjangoConfig, method: str = "get") -> BASE_API_TYPE:
    def decorator(fun: VIEW_TYPE) -> API_VIEW_HANDLER_TYPE:
        def handler(request: HttpRequest, *args: ..., **kwargs: ...) -> HttpResponse:
            try:
                api_util: BaseAPIUtil = BaseAPIUtil(config=config, request=request, method=method)
            except ViewException as e:
                config.printf.warning(e.error_summary)
                config.printf.error(e.error_detail)
                return WebResponse(status=405, error=e).to_response()
            try:
                web_request: WebRequest = api_util.request_init()
            except ViewException as e:
                config.printf.warning(e.error_summary)
                config.printf.error(e.error_detail)
                return WebResponse(status=403, error=e).to_response()
            try:
                web_response: WebResponse = fun(web_request, *args, **kwargs)
            except ViewException as e:
                config.printf.warning(e.error_summary)
                config.printf.error(e.error_detail)
                return WebResponse(status=410, error=e).to_response()
            return web_response.to_response()

        return handler

    return decorator


def async_base_api(config: DjangoConfig, method: str = "get"):
    printf: Logger = config.printf

    def decorator(fun):
        @functools.wraps(fun)
        async def handler(request, *args, **kwargs):
            try:
                api_util: BaseAPIUtil = BaseAPIUtil(request, method, config=config)
            except ViewException as e:
                printf.warning(e.error_summary)
                printf.error(e.error_detail)
                return WebResponse(status=405, error=e).to_response()
            try:
                web_request: WebRequest = await api_util.async_request_init()
            except ViewException as e:
                printf.warning(e.error_summary)
                printf.error(e.error_detail)
                return WebResponse(status=403, error=e).to_response()
            try:
                web_response: WebResponse = await fun(web_request, *args, **kwargs)
            except ViewException as e:
                printf.warning(e.error_summary)
                printf.error(e.error_detail)
                return WebResponse(status=410, error=e).to_response()
            return web_response.to_response()

        return handler

    return decorator
