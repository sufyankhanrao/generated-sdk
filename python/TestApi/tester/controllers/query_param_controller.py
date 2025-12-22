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


class QueryParamController(BaseController):
    """A Controller to access Endpoints in the tester API."""

    def __init__(self, config):
        """Initialize QueryParamController object."""
        super(QueryParamController, self).__init__(config)

    def date_array(self,
                   dates):
        """Perform a GET request to /query/datearray.

        Args:
            dates (List[date]): The request query parameter.

        Returns:
            ServerResponse: Response from the API.

        Raises:
            APIException: When an error occurs while fetching the data from the
                remote API. This exception includes the HTTP Response code, an error
                message, and the HTTP body that was received in the request.

        """
        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path("/query/datearray")
            .http_method(HttpMethodEnum.GET)
            .query_param(Parameter()
                .key("dates")
                .value(dates)
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

    def optional_dynamic_query_param(self,
                                     name,
                                     _optional_query_parameters=None):
        """Perform a GET request to /query/optionalQueryParam.

        get optional dynamic query parameter

        Args:
            name (str): The request query parameter.
            _optional_query_parameters (Array, optional): Additional optional query
                parameters are supported by this endpoint

        Returns:
            ServerResponse: Response from the API.

        Raises:
            APIException: When an error occurs while fetching the data from the
                remote API. This exception includes the HTTP Response code, an error
                message, and the HTTP body that was received in the request.

        """
        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path("/query/optionalQueryParam")
            .http_method(HttpMethodEnum.GET)
            .query_param(Parameter()
                .key("name")
                .value(name)
                .is_required(True))
            .header_param(Parameter()
                .key("accept")
                .value("application/json"))
            .additional_query_params(_optional_query_parameters),
        ).response(
            ResponseHandler()
            .is_nullify404(True)
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(ServerResponse.from_dictionary),
        ).execute()

    def date(self,
             date):
        """Perform a GET request to /query/date.

        Args:
            date (date): The request query parameter.

        Returns:
            ServerResponse: Response from the API.

        Raises:
            APIException: When an error occurs while fetching the data from the
                remote API. This exception includes the HTTP Response code, an error
                message, and the HTTP body that was received in the request.

        """
        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path("/query/date")
            .http_method(HttpMethodEnum.GET)
            .query_param(Parameter()
                .key("date")
                .value(date)
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

    def unix_date_time_array(self,
                             datetimes):
        """Perform a GET request to /query/unixdatetimearray.

        Args:
            datetimes (List[datetime]): The request query parameter.

        Returns:
            ServerResponse: Response from the API.

        Raises:
            APIException: When an error occurs while fetching the data from the
                remote API. This exception includes the HTTP Response code, an error
                message, and the HTTP body that was received in the request.

        """
        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path("/query/unixdatetimearray")
            .http_method(HttpMethodEnum.GET)
            .query_param(Parameter()
                .key("datetimes")
                .value([APIHelper.when_defined(APIHelper.UnixDateTime,
                    element) for element in datetimes])
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

    def unix_date_time(self,
                       datetime):
        """Perform a GET request to /query/unixdatetime.

        Args:
            datetime (datetime): The request query parameter.

        Returns:
            ServerResponse: Response from the API.

        Raises:
            APIException: When an error occurs while fetching the data from the
                remote API. This exception includes the HTTP Response code, an error
                message, and the HTTP body that was received in the request.

        """
        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path("/query/unixdatetime")
            .http_method(HttpMethodEnum.GET)
            .query_param(Parameter()
                .key("datetime")
                .value(APIHelper.when_defined(APIHelper.UnixDateTime,
                    datetime))
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

    def rfc_1123_date_time(self,
                           datetime):
        """Perform a GET request to /query/rfc1123datetime.

        Args:
            datetime (datetime): The request query parameter.

        Returns:
            ServerResponse: Response from the API.

        Raises:
            APIException: When an error occurs while fetching the data from the
                remote API. This exception includes the HTTP Response code, an error
                message, and the HTTP body that was received in the request.

        """
        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path("/query/rfc1123datetime")
            .http_method(HttpMethodEnum.GET)
            .query_param(Parameter()
                .key("datetime")
                .value(APIHelper.when_defined(APIHelper.HttpDateTime,
                    datetime))
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

    def rfc_1123_date_time_array(self,
                                 datetimes):
        """Perform a GET request to /query/rfc1123datetimearray.

        Args:
            datetimes (List[datetime]): The request query parameter.

        Returns:
            ServerResponse: Response from the API.

        Raises:
            APIException: When an error occurs while fetching the data from the
                remote API. This exception includes the HTTP Response code, an error
                message, and the HTTP body that was received in the request.

        """
        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path("/query/rfc1123datetimearray")
            .http_method(HttpMethodEnum.GET)
            .query_param(Parameter()
                .key("datetimes")
                .value([APIHelper.when_defined(APIHelper.HttpDateTime,
                    element) for element in datetimes])
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

    def rfc_3339_date_time_array(self,
                                 datetimes):
        """Perform a GET request to /query/rfc3339datetimearray.

        Args:
            datetimes (List[datetime]): The request query parameter.

        Returns:
            ServerResponse: Response from the API.

        Raises:
            APIException: When an error occurs while fetching the data from the
                remote API. This exception includes the HTTP Response code, an error
                message, and the HTTP body that was received in the request.

        """
        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path("/query/rfc3339datetimearray")
            .http_method(HttpMethodEnum.GET)
            .query_param(Parameter()
                .key("datetimes")
                .value([APIHelper.when_defined(APIHelper.RFC3339DateTime,
                    element) for element in datetimes])
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

    def rfc_3339_date_time(self,
                           datetime):
        """Perform a GET request to /query/rfc3339datetime.

        Args:
            datetime (datetime): The request query parameter.

        Returns:
            ServerResponse: Response from the API.

        Raises:
            APIException: When an error occurs while fetching the data from the
                remote API. This exception includes the HTTP Response code, an error
                message, and the HTTP body that was received in the request.

        """
        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path("/query/rfc3339datetime")
            .http_method(HttpMethodEnum.GET)
            .query_param(Parameter()
                .key("datetime")
                .value(APIHelper.when_defined(APIHelper.RFC3339DateTime,
                    datetime))
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

    def no_params(self):
        """Perform a GET request to /query/noparams.

        Returns:
            ServerResponse: Response from the API.

        Raises:
            APIException: When an error occurs while fetching the data from the
                remote API. This exception includes the HTTP Response code, an error
                message, and the HTTP body that was received in the request.

        """
        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path("/query/noparams")
            .http_method(HttpMethodEnum.GET)
            .header_param(Parameter()
                .key("accept")
                .value("application/json")),
        ).response(
            ResponseHandler()
            .is_nullify404(True)
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(ServerResponse.from_dictionary),
        ).execute()

    def string_param(self,
                     string):
        """Perform a GET request to /query/stringparam.

        Args:
            string (str): The request query parameter.

        Returns:
            ServerResponse: Response from the API.

        Raises:
            APIException: When an error occurs while fetching the data from the
                remote API. This exception includes the HTTP Response code, an error
                message, and the HTTP body that was received in the request.

        """
        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path("/query/stringparam")
            .http_method(HttpMethodEnum.GET)
            .query_param(Parameter()
                .key("string")
                .value(string)
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

    def url_param(self,
                  url):
        """Perform a GET request to /query/urlparam.

        Args:
            url (str): The request query parameter.

        Returns:
            ServerResponse: Response from the API.

        Raises:
            APIException: When an error occurs while fetching the data from the
                remote API. This exception includes the HTTP Response code, an error
                message, and the HTTP body that was received in the request.

        """
        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path("/query/urlparam")
            .http_method(HttpMethodEnum.GET)
            .query_param(Parameter()
                .key("url")
                .value(url)
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

    def number_array(self,
                     integers):
        """Perform a GET request to /query/numberarray.

        Args:
            integers (List[int]): The request query parameter.

        Returns:
            ServerResponse: Response from the API.

        Raises:
            APIException: When an error occurs while fetching the data from the
                remote API. This exception includes the HTTP Response code, an error
                message, and the HTTP body that was received in the request.

        """
        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path("/query/numberarray")
            .http_method(HttpMethodEnum.GET)
            .query_param(Parameter()
                .key("integers")
                .value(integers)
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

    def string_array(self,
                     strings):
        """Perform a GET request to /query/stringarray.

        Args:
            strings (List[str]): The request query parameter.

        Returns:
            ServerResponse: Response from the API.

        Raises:
            APIException: When an error occurs while fetching the data from the
                remote API. This exception includes the HTTP Response code, an error
                message, and the HTTP body that was received in the request.

        """
        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path("/query/stringarray")
            .http_method(HttpMethodEnum.GET)
            .query_param(Parameter()
                .key("strings")
                .value(strings)
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

    def simple_query(self,
                     boolean,
                     number,
                     string,
                     _optional_query_parameters=None):
        """Perform a GET request to /query.

        Args:
            boolean (bool): The request query parameter.
            number (int): The request query parameter.
            string (str): The request query parameter.
            _optional_query_parameters (Array, optional): Additional optional query
                parameters are supported by this endpoint

        Returns:
            ServerResponse: Response from the API.

        Raises:
            APIException: When an error occurs while fetching the data from the
                remote API. This exception includes the HTTP Response code, an error
                message, and the HTTP body that was received in the request.

        """
        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path("/query")
            .http_method(HttpMethodEnum.GET)
            .query_param(Parameter()
                .key("boolean")
                .value(boolean)
                .is_required(True))
            .query_param(Parameter()
                .key("number")
                .value(number)
                .is_required(True))
            .query_param(Parameter()
                .key("string")
                .value(string)
                .is_required(True))
            .header_param(Parameter()
                .key("accept")
                .value("application/json"))
            .additional_query_params(_optional_query_parameters),
        ).response(
            ResponseHandler()
            .is_nullify404(True)
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(ServerResponse.from_dictionary),
        ).execute()

    def string_enum_array(self,
                          days):
        """Perform a GET request to /query/stringenumarray.

        Args:
            days (List[Days1Enum]): The request query parameter.

        Returns:
            ServerResponse: Response from the API.

        Raises:
            APIException: When an error occurs while fetching the data from the
                remote API. This exception includes the HTTP Response code, an error
                message, and the HTTP body that was received in the request.

        """
        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path("/query/stringenumarray")
            .http_method(HttpMethodEnum.GET)
            .query_param(Parameter()
                .key("days")
                .value(days)
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

    def multiple_params(self,
                        number,
                        precision,
                        string,
                        url):
        """Perform a GET request to /query/multipleparams.

        Args:
            number (int): The request query parameter.
            precision (float): The request query parameter.
            string (str): The request query parameter.
            url (str): The request query parameter.

        Returns:
            ServerResponse: Response from the API.

        Raises:
            APIException: When an error occurs while fetching the data from the
                remote API. This exception includes the HTTP Response code, an error
                message, and the HTTP body that was received in the request.

        """
        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path("/query/multipleparams")
            .http_method(HttpMethodEnum.GET)
            .query_param(Parameter()
                .key("number")
                .value(number)
                .is_required(True))
            .query_param(Parameter()
                .key("precision")
                .value(precision)
                .is_required(True))
            .query_param(Parameter()
                .key("string")
                .value(string)
                .is_required(True))
            .query_param(Parameter()
                .key("url")
                .value(url)
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

    def integer_enum_array(self,
                           suites):
        """Perform a GET request to /query/integerenumarray.

        Args:
            suites (List[SuiteCodeEnum]): The request query parameter.

        Returns:
            ServerResponse: Response from the API.

        Raises:
            APIException: When an error occurs while fetching the data from the
                remote API. This exception includes the HTTP Response code, an error
                message, and the HTTP body that was received in the request.

        """
        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path("/query/integerenumarray")
            .http_method(HttpMethodEnum.GET)
            .query_param(Parameter()
                .key("suites")
                .value(suites)
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

    def send_indexed_complex_type_in_query(self,
                                           complex_type):
        """Perform a POST request to /query/complex/indexed.

        Args:
            complex_type (ComplexType): The request query parameter.

        Returns:
            ServerResponse: Response from the API.

        Raises:
            APIException: When an error occurs while fetching the data from the
                remote API. This exception includes the HTTP Response code, an error
                message, and the HTTP body that was received in the request.

        """
        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path("/query/complex/indexed")
            .http_method(HttpMethodEnum.POST)
            .query_param(Parameter()
                .key("complexType")
                .value(complex_type)
                .is_required(True))
            .query_param(Parameter()
                .key("content")
                .value("SIMPLE"))
            .header_param(Parameter()
                .key("accept")
                .value("application/json")),
        ).response(
            ResponseHandler()
            .is_nullify404(True)
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(ServerResponse.from_dictionary),
        ).execute()

    def send_indexed_list_of_complex_type_in_query(self,
                                                   complex_type):
        """Perform a POST request to /query/complex/indexed.

        Args:
            complex_type (List[ComplexType]): The request query parameter.

        Returns:
            ServerResponse: Response from the API.

        Raises:
            APIException: When an error occurs while fetching the data from the
                remote API. This exception includes the HTTP Response code, an error
                message, and the HTTP body that was received in the request.

        """
        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path("/query/complex/indexed")
            .http_method(HttpMethodEnum.POST)
            .query_param(Parameter()
                .key("complexType")
                .value(complex_type)
                .is_required(True))
            .query_param(Parameter()
                .key("content")
                .value("ARRAY"))
            .header_param(Parameter()
                .key("accept")
                .value("application/json")),
        ).response(
            ResponseHandler()
            .is_nullify404(True)
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(ServerResponse.from_dictionary),
        ).execute()

    def send_indexed_map_of_complex_type_in_query(self,
                                                  complex_type):
        """Perform a POST request to /query/complex/indexed.

        Args:
            complex_type (Dict[str, ComplexType]): The request query parameter.

        Returns:
            ServerResponse: Response from the API.

        Raises:
            APIException: When an error occurs while fetching the data from the
                remote API. This exception includes the HTTP Response code, an error
                message, and the HTTP body that was received in the request.

        """
        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path("/query/complex/indexed")
            .http_method(HttpMethodEnum.POST)
            .query_param(Parameter()
                .key("complexType")
                .value(complex_type)
                .is_required(True))
            .query_param(Parameter()
                .key("content")
                .value("MAP"))
            .header_param(Parameter()
                .key("accept")
                .value("application/json")),
        ).response(
            ResponseHandler()
            .is_nullify404(True)
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(ServerResponse.from_dictionary),
        ).execute()
