from typing import Optional, Dict, Union, Any

from drf_yasg.openapi import Schema

from .. import params_types


class SwaggerResponseBase:
    type: str = params_types.object
    title: Optional[str]
    description: Optional[str]

    def __init__(self, type: Union[params_types, Any], title: Optional = None, description: Optional[str] = None):
        self.type = type.value
        self.title = title
        self.description = description

    def response(self, properties: Optional[Dict[str, Schema]] = None) -> Schema:
        return Schema(type=self.type, title=self.title, description=self.description, properties=properties)
