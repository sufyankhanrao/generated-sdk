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
from tester.models.echo_response import EchoResponse


class EchoController(BaseController):
    """A Controller to access Endpoints in the tester API."""

    def __init__(self, config):
        """Initialize EchoController object."""
        super(EchoController, self).__init__(config)

    def json_echo(self,
                  input):
        """Perform a POST request to /.

        Echo's back the request

        Args:
            input (Any): The request body parameter.

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
            .path("/")
            .http_method(HttpMethodEnum.POST)
            .query_param(Parameter()
                .key("echo")
                .value(True))
            .body_param(Parameter()
                .value(input)
                .is_required(True))
            .header_param(Parameter()
                .key("content-type")
                .value("application/json; charset=utf-8"))
            .header_param(Parameter()
                .key("accept")
                .value("application/json"))
            .body_serializer(APIHelper.json_serialize),
        ).response(
            ResponseHandler()
            .is_nullify404(True)
            .deserializer(APIHelper.dynamic_deserialize)
            .is_api_response(True),
        ).execute()

    def form_echo(self,
                  input):
        """Perform a POST request to /.

        Sends the request including any form params as JSON

        Args:
            input (Any): The request form parameter.

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
            .path("/")
            .http_method(HttpMethodEnum.POST)
            .form_param(Parameter()
                .key("input")
                .value(input)
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
            .deserializer(APIHelper.dynamic_deserialize)
            .is_api_response(True),
        ).execute()

    def query_echo(self,
                   _optional_query_parameters=None):
        """Perform a GET request to /.

        Args:
            _optional_query_parameters (Array, optional): Additional optional query
                parameters are supported by this endpoint

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
            .path("/")
            .http_method(HttpMethodEnum.GET)
            .header_param(Parameter()
                .key("accept")
                .value("application/json"))
            .additional_query_params(_optional_query_parameters),
        ).response(
            ResponseHandler()
            .is_nullify404(True)
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(EchoResponse.from_dictionary)
            .is_api_response(True),
        ).execute()
