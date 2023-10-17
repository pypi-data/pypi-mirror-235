from copy import deepcopy
from drf_yasg.openapi import Schema
from typing import Dict, Optional

from .. import params_types
from ._base import SwaggerResponseBase


class SwaggerResponse:
    base: Dict[str, Schema] = {
        "errno": SwaggerResponseBase(params_types.integer, "响应码").response(),
        "errmsg": SwaggerResponseBase(params_types.string, "响应状态").response()
    }

    def success(self, properties: Optional[Dict[str, Schema]] = None) -> Schema:
        base: Dict[str, Schema] = deepcopy(self.base)
        if properties:
            base.update({
                "data": SwaggerResponseBase(params_types.object, description="响应数据").response(properties=properties)
            })
        return Schema(type=params_types.object.value, properties=base)

    def error(self) -> Schema:
        base: Dict[str, Schema] = deepcopy(self.base)
        base.update({
            "error": SwaggerResponseBase(params_types.string, "错误信息").response()
        })
        return Schema(type=params_types.object.value, properties=base)
