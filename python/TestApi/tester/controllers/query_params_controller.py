"""tester.

This file was automatically generated for Stamplay by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

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


class QueryParamsController(BaseController):
    """A Controller to access Endpoints in the tester API."""

    def __init__(self, config):
        """Initialize QueryParamsController object."""
        super(QueryParamsController, self).__init__(config)

    def send_number_as_optional(self,
                                number,
                                number_1=None):
        """Perform a GET request to /query/numberAsOptional.

        Args:
            number (int): The request query parameter.
            number_1 (int, optional): The request query parameter.

        Returns:
            ApiResponse: An object with the response value as well as other
                useful information such as status codes and headers.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path("/query/numberAsOptional")
            .http_method(HttpMethodEnum.GET)
            .query_param(Parameter()
                         .key("number")
                         .value(number)
                         .is_required(True))
            .query_param(Parameter()
                         .key("number1")
                         .value(number_1))
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

    def send_long_as_optional(self,
                              long,
                              long_1=None):
        """Perform a GET request to /query/longAsOptional.

        Args:
            long (int): The request query parameter.
            long_1 (int, optional): The request query parameter.

        Returns:
            ApiResponse: An object with the response value as well as other
                useful information such as status codes and headers.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path("/query/longAsOptional")
            .http_method(HttpMethodEnum.GET)
            .query_param(Parameter()
                         .key("long")
                         .value(long)
                         .is_required(True))
            .query_param(Parameter()
                         .key("long1")
                         .value(long_1))
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

    def precision_as_optional(self,
                              precision,
                              precision_1=None):
        """Perform a GET request to /query/precisionAsOptional.

        Args:
            precision (float): The request query parameter.
            precision_1 (float, optional): The request query parameter.

        Returns:
            ApiResponse: An object with the response value as well as other
                useful information such as status codes and headers.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path("/query/precisionAsOptional")
            .http_method(HttpMethodEnum.GET)
            .query_param(Parameter()
                         .key("precision")
                         .value(precision)
                         .is_required(True))
            .query_param(Parameter()
                         .key("precision1")
                         .value(precision_1))
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

    def boolean_as_optional(self,
                            boolean,
                            boolean_1=None):
        """Perform a GET request to /query/booleanAsOptional.

        Args:
            boolean (bool): The request query parameter.
            boolean_1 (bool, optional): The request query parameter.

        Returns:
            ApiResponse: An object with the response value as well as other
                useful information such as status codes and headers.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path("/query/booleanAsOptional")
            .http_method(HttpMethodEnum.GET)
            .query_param(Parameter()
                         .key("boolean")
                         .value(boolean)
                         .is_required(True))
            .query_param(Parameter()
                         .key("boolean1")
                         .value(boolean_1))
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

    def rfc_1123_datetime_as_optional(self,
                                      date_time,
                                      date_time_1=None):
        """Perform a GET request to /query/rfc1123dateTimeAsOptional.

        Args:
            date_time (datetime): The request query parameter.
            date_time_1 (datetime, optional): The request query parameter.

        Returns:
            ApiResponse: An object with the response value as well as other
                useful information such as status codes and headers.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path("/query/rfc1123dateTimeAsOptional")
            .http_method(HttpMethodEnum.GET)
            .query_param(Parameter()
                         .key("dateTime")
                         .value(APIHelper.when_defined(APIHelper.HttpDateTime,
                             date_time))
                         .is_required(True))
            .query_param(Parameter()
                         .key("dateTime1")
                         .value(APIHelper.when_defined(APIHelper.HttpDateTime,
                             date_time_1)))
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

    def rfc_3339_datetime_as_optional(self,
                                      date_time,
                                      date_time_1=None):
        """Perform a GET request to /query/rfc3339dateTimeAsOptional.

        Args:
            date_time (datetime): The request query parameter.
            date_time_1 (datetime, optional): The request query parameter.

        Returns:
            ApiResponse: An object with the response value as well as other
                useful information such as status codes and headers.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path("/query/rfc3339dateTimeAsOptional")
            .http_method(HttpMethodEnum.GET)
            .query_param(Parameter()
                         .key("dateTime")
                         .value(APIHelper.when_defined(APIHelper.RFC3339DateTime,
                             date_time))
                         .is_required(True))
            .query_param(Parameter()
                         .key("dateTime1")
                         .value(APIHelper.when_defined(APIHelper.RFC3339DateTime,
                             date_time_1)))
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

    def send_date_as_optional(self,
                              date,
                              date_1=None):
        """Perform a GET request to /query/dateAsOptional.

        Args:
            date (date): The request query parameter.
            date_1 (date, optional): The request query parameter.

        Returns:
            ApiResponse: An object with the response value as well as other
                useful information such as status codes and headers.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path("/query/dateAsOptional")
            .http_method(HttpMethodEnum.GET)
            .query_param(Parameter()
                         .key("date")
                         .value(date)
                         .is_required(True))
            .query_param(Parameter()
                         .key("date1")
                         .value(date_1))
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

    def send_string_as_optional(self,
                                string,
                                string_1=None):
        """Perform a GET request to /query/stringAsOptional.

        Args:
            string (str): The request query parameter.
            string_1 (str, optional): The request query parameter.

        Returns:
            ApiResponse: An object with the response value as well as other
                useful information such as status codes and headers.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path("/query/stringAsOptional")
            .http_method(HttpMethodEnum.GET)
            .query_param(Parameter()
                         .key("string")
                         .value(string)
                         .is_required(True))
            .query_param(Parameter()
                         .key("string1")
                         .value(string_1))
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

    def unixdatetime_as_optional(self,
                                 date_time,
                                 date_time_1=None):
        """Perform a GET request to /query/unixdateTimeAsOptional.

        Args:
            date_time (datetime): The request query parameter.
            date_time_1 (datetime, optional): The request query parameter.

        Returns:
            ApiResponse: An object with the response value as well as other
                useful information such as status codes and headers.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path("/query/unixdateTimeAsOptional")
            .http_method(HttpMethodEnum.GET)
            .query_param(Parameter()
                         .key("dateTime")
                         .value(APIHelper.when_defined(APIHelper.UnixDateTime,
                             date_time))
                         .is_required(True))
            .query_param(Parameter()
                         .key("dateTime1")
                         .value(APIHelper.when_defined(APIHelper.UnixDateTime,
                             date_time_1)))
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
