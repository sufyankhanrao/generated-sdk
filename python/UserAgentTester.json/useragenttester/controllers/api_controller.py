"""useragenttester.

This file was automatically generated for Stamplay by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

# ruff: noqa: D410
from apimatic_core.request_builder import RequestBuilder
from apimatic_core.response_handler import ResponseHandler
from apimatic_core.types.parameter import Parameter

from useragenttester.api_helper import APIHelper
from useragenttester.configuration import Server
from useragenttester.controllers.base_controller import (
    BaseController,
)
from useragenttester.http.http_method_enum import (
    HttpMethodEnum,
)
from useragenttester.models.server_response import (
    ServerResponse,
)


class APIController(BaseController):
    """A Controller to access Endpoints in the useragenttester API."""

    def __init__(self, config):
        """Initialize APIController object."""
        super(APIController, self).__init__(config)

    def send_user_agent(self):
        """Perform a GET request to /response/testUserAgent.

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
            .path("/response/testUserAgent")
            .http_method(HttpMethodEnum.GET)
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
