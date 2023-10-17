from typing import Optional, List, Dict, Any, Union

from drf_yasg.openapi import Schema

from ._types import SwaggerParamsEnum


class SwaggerParams():
    type: Union[SwaggerParamsEnum, Any]
    title: Optional[str]
    require: Optional[List[str]]
    description: Optional[str]
    properties: Optional[Dict[str, Schema]]

    def __init__(self, type: Union[SwaggerParamsEnum, Any], title: Optional[str] = None,
                 require: Optional[List[str]] = None,
                 description: Optional[str] = None):
        self.type = type
        self.title = title
        self.require = require
        self.description = description

    def schema(self, properties: Optional[Dict[str, Schema]] = None) -> Schema:
        return Schema(
            title=self.title,
            type=self.type.value,
            required=self.require,
            description=self.description,
            properties=properties
        )



if __name__ == '__main__':
    from drf_yasg.openapi import TYPE_OBJECT
