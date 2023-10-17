from ._response import SwaggerResponse
from ._base import SwaggerResponseBase

swagger_response = SwaggerResponse
response_params = SwaggerResponseBase

__all__ = [
    "swagger_response",
    "SwaggerResponse",
    "response_params"
]
