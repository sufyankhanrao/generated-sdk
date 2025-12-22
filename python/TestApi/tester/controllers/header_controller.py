"""tester.

This file was automatically generated for Stamplay by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

# ruff: noqa: D410
from apimatic_core.request_builder import RequestBuilder
from apimatic_core.response_handler import ResponseHandler
from apimatic_core.types.parameter import Parameter

from tester.api_helper import APIHelper
from tester.configuration import Server
from tester.controllers.base_controller import (
    BaseController,
)
from tester.http.http_method_enum import HttpMethodEnum
from tester.models.server_response import ServerResponse


class HeaderController(BaseController):
    """A Controller to access Endpoints in the tester API."""

    def __init__(self, config):
        """Initialize HeaderController object."""
        super(HeaderController, self).__init__(config)

    def send_headers(self,
                     custom_header,
                     value):
        """Perform a POST request to /header.

        Sends a single header params

        Args:
            custom_header (str): The request header parameter.
            value (str): Represents the value of the custom header

        Returns:
            ApiResponse: An object with the response value as well as other useful
                information such as status codes and headers.

        Raises:
            APIException: When an error occurs while fetching the data from the
                remote API. This exception includes the HTTP Response code, an error
                message, and the HTTP body that was received in the request.

        """
        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path("/header")
            .http_method(HttpMethodEnum.POST)
            .header_param(Parameter()
                .key("custom-header")
                .value(custom_header)
                .is_required(True))
            .form_param(Parameter()
                .key("value")
                .value(value)
                .is_required(True))
            .header_param(Parameter()
                            .key("content-type")
                            .value("application/x-www-form-urlencoded"))
            .header_param(Parameter()
                .key("accept")
                .value("application/json")),
        ).response(
            ResponseHandler()
            .is_nullify404(True)
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(ServerResponse.from_dictionary)
            .is_api_response(True),
        ).execute()
