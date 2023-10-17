import traceback
import functools

from loguru._logger import Logger

from django.http.request import HttpRequest
from django.http.response import HttpResponse

from utils.exception import ViewException
from utils.web.django.conf import DjangoConfig
from utils.web.django.request import WebRequest
from utils.web.django.response import WebResponse

from .api_util import BaseAPIUtil

from .._types import BASE_API_TYPE, VIEW_TYPE, API_VIEW_HANDLER_TYPE


def base_api(config: DjangoConfig, method: str = "get") -> BASE_API_TYPE:
    def decorator(fun: VIEW_TYPE) -> API_VIEW_HANDLER_TYPE:
        def handler(request: HttpRequest, *args: ..., **kwargs: ...) -> HttpResponse:
            try:
                api_util: BaseAPIUtil = BaseAPIUtil(config=config, request=request, method=method)
            except ViewException as e:
                config.printf.warning(e.error_summary)
                config.printf.error(e.error_detail)
                return WebResponse(status=405, error=e).to_response()
            except Exception as e:
                view_exception: ViewException = ViewException(str(e), traceback.format_exc())
                config.printf.warning(view_exception.error_summary)
                config.printf.error(view_exception.error_detail)
                return WebResponse(status=405, error=view_exception).to_response()
            try:
                web_request: WebRequest = api_util.request_init()
            except ViewException as e:
                config.printf.warning(e.error_summary)
                config.printf.error(e.error_detail)
                return WebResponse(status=403, error=e).to_response()
            except Exception as e:
                view_exception: ViewException = ViewException(str(e), traceback.format_exc())
                config.printf.warning(view_exception.error_summary)
                config.printf.error(view_exception.error_detail)
                return WebResponse(status=403, error=view_exception).to_response()
            try:
                web_response: WebResponse = fun(web_request, *args, **kwargs)
            except ViewException as e:
                config.printf.warning(e.error_summary)
                config.printf.error(e.error_detail)
                return WebResponse(status=410, error=e).to_response()
            except Exception as e:
                view_exception: ViewException = ViewException(str(e), traceback.format_exc())
                config.printf.warning(view_exception.error_summary)
                config.printf.error(view_exception.error_detail)
                return WebResponse(status=410, error=view_exception).to_response()
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
