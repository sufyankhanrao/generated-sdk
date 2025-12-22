"""testerfilesandmultipart.

This file was automatically generated for Stamplay by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

# ruff: noqa: D410
from apimatic_core.request_builder import RequestBuilder
from apimatic_core.response_handler import ResponseHandler
from apimatic_core.types.parameter import Parameter

from testerfilesandmultipart.api_helper import (
    APIHelper,
)
from testerfilesandmultipart.configuration import (
    Server,
)
from testerfilesandmultipart.controllers.base_controller import (
    BaseController,
)
from testerfilesandmultipart.http.http_method_enum import (
    HttpMethodEnum,
)
from testerfilesandmultipart.models.server_response import (
    ServerResponse,
)


class BinaryParamsController(BaseController):
    """A Controller to access Endpoints in the testerfilesandmultipart API."""

    def __init__(self, config):
        """Initialize BinaryParamsController object."""
        super(BinaryParamsController, self).__init__(config)

    def send_file(self,
                  file):
        """Perform a POST request to /binary/file.

        Args:
            file (typing.BinaryIO): The request body parameter.

        Returns:
            ServerResponse: Response from the API.

        Raises:
            APIException: When an error occurs while fetching the data from the
                remote API. This exception includes the HTTP Response code, an error
                message, and the HTTP body that was received in the request.

        """
        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path("/binary/file")
            .http_method(HttpMethodEnum.POST)
            .body_param(Parameter()
                .value(file)
                .is_required(True))
            .query_param(Parameter()
                .key("is_image")
                .value("false"))
            .header_param(Parameter()
                .key("content-type")
                .value("application/octet-stream"))
            .header_param(Parameter()
                .key("accept")
                .value("application/json")),
        ).response(
            ResponseHandler()
            .is_nullify404(True)
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(ServerResponse.from_dictionary),
        ).execute()

    def send_image_with_constant_content_type(self,
                                              image):
        """Perform a POST request to /binary/file.

        Args:
            image (typing.BinaryIO): The request body parameter.

        Returns:
            ServerResponse: Response from the API.

        Raises:
            APIException: When an error occurs while fetching the data from the
                remote API. This exception includes the HTTP Response code, an error
                message, and the HTTP body that was received in the request.

        """
        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path("/binary/file")
            .http_method(HttpMethodEnum.POST)
            .header_param(Parameter()
                .key("content-type")
                .value("image/png"))
            .body_param(Parameter()
                .value(image)
                .is_required(True))
            .query_param(Parameter()
                .key("is_image")
                .value("true"))
            .header_param(Parameter()
                .key("accept")
                .value("application/json")),
        ).response(
            ResponseHandler()
            .is_nullify404(True)
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(ServerResponse.from_dictionary),
        ).execute()

    def send_image_with_configured_content_type(self,
                                                options=dict()):
        """Perform a POST request to /binary/file.

        Args:
            options (dict, optional): Key-value pairs for any of the parameters to
                this API Endpoint. All parameters to the endpoint are supplied
                through the dictionary with their names being the key and their
                desired values being the value. A list of parameters that can be used
                are::
                    content_type -- str -- The request header parameter.
                    image -- typing.BinaryIO -- The request body parameter.
                    is_image -- str -- The request query parameter. Example: true

        Returns:
            ServerResponse: Response from the API.

        Raises:
            APIException: When an error occurs while fetching the data from the
                remote API. This exception includes the HTTP Response code, an error
                message, and the HTTP body that was received in the request.

        """
        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path("/binary/file")
            .http_method(HttpMethodEnum.POST)
            .header_param(Parameter()
                .key("content-type")
                .value(options.get("content_type", None))
                .is_required(True))
            .body_param(Parameter()
                .value(options.get("image", None))
                .is_required(True))
            .query_param(Parameter()
                .key("is_image")
                .value(options.get("is_image", None))
                .is_required(True))
            .header_param(Parameter()
                .key("accept")
                .value("application/json")),
        ).response(
            ResponseHandler()
            .is_nullify404(True)
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(ServerResponse.from_dictionary),
        ).execute()
