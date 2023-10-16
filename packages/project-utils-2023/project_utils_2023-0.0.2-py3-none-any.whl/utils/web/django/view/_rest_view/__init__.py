from utils.web.django.view._rest_view._base_view import BaseRestAPIView
from utils.web.django.view._rest_view._async_view import AsyncAPIView
from utils.web.django.view._rest_view._async_base_view import AsyncBaseAPIView

BaseView = RestAPIView = RestView = BaseRestAPIView
AsyncView = AsyncAPIView
AsyncBaseView = AsyncBaseAPIView

__all__ = [
    "BaseView",
    "RestAPIView",
    "RestView",
    "BaseRestAPIView",
    "AsyncView",
    "AsyncAPIView",
    "AsyncBaseView",
    "AsyncBaseAPIView"
]
