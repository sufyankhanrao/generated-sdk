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


class CustomTypesController(BaseController):
    """A Controller to access Endpoints in the testcodesamples API."""

    def __init__(self, config):
        """Initialize CustomTypesController object."""
        super(CustomTypesController, self).__init__(config)

    def multi_dimensional_model_array_required(self,
                                               employee_array,
                                               employee_array_optional=None):
        """Perform a POST request to /CustomTypes/First.

        Args:
            employee_array (List[EmployeeRequired]): The request form
                parameter.
            employee_array_optional (List[EmployeeRequired], optional): The
                request form parameter.

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
            .path("/CustomTypes/First")
            .http_method(HttpMethodEnum.POST)
            .form_param(Parameter()
                        .key("employeeArray")
                        .value(employee_array)
                        .is_required(True))
            .form_param(Parameter()
                        .key("employeeArrayOptional")
                        .value(employee_array_optional))
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

    def multi_dimensional_model_array_optional(self,
                                               employee_array=None,
                                               employee_array_optional=None):
        """Perform a POST request to /CustomTypes/Second.

        Args:
            employee_array (List[EmployeeRequired], optional): The request
                form parameter.
            employee_array_optional (List[EmployeeOptional], optional): The
                request form parameter.

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
            .path("/CustomTypes/Second")
            .http_method(HttpMethodEnum.POST)
            .form_param(Parameter()
                        .key("employeeArray")
                        .value(employee_array))
            .form_param(Parameter()
                        .key("employeeArrayOptional")
                        .value(employee_array_optional))
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

    def custom_type_map_of_array_and_array_of_map_required(self,
                                                           employee_array_of_map,
                                                           employee_map_of_array):
        """Perform a POST request to /CustomTypes/Third.

        Args:
            employee_array_of_map (EmployeeRequired): The request form
                parameter.
            employee_map_of_array (List[bool]): The request form parameter.

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
            .path("/CustomTypes/Third")
            .http_method(HttpMethodEnum.POST)
            .form_param(Parameter()
                        .key("employeeArrayOfMap")
                        .value(employee_array_of_map)
                        .is_required(True))
            .form_param(Parameter()
                        .key("employeeMapOfArray")
                        .value(employee_map_of_array)
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

    def custom_type_map_of_array_and_array_of_map_optional(self,
                                                           employee_array_of_map=None,
                                                           employee_map_of_array=None):
        """Perform a POST request to /CustomTypes/Fourth.

        Args:
            employee_array_of_map (EmployeeRequired, optional): The request
                form parameter.
            employee_map_of_array (List[bool], optional): The request form
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
            .path("/CustomTypes/Fourth")
            .http_method(HttpMethodEnum.POST)
            .form_param(Parameter()
                        .key("employeeArrayOfMap")
                        .value(employee_array_of_map))
            .form_param(Parameter()
                        .key("employeeMapOfArray")
                        .value(employee_map_of_array))
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

    def send_model_in_form_required(self,
                                    model,
                                    model_optional=None):
        """Perform a POST request to /CustomTypes/Fifth.

        Args:
            model (Dict[str, EmployeeRequired]): The request form parameter.
            model_optional (Dict[str, EmployeeRequired], optional): The
                request form parameter.

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
            .path("/CustomTypes/Fifth")
            .http_method(HttpMethodEnum.POST)
            .form_param(Parameter()
                        .key("model")
                        .value(model)
                        .is_required(True))
            .form_param(Parameter()
                        .key("modelOptional")
                        .value(model_optional))
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

    def send_model_in_form_optional(self,
                                    model,
                                    model_optional=None):
        """Perform a POST request to /CustomTypes/Sixth.

        Args:
            model (Dict[str, EmployeeOptional]): The request form parameter.
            model_optional (Dict[str, EmployeeOptional], optional): The
                request form parameter.

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
            .path("/CustomTypes/Sixth")
            .http_method(HttpMethodEnum.POST)
            .form_param(Parameter()
                        .key("model")
                        .value(model)
                        .is_required(True))
            .form_param(Parameter()
                        .key("modelOptional")
                        .value(model_optional))
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
