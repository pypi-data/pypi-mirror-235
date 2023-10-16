import json

from django.http.request import HttpRequest

from utils.exception import ViewException
from utils.web.django.conf._django_config import DjangoConfig
from utils.web.django.view._base import Base, PARAMS_TYPE


class BaseAPIUtil(Base):
    request: HttpRequest

    def __init__(self, request: HttpRequest, method: str, config: DjangoConfig):
        super().__init__(request, method, config)
        request_method: str = request.method
        assert request_method.lower() == method.lower(), ViewException("request method isn't match")

    def parse_params(self) -> PARAMS_TYPE:
        method: str = self.method.lower()
        params: PARAMS_TYPE = {}
        if method in ("get", "delete"):
            params.update(self.request.GET.dict())
        if method in ("post", "put", "delete"):
            params.update(json.loads(self.request.body.decode("utf-8")))
        return params
