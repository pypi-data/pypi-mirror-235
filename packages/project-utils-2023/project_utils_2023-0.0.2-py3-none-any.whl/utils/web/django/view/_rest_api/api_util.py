from rest_framework.request import Request

from utils.web.django.view._base import Base
from utils.web.django.view._types import PARAMS_TYPE


class BaseRestAPI(Base):
    request: Request

    def parse_params(self) -> PARAMS_TYPE:
        method: str = self.method.lower()
        params: PARAMS_TYPE = {}
        if method in ("get", "delete"):
            params.update(self.request.query_params)
        elif method in ("post", "put", "delete"):
            params.update(self.request.data)
        return params
