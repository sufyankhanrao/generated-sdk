"""testcodesamples.

This file was automatically generated for Stamplay by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

from apimatic_core.request_builder import RequestBuilder
from apimatic_core.response_handler import ResponseHandler
from apimatic_core.types.parameter import Parameter

from testcodesamples.api_helper import APIHelper
from testcodesamples.configuration import Server
from testcodesamples.controllers.base_controller import (
    BaseController,
)
from testcodesamples.http.http_method_enum import (
    HttpMethodEnum,
)
from testcodesamples.models.server_response import (
    ServerResponse,
)


class NativeTypesController(BaseController):
    """A Controller to access Endpoints in the testcodesamples API."""

    def __init__(self, config):
        """Initialize NativeTypesController object."""
        super(NativeTypesController, self).__init__(config)

    def send_string_boolean_object_dynamic_required(self,
                                                    string_var,
                                                    boolean_var,
                                                    object_var,
                                                    dynamic_var):
        """Perform a POST request to /NativeTypes/First.

        Args:
            string_var (str): The request form parameter.
            boolean_var (bool): The request form parameter.
            object_var (Any): The request form parameter.
            dynamic_var (Any): The request form parameter.

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
            .path("/NativeTypes/First")
            .http_method(HttpMethodEnum.POST)
            .form_param(Parameter()
                        .key("stringVar")
                        .value(string_var)
                        .is_required(True))
            .form_param(Parameter()
                        .key("booleanVar")
                        .value(boolean_var)
                        .is_required(True))
            .form_param(Parameter()
                        .key("objectVar")
                        .value(object_var)
                        .is_required(True))
            .form_param(Parameter()
                        .key("dynamicVar")
                        .value(dynamic_var)
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

    def send_string_boolean_object_dynamic_optional(self,
                                                    string_var=None,
                                                    boolean_var=None,
                                                    object_var=None,
                                                    dynamic_var=None):
        """Perform a POST request to /NativeTypes/Second.

        Args:
            string_var (str, optional): The request form parameter.
            boolean_var (bool, optional): The request form parameter.
            object_var (Any, optional): The request form parameter.
            dynamic_var (Any, optional): The request form parameter.

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
            .path("/NativeTypes/Second")
            .http_method(HttpMethodEnum.POST)
            .form_param(Parameter()
                        .key("stringVar")
                        .value(string_var))
            .form_param(Parameter()
                        .key("booleanVar")
                        .value(boolean_var))
            .form_param(Parameter()
                        .key("objectVar")
                        .value(object_var))
            .form_param(Parameter()
                        .key("dynamicVar")
                        .value(dynamic_var))
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

    def send_date_and_time_required(self,
                                    unix_date_time_var,
                                    rfc_1123_date_time_var,
                                    rfc_3339_date_time,
                                    date_var):
        """Perform a POST request to /NativeTypes/Third.

        Args:
            unix_date_time_var (datetime): The request form parameter.
            rfc_1123_date_time_var (datetime): The request form parameter.
            rfc_3339_date_time (datetime): The request form parameter.
            date_var (date): The request form parameter.

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
            .path("/NativeTypes/Third")
            .http_method(HttpMethodEnum.POST)
            .form_param(Parameter()
                        .key("unixDateTimeVar")
                        .value(APIHelper.when_defined(APIHelper.UnixDateTime,
                            unix_date_time_var))
                        .is_required(True))
            .form_param(Parameter()
                        .key("rfc1123DateTimeVar")
                        .value(APIHelper.when_defined(APIHelper.HttpDateTime,
                            rfc_1123_date_time_var))
                        .is_required(True))
            .form_param(Parameter()
                        .key("rfc3339DateTime")
                        .value(APIHelper.when_defined(APIHelper.RFC3339DateTime,
                            rfc_3339_date_time))
                        .is_required(True))
            .form_param(Parameter()
                        .key("dateVar")
                        .value(date_var)
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

    def send_date_and_time_optional(self,
                                    unix_date_time_var=None,
                                    rfc_1123_date_time_var=None,
                                    rfc_3339_date_time=None,
                                    date_var=None):
        """Perform a POST request to /NativeTypes/Fourth.

        Args:
            unix_date_time_var (datetime, optional): The request form
                parameter.
            rfc_1123_date_time_var (datetime, optional): The request form
                parameter.
            rfc_3339_date_time (datetime, optional): The request form
                parameter.
            date_var (date, optional): The request form parameter.

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
            .path("/NativeTypes/Fourth")
            .http_method(HttpMethodEnum.POST)
            .form_param(Parameter()
                        .key("unixDateTimeVar")
                        .value(APIHelper.when_defined(APIHelper.UnixDateTime,
                            unix_date_time_var)))
            .form_param(Parameter()
                        .key("rfc1123DateTimeVar")
                        .value(APIHelper.when_defined(APIHelper.HttpDateTime,
                            rfc_1123_date_time_var)))
            .form_param(Parameter()
                        .key("rfc3339DateTime")
                        .value(APIHelper.when_defined(APIHelper.RFC3339DateTime,
                            rfc_3339_date_time)))
            .form_param(Parameter()
                        .key("dateVar")
                        .value(date_var))
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

    def multi_dimensional_native_array_required(self,
                                                boolean_array):
        """Perform a POST request to /NativeTypes/Seventh.

        Args:
            boolean_array (List[bool]): The request form parameter.

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
            .path("/NativeTypes/Seventh")
            .http_method(HttpMethodEnum.POST)
            .form_param(Parameter()
                        .key("booleanArray")
                        .value(boolean_array)
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

    def multi_dimensional_native_array_optional(self,
                                                boolean_array=None):
        """Perform a POST request to /NativeTypes/Eighth.

        Args:
            boolean_array (List[bool], optional): The request form parameter.

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
            .path("/NativeTypes/Eighth")
            .http_method(HttpMethodEnum.POST)
            .form_param(Parameter()
                        .key("booleanArray")
                        .value(boolean_array))
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

    def native_map_of_array_and_array_of_map_required(self,
                                                      boolean_array_of_map,
                                                      boolean_map_of_array):
        """Perform a POST request to /NativeTypes/Nineth.

        Args:
            boolean_array_of_map (bool): The request form parameter.
            boolean_map_of_array (List[bool]): The request form parameter.

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
            .path("/NativeTypes/Nineth")
            .http_method(HttpMethodEnum.POST)
            .form_param(Parameter()
                        .key("booleanArrayOfMap")
                        .value(boolean_array_of_map)
                        .is_required(True))
            .form_param(Parameter()
                        .key("booleanMapOfArray")
                        .value(boolean_map_of_array)
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

    def native_map_of_array_and_array_of_map_optional(self,
                                                      boolean_array_of_map=None,
                                                      boolean_map_of_array=None):
        """Perform a POST request to /NativeTypes/Tenth.

        Args:
            boolean_array_of_map (bool, optional): The request form parameter.
            boolean_map_of_array (List[bool], optional): The request form
                parameter.

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
            .path("/NativeTypes/Tenth")
            .http_method(HttpMethodEnum.POST)
            .form_param(Parameter()
                        .key("booleanArrayOfMap")
                        .value(boolean_array_of_map))
            .form_param(Parameter()
                        .key("booleanMapOfArray")
                        .value(boolean_map_of_array))
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
