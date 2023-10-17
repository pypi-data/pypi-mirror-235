import functools
import traceback

from rest_framework.request import Request
from rest_framework.response import Response

from utils.exception import ViewException
from utils.web.django.conf import DjangoConfig
from utils.web.django.request import WebRequest
from utils.web.django.response import WebResponse

from .api_util import BaseRestAPI

from .._types import REST_API_TYPE, VIEW_TYPE, REST_VIEW_HANDLER_TYPE


def rest_api(method: str = "get") -> REST_API_TYPE:
    def decorator(fun: VIEW_TYPE) -> REST_VIEW_HANDLER_TYPE:
        def handler(request: Request, *args: ..., **kwargs: ...) -> Response:
            config: DjangoConfig = request.config
            base_rest_api: BaseRestAPI = BaseRestAPI(request, method, config)
            try:
                web_request: WebRequest = base_rest_api.request_init()
            except ViewException as e:
                config.printf.warning(e.error_summary)
                config.printf.error(e.error_detail)
                return WebResponse(status=403, error=e).to_rest_response()
            try:
                web_response: WebResponse = fun(web_request, *args, **kwargs)
            except Exception as e:
                err: ViewException = ViewException(str(e), error_detail=traceback.format_exc())
                config.printf.warning(err.error_summary)
                config.printf.error(err.error_detail)
                return WebResponse(status=410, error=err).to_rest_response()
            return web_response.to_rest_response()

        return handler

    return decorator


def async_rest_api(method: str = "get"):
    def decorator(fun):
        @functools.wraps(fun)
        async def handler(request: Request, *args: ..., **kwargs: ...):
            config: DjangoConfig = request.config
            base_rest_api: BaseRestAPI = BaseRestAPI(request, method, config)
            try:
                web_request: WebRequest = await base_rest_api.async_request_init()
            except ViewException as e:
                config.printf.warning(e.error_summary)
                config.printf.error(e.error_detail)
                return WebResponse(status=403, error=e).to_rest_response()
            try:
                web_response: WebResponse = await fun(web_request, *args, **kwargs)
            except ViewException as e:
                config.printf.warning(e.error_summary)
                config.printf.error(e.error_detail)
                return WebResponse(status=410, error=e).to_rest_response()
            except Exception as e:
                _e: ViewException = ViewException(str(e), traceback.format_exc())
                config.printf.error(_e.error_detail)
                config.printf.warning(_e.error_summary)
                return WebResponse(status=410, error=_e).to_rest_response()
            return web_response.to_rest_response()

        return handler

    return decorator
