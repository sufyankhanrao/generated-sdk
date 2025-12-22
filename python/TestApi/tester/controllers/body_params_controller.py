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
from tester.exceptions.rfc_7807_error_response_error_exception import (
    RFC7807ErrorResponseErrorException,
)
from tester.http.http_method_enum import HttpMethodEnum
from tester.models.server_response import ServerResponse


class BodyParamsController(BaseController):
    """A Controller to access Endpoints in the tester API."""

    def __init__(self, config):
        """Initialize BodyParamsController object."""
        super(BodyParamsController, self).__init__(config)

    def send_delete_plain_text(self,
                               text_string):
        """Perform a DELETE request to /body/deletePlainTextBody.

        Args:
            text_string (str): The request body parameter.

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
            .path("/body/deletePlainTextBody")
            .http_method(HttpMethodEnum.DELETE)
            .body_param(Parameter()
                .value(text_string)
                .is_required(True))
            .header_param(Parameter()
                .key("content-type")
                .value("text/plain; charset=utf-8"))
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

    def send_delete_body(self,
                         body):
        """Perform a DELETE request to /body/deleteBody.

        Args:
            body (DeleteBody): The request body parameter.

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
            .path("/body/deleteBody")
            .http_method(HttpMethodEnum.DELETE)
            .header_param(Parameter()
                .key("Content-Type")
                .value("application/json"))
            .body_param(Parameter()
                .value(body)
                .is_required(True))
            .header_param(Parameter()
                .key("accept")
                .value("application/json"))
            .body_serializer(APIHelper.json_serialize),
        ).response(
            ResponseHandler()
            .is_nullify404(True)
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(ServerResponse.from_dictionary)
            .is_api_response(True),
        ).execute()

    def send_date_array(self,
                        dates):
        """Perform a POST request to /body/date.

        Args:
            dates (List[date]): The request body parameter.

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
            .path("/body/date")
            .http_method(HttpMethodEnum.POST)
            .header_param(Parameter()
                .key("Content-Type")
                .value("application/json"))
            .query_param(Parameter()
                .key("array")
                .value(True))
            .body_param(Parameter()
                .value(dates)
                .is_required(True))
            .header_param(Parameter()
                .key("accept")
                .value("application/json"))
            .body_serializer(APIHelper.json_serialize),
        ).response(
            ResponseHandler()
            .is_nullify404(True)
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(ServerResponse.from_dictionary)
            .is_api_response(True),
        ).execute()

    def send_date(self,
                  date):
        """Perform a POST request to /body/date.

        Args:
            date (date): The request body parameter.

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
            .path("/body/date")
            .http_method(HttpMethodEnum.POST)
            .body_param(Parameter()
                .value(date)
                .is_required(True))
            .header_param(Parameter()
                .key("content-type")
                .value("text/plain; charset=utf-8"))
            .header_param(Parameter()
                .key("accept")
                .value("application/json"))
            .body_serializer(str),
        ).response(
            ResponseHandler()
            .is_nullify404(True)
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(ServerResponse.from_dictionary)
            .is_api_response(True),
        ).execute()

    def send_unix_date_time(self,
                            datetime):
        """Perform a POST request to /body/unixdatetime.

        Args:
            datetime (datetime): The request body parameter.

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
            .path("/body/unixdatetime")
            .http_method(HttpMethodEnum.POST)
            .body_param(Parameter()
                .value(APIHelper.when_defined(APIHelper.UnixDateTime,
                    datetime))
                .is_required(True))
            .header_param(Parameter()
                .key("content-type")
                .value("text/plain; charset=utf-8"))
            .header_param(Parameter()
                .key("accept")
                .value("application/json"))
            .body_serializer(str),
        ).response(
            ResponseHandler()
            .is_nullify404(True)
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(ServerResponse.from_dictionary)
            .is_api_response(True),
        ).execute()

    def send_rfc_1123_date_time(self,
                                datetime):
        """Perform a POST request to /body/rfc1123datetime.

        Args:
            datetime (datetime): The request body parameter.

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
            .path("/body/rfc1123datetime")
            .http_method(HttpMethodEnum.POST)
            .body_param(Parameter()
                .value(APIHelper.when_defined(APIHelper.HttpDateTime,
                    datetime))
                .is_required(True))
            .header_param(Parameter()
                .key("content-type")
                .value("text/plain; charset=utf-8"))
            .header_param(Parameter()
                .key("accept")
                .value("application/json"))
            .body_serializer(str),
        ).response(
            ResponseHandler()
            .is_nullify404(True)
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(ServerResponse.from_dictionary)
            .is_api_response(True),
        ).execute()

    def send_rfc_3339_date_time(self,
                                datetime):
        """Perform a POST request to /body/rfc3339datetime.

        Args:
            datetime (datetime): The request body parameter.

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
            .path("/body/rfc3339datetime")
            .http_method(HttpMethodEnum.POST)
            .body_param(Parameter()
                .value(APIHelper.when_defined(APIHelper.RFC3339DateTime,
                    datetime))
                .is_required(True))
            .header_param(Parameter()
                .key("content-type")
                .value("text/plain; charset=utf-8"))
            .header_param(Parameter()
                .key("accept")
                .value("application/json"))
            .body_serializer(str),
        ).response(
            ResponseHandler()
            .is_nullify404(True)
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(ServerResponse.from_dictionary)
            .is_api_response(True),
        ).execute()

    def send_unix_date_time_array(self,
                                  datetimes):
        """Perform a POST request to /body/unixdatetime.

        Args:
            datetimes (List[datetime]): The request body parameter.

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
            .path("/body/unixdatetime")
            .http_method(HttpMethodEnum.POST)
            .query_param(Parameter()
                .key("array")
                .value(True))
            .body_param(Parameter()
                .value([APIHelper.when_defined(APIHelper.UnixDateTime,
                    element) for element in datetimes])
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
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(ServerResponse.from_dictionary)
            .is_api_response(True),
        ).execute()

    def send_rfc_1123_date_time_array(self,
                                      datetimes):
        """Perform a POST request to /body/rfc1123datetime.

        Args:
            datetimes (List[datetime]): The request body parameter.

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
            .path("/body/rfc1123datetime")
            .http_method(HttpMethodEnum.POST)
            .header_param(Parameter()
                .key("Content-Type")
                .value("application/json"))
            .query_param(Parameter()
                .key("array")
                .value(True))
            .body_param(Parameter()
                .value([APIHelper.when_defined(APIHelper.HttpDateTime,
                    element) for element in datetimes])
                .is_required(True))
            .header_param(Parameter()
                .key("accept")
                .value("application/json"))
            .body_serializer(APIHelper.json_serialize),
        ).response(
            ResponseHandler()
            .is_nullify404(True)
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(ServerResponse.from_dictionary)
            .is_api_response(True),
        ).execute()

    def send_rfc_3339_date_time_array(self,
                                      datetimes):
        """Perform a POST request to /body/rfc3339datetime.

        Args:
            datetimes (List[datetime]): The request body parameter.

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
            .path("/body/rfc3339datetime")
            .http_method(HttpMethodEnum.POST)
            .query_param(Parameter()
                .key("array")
                .value(True))
            .body_param(Parameter()
                .value([APIHelper.when_defined(APIHelper.RFC3339DateTime,
                    element) for element in datetimes])
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
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(ServerResponse.from_dictionary)
            .is_api_response(True),
        ).execute()

    def send_string_array(self,
                          sarray):
        """Perform a POST request to /body/string.

        sends a string body param

        Args:
            sarray (List[str]): The request body parameter.

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
            .path("/body/string")
            .http_method(HttpMethodEnum.POST)
            .header_param(Parameter()
                .key("Content-Type")
                .value("application/json"))
            .query_param(Parameter()
                .key("array")
                .value(True))
            .body_param(Parameter()
                .value(sarray)
                .is_required(True))
            .header_param(Parameter()
                .key("accept")
                .value("application/json"))
            .body_serializer(APIHelper.json_serialize),
        ).response(
            ResponseHandler()
            .is_nullify404(True)
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(ServerResponse.from_dictionary)
            .is_api_response(True),
        ).execute()

    def update_string(self,
                      value):
        """Perform a PUT request to /body/updateString.

        Args:
            value (str): The request body parameter.

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
            .path("/body/updateString")
            .http_method(HttpMethodEnum.PUT)
            .body_param(Parameter()
                .value(value)
                .is_required(True))
            .header_param(Parameter()
                .key("content-type")
                .value("text/plain; charset=utf-8"))
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

    def send_integer_array(self,
                           integers):
        """Perform a POST request to /body/number.

        Args:
            integers (List[int]): The request body parameter.

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
            .path("/body/number")
            .http_method(HttpMethodEnum.POST)
            .header_param(Parameter()
                .key("Content-Type")
                .value("application/json"))
            .query_param(Parameter()
                .key("array")
                .value(True))
            .body_param(Parameter()
                .value(integers)
                .is_required(True))
            .header_param(Parameter()
                .key("accept")
                .value("application/json"))
            .body_serializer(APIHelper.json_serialize),
        ).response(
            ResponseHandler()
            .is_nullify404(True)
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(ServerResponse.from_dictionary)
            .is_api_response(True),
        ).execute()

    def wrap_body_in_object(self,
                            field,
                            name):
        """Perform a POST request to /body/wrapParamInObject.

        Args:
            field (str): The request body parameter.
            name (str): The request body parameter.

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
            .path("/body/wrapParamInObject")
            .http_method(HttpMethodEnum.POST)
            .header_param(Parameter()
                .key("Content-Type")
                .value("application/json"))
            .body_param(Parameter()
                .key("field")
                .value(field)
                .is_required(True))
            .body_param(Parameter()
                .key("name")
                .value(name)
                .is_required(True))
            .header_param(Parameter()
                .key("accept")
                .value("application/json"))
            .body_serializer(APIHelper.json_serialize_wrapped_params),
        ).response(
            ResponseHandler()
            .is_nullify404(True)
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(ServerResponse.from_dictionary)
            .is_api_response(True),
        ).execute()

    def additional_model_parameters(self,
                                    model):
        """Perform a POST request to /body/additionalModelProperties.

        Args:
            model (AdditionalModelParameters): The request body parameter.

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
            .path("/body/additionalModelProperties")
            .http_method(HttpMethodEnum.POST)
            .header_param(Parameter()
                .key("Content-Type")
                .value("application/json"))
            .body_param(Parameter()
                .value(model)
                .is_required(True))
            .header_param(Parameter()
                .key("accept")
                .value("application/json"))
            .body_serializer(APIHelper.json_serialize),
        ).response(
            ResponseHandler()
            .is_nullify404(True)
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(ServerResponse.from_dictionary)
            .is_api_response(True),
        ).execute()

    def validate_required_parameter(self,
                                    model,
                                    option=None):
        """Perform a POST request to /body/validateRequiredParam.

        Args:
            model (Validate): The request body parameter.
            option (str, optional): The request query parameter.

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
            .path("/body/validateRequiredParam")
            .http_method(HttpMethodEnum.POST)
            .header_param(Parameter()
                .key("Content-Type")
                .value("application/json"))
            .body_param(Parameter()
                .value(model)
                .is_required(True))
            .query_param(Parameter()
                .key("option")
                .value(option))
            .header_param(Parameter()
                .key("accept")
                .value("application/json"))
            .body_serializer(APIHelper.json_serialize),
        ).response(
            ResponseHandler()
            .is_nullify404(True)
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(ServerResponse.from_dictionary)
            .is_api_response(True),
        ).execute()

    def additional_model_parameters_1(self,
                                      model):
        """Perform a POST request to /body/additionalModelProperties.

        Args:
            model (AdditionalModelParameters): The request body parameter.

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
            .path("/body/additionalModelProperties")
            .http_method(HttpMethodEnum.POST)
            .header_param(Parameter()
                .key("Content-Type")
                .value("application/json"))
            .body_param(Parameter()
                .value(model)
                .is_required(True))
            .header_param(Parameter()
                .key("accept")
                .value("application/json"))
            .body_serializer(APIHelper.json_serialize),
        ).response(
            ResponseHandler()
            .is_nullify404(True)
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(ServerResponse.from_dictionary)
            .is_api_response(True),
        ).execute()

    def send_model(self,
                   model):
        """Perform a POST request to /body/model.

        Args:
            model (Employee): The request body parameter.

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
            .path("/body/model")
            .http_method(HttpMethodEnum.POST)
            .header_param(Parameter()
                .key("Content-Type")
                .value("application/json"))
            .body_param(Parameter()
                .value(model)
                .is_required(True))
            .header_param(Parameter()
                .key("accept")
                .value("application/json"))
            .body_serializer(APIHelper.json_serialize),
        ).response(
            ResponseHandler()
            .is_nullify404(True)
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(ServerResponse.from_dictionary)
            .is_api_response(True),
        ).execute()

    def send_model_array(self,
                         models):
        """Perform a POST request to /body/model.

        Args:
            models (List[Employee]): The request body parameter.

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
            .path("/body/model")
            .http_method(HttpMethodEnum.POST)
            .header_param(Parameter()
                .key("Content-Type")
                .value("application/json"))
            .query_param(Parameter()
                .key("array")
                .value(True))
            .body_param(Parameter()
                .value(models)
                .is_required(True))
            .header_param(Parameter()
                .key("accept")
                .value("application/json"))
            .body_serializer(APIHelper.json_serialize),
        ).response(
            ResponseHandler()
            .is_nullify404(True)
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(ServerResponse.from_dictionary)
            .is_api_response(True),
        ).execute()

    def send_model_map(self,
                       models):
        """Perform a POST request to /body/model.

        Args:
            models (Dict[str, Employee]): The request body parameter.

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
            .path("/body/model")
            .http_method(HttpMethodEnum.POST)
            .header_param(Parameter()
                .key("Content-Type")
                .value("application/json"))
            .query_param(Parameter()
                .key("map")
                .value(True))
            .body_param(Parameter()
                .value(models)
                .is_required(True))
            .header_param(Parameter()
                .key("accept")
                .value("application/json"))
            .body_serializer(APIHelper.json_serialize),
        ).response(
            ResponseHandler()
            .is_nullify404(True)
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(ServerResponse.from_dictionary)
            .is_api_response(True),
        ).execute()

    def send_dynamic(self,
                     dynamic):
        """Perform a POST request to /body/dynamic.

        Args:
            dynamic (Any): The request body parameter.

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
            .path("/body/dynamic")
            .http_method(HttpMethodEnum.POST)
            .header_param(Parameter()
                .key("Content-Type")
                .value("application/json"))
            .body_param(Parameter()
                .value(dynamic)
                .is_required(True))
            .header_param(Parameter()
                .key("accept")
                .value("application/json"))
            .body_serializer(APIHelper.json_serialize),
        ).response(
            ResponseHandler()
            .is_nullify404(True)
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(ServerResponse.from_dictionary)
            .is_api_response(True),
        ).execute()

    def send_string(self,
                    value):
        """Perform a POST request to /body/string.

        Args:
            value (str): The request body parameter.

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
            .path("/body/string")
            .http_method(HttpMethodEnum.POST)
            .body_param(Parameter()
                .value(value)
                .is_required(True))
            .header_param(Parameter()
                .key("content-type")
                .value("text/plain; charset=utf-8"))
            .header_param(Parameter()
                .key("accept")
                .value("application/json")),
        ).response(
            ResponseHandler()
            .is_nullify404(True)
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(ServerResponse.from_dictionary)
            .is_api_response(True)
            .local_error("400",
                "The request was malformed.\nIf this update is a 'report lost' but th"
                "e user does not have a known address with a known state, the title o"
                "f the error will be 'User record missing address.''",
                RFC7807ErrorResponseErrorException),
        ).execute()

    def send_string_enum_array(self,
                               days):
        """Perform a POST request to /body/stringenum.

        Args:
            days (List[Days1Enum]): The request body parameter.

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
            .path("/body/stringenum")
            .http_method(HttpMethodEnum.POST)
            .header_param(Parameter()
                .key("Content-Type")
                .value("application/json"))
            .query_param(Parameter()
                .key("array")
                .value(True))
            .body_param(Parameter()
                .value(days)
                .is_required(True))
            .header_param(Parameter()
                .key("accept")
                .value("application/json"))
            .body_serializer(APIHelper.json_serialize),
        ).response(
            ResponseHandler()
            .is_nullify404(True)
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(ServerResponse.from_dictionary)
            .is_api_response(True),
        ).execute()

    def send_integer_enum_array(self,
                                suites):
        """Perform a POST request to /body/integerenum.

        Args:
            suites (List[SuiteCodeEnum]): The request body parameter.

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
            .path("/body/integerenum")
            .http_method(HttpMethodEnum.POST)
            .header_param(Parameter()
                .key("Content-Type")
                .value("application/json"))
            .query_param(Parameter()
                .key("array")
                .value(True))
            .body_param(Parameter()
                .value(suites)
                .is_required(True))
            .header_param(Parameter()
                .key("accept")
                .value("application/json"))
            .body_serializer(APIHelper.json_serialize),
        ).response(
            ResponseHandler()
            .is_nullify404(True)
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(ServerResponse.from_dictionary)
            .is_api_response(True),
        ).execute()

    def update_model(self,
                     model):
        """Perform a PUT request to /body/updateModel.

        Args:
            model (Employee): The request body parameter.

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
            .path("/body/updateModel")
            .http_method(HttpMethodEnum.PUT)
            .header_param(Parameter()
                .key("Content-Type")
                .value("application/json"))
            .body_param(Parameter()
                .value(model)
                .is_required(True))
            .header_param(Parameter()
                .key("accept")
                .value("application/json"))
            .body_serializer(APIHelper.json_serialize),
        ).response(
            ResponseHandler()
            .is_nullify404(True)
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(ServerResponse.from_dictionary)
            .is_api_response(True),
        ).execute()

    def send_delete_body_with_model(self,
                                    model):
        """Perform a DELETE request to /body/deleteBody1.

        Args:
            model (Employee): The request body parameter.

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
            .path("/body/deleteBody1")
            .http_method(HttpMethodEnum.DELETE)
            .header_param(Parameter()
                .key("Content-Type")
                .value("application/json"))
            .body_param(Parameter()
                .value(model)
                .is_required(True))
            .header_param(Parameter()
                .key("accept")
                .value("application/json"))
            .body_serializer(APIHelper.json_serialize),
        ).response(
            ResponseHandler()
            .is_nullify404(True)
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(ServerResponse.from_dictionary)
            .is_api_response(True),
        ).execute()

    def send_delete_body_with_model_array(self,
                                          models):
        """Perform a DELETE request to /body/deleteBody1.

        Args:
            models (List[Employee]): The request body parameter.

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
            .path("/body/deleteBody1")
            .http_method(HttpMethodEnum.DELETE)
            .header_param(Parameter()
                .key("Content-Type")
                .value("application/json"))
            .query_param(Parameter()
                .key("array")
                .value(True))
            .body_param(Parameter()
                .value(models)
                .is_required(True))
            .header_param(Parameter()
                .key("accept")
                .value("application/json"))
            .body_serializer(APIHelper.json_serialize),
        ).response(
            ResponseHandler()
            .is_nullify404(True)
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(ServerResponse.from_dictionary)
            .is_api_response(True),
        ).execute()

    def update_model_array(self,
                           models):
        """Perform a PUT request to /body/updateModel.

        Args:
            models (List[Employee]): The request body parameter.

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
            .path("/body/updateModel")
            .http_method(HttpMethodEnum.PUT)
            .header_param(Parameter()
                .key("Content-Type")
                .value("application/json"))
            .query_param(Parameter()
                .key("array")
                .value(True))
            .body_param(Parameter()
                .value(models)
                .is_required(True))
            .header_param(Parameter()
                .key("accept")
                .value("application/json"))
            .body_serializer(APIHelper.json_serialize),
        ).response(
            ResponseHandler()
            .is_nullify404(True)
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(ServerResponse.from_dictionary)
            .is_api_response(True),
        ).execute()

    def update_string_1(self,
                        value):
        """Perform a PUT request to /body/updateString.

        Args:
            value (str): The request body parameter.

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
            .path("/body/updateString")
            .http_method(HttpMethodEnum.PUT)
            .body_param(Parameter()
                .value(value)
                .is_required(True))
            .header_param(Parameter()
                .key("content-type")
                .value("text/plain; charset=utf-8"))
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

    def update_string_array(self,
                            strings):
        """Perform a PUT request to /body/updateString.

        Args:
            strings (List[str]): The request body parameter.

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
            .path("/body/updateString")
            .http_method(HttpMethodEnum.PUT)
            .header_param(Parameter()
                .key("Content-Type")
                .value("application/json"))
            .query_param(Parameter()
                .key("array")
                .value(True))
            .body_param(Parameter()
                .value(strings)
                .is_required(True))
            .header_param(Parameter()
                .key("accept")
                .value("application/json"))
            .body_serializer(APIHelper.json_serialize),
        ).response(
            ResponseHandler()
            .is_nullify404(True)
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(ServerResponse.from_dictionary)
            .is_api_response(True),
        ).execute()

    def send_string_with_new_line(self,
                                  body):
        """Perform a POST request to /body/stringEncoding.

        Args:
            body (TestNstringEncoding): The request body parameter.

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
            .path("/body/stringEncoding")
            .http_method(HttpMethodEnum.POST)
            .header_param(Parameter()
                .key("Content-Type")
                .value("application/json"))
            .body_param(Parameter()
                .value(body)
                .is_required(True))
            .header_param(Parameter()
                .key("accept")
                .value("application/json"))
            .body_serializer(APIHelper.json_serialize),
        ).response(
            ResponseHandler()
            .is_nullify404(True)
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(ServerResponse.from_dictionary)
            .is_api_response(True),
        ).execute()

    def send_string_with_r(self,
                           body):
        """Perform a POST request to /body/stringEncoding.

        Args:
            body (TestRstringEncoding): The request body parameter.

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
            .path("/body/stringEncoding")
            .http_method(HttpMethodEnum.POST)
            .header_param(Parameter()
                .key("Content-Type")
                .value("application/json"))
            .body_param(Parameter()
                .value(body)
                .is_required(True))
            .header_param(Parameter()
                .key("accept")
                .value("application/json"))
            .body_serializer(APIHelper.json_serialize),
        ).response(
            ResponseHandler()
            .is_nullify404(True)
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(ServerResponse.from_dictionary)
            .is_api_response(True),
        ).execute()

    def send_string_in_body_with_r_n(self,
                                     body):
        """Perform a POST request to /body/stringEncoding.

        Args:
            body (TestRNstringEncoding): The request body parameter.

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
            .path("/body/stringEncoding")
            .http_method(HttpMethodEnum.POST)
            .header_param(Parameter()
                .key("Content-Type")
                .value("application/json"))
            .body_param(Parameter()
                .value(body)
                .is_required(True))
            .header_param(Parameter()
                .key("accept")
                .value("application/json"))
            .body_serializer(APIHelper.json_serialize),
        ).response(
            ResponseHandler()
            .is_nullify404(True)
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(ServerResponse.from_dictionary)
            .is_api_response(True),
        ).execute()

    def send_optional_unix_date_time_in_body(self,
                                             date_time=None):
        """Perform a POST request to /body/optionalUnixTimeStamp.

        Args:
            date_time (datetime, optional): The request body parameter.

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
            .path("/body/optionalUnixTimeStamp")
            .http_method(HttpMethodEnum.POST)
            .body_param(Parameter()
                .value(APIHelper.when_defined(APIHelper.UnixDateTime,
                    date_time)))
            .header_param(Parameter()
                .key("content-type")
                .value("text/plain; charset=utf-8"))
            .header_param(Parameter()
                .key("accept")
                .value("application/json"))
            .body_serializer(str),
        ).response(
            ResponseHandler()
            .is_nullify404(True)
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(ServerResponse.from_dictionary)
            .is_api_response(True),
        ).execute()

    def send_optional_rfc_1123_in_body(self,
                                       body):
        """Perform a POST request to /body/optionlRfc1123.

        Args:
            body (datetime): The request body parameter.

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
            .path("/body/optionlRfc1123")
            .http_method(HttpMethodEnum.POST)
            .body_param(Parameter()
                .value(APIHelper.when_defined(APIHelper.HttpDateTime,
                    body))
                .is_required(True))
            .header_param(Parameter()
                .key("content-type")
                .value("text/plain; charset=utf-8"))
            .header_param(Parameter()
                .key("accept")
                .value("application/json"))
            .body_serializer(str),
        ).response(
            ResponseHandler()
            .is_nullify404(True)
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(ServerResponse.from_dictionary)
            .is_api_response(True),
        ).execute()

    def send_datetime_optional_in_endpoint(self,
                                           body=None):
        """Perform a POST request to /body/optionalDateTime.

        Args:
            body (datetime, optional): The request body parameter.

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
            .path("/body/optionalDateTime")
            .http_method(HttpMethodEnum.POST)
            .body_param(Parameter()
                .value(APIHelper.when_defined(APIHelper.RFC3339DateTime,
                    body)))
            .header_param(Parameter()
                .key("content-type")
                .value("text/plain; charset=utf-8"))
            .header_param(Parameter()
                .key("accept")
                .value("application/json"))
            .body_serializer(str),
        ).response(
            ResponseHandler()
            .is_nullify404(True)
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(ServerResponse.from_dictionary)
            .is_api_response(True),
        ).execute()

    def send_optional_unix_time_stamp_in_model_body(self,
                                                    date_time):
        """Perform a POST request to /body/optionalUnixDateTimeInModel.

        Args:
            date_time (UnixDateTime): The request body parameter.

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
            .path("/body/optionalUnixDateTimeInModel")
            .http_method(HttpMethodEnum.POST)
            .header_param(Parameter()
                .key("Content-Type")
                .value("application/json"))
            .body_param(Parameter()
                .value(date_time)
                .is_required(True))
            .header_param(Parameter()
                .key("accept")
                .value("application/json"))
            .body_serializer(APIHelper.json_serialize),
        ).response(
            ResponseHandler()
            .is_nullify404(True)
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(ServerResponse.from_dictionary)
            .is_api_response(True),
        ).execute()

    def send_optional_unix_time_stamp_in_nested_model_body(self,
                                                           date_time):
        """Perform a POST request to /body/optionalUnixTimeStampInNestedModel.

        Args:
            date_time (SendUnixDateTime): The request body parameter.

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
            .path("/body/optionalUnixTimeStampInNestedModel")
            .http_method(HttpMethodEnum.POST)
            .header_param(Parameter()
                .key("Content-Type")
                .value("application/json"))
            .body_param(Parameter()
                .value(date_time)
                .is_required(True))
            .header_param(Parameter()
                .key("accept")
                .value("application/json"))
            .body_serializer(APIHelper.json_serialize),
        ).response(
            ResponseHandler()
            .is_nullify404(True)
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(ServerResponse.from_dictionary)
            .is_api_response(True),
        ).execute()

    def send_rfc_1123_date_time_in_nested_model(self,
                                                body):
        """Perform a POST request to /body/rfc1123InNestedModel.

        Args:
            body (SendRfc1123DateTime): The request body parameter.

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
            .path("/body/rfc1123InNestedModel")
            .http_method(HttpMethodEnum.POST)
            .header_param(Parameter()
                .key("Content-Type")
                .value("application/json"))
            .body_param(Parameter()
                .value(body)
                .is_required(True))
            .header_param(Parameter()
                .key("accept")
                .value("application/json"))
            .body_serializer(APIHelper.json_serialize),
        ).response(
            ResponseHandler()
            .is_nullify404(True)
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(ServerResponse.from_dictionary)
            .is_api_response(True),
        ).execute()

    def send_rfc_1123_date_time_in_model(self,
                                         date_time):
        """Perform a POST request to /body/OptionalRfc1123InModel.

        Args:
            date_time (ModelWithOptionalRfc1123DateTime): The request body parameter.

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
            .path("/body/OptionalRfc1123InModel")
            .http_method(HttpMethodEnum.POST)
            .header_param(Parameter()
                .key("Content-Type")
                .value("application/json"))
            .body_param(Parameter()
                .value(date_time)
                .is_required(True))
            .header_param(Parameter()
                .key("accept")
                .value("application/json"))
            .body_serializer(APIHelper.json_serialize),
        ).response(
            ResponseHandler()
            .is_nullify404(True)
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(ServerResponse.from_dictionary)
            .is_api_response(True),
        ).execute()

    def send_optional_datetime_in_model(self,
                                        body):
        """Perform a POST request to /body/optionalDateTimeInBody.

        Args:
            body (ModelWithOptionalRfc3339DateTime): The request body parameter.

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
            .path("/body/optionalDateTimeInBody")
            .http_method(HttpMethodEnum.POST)
            .header_param(Parameter()
                .key("Content-Type")
                .value("application/json"))
            .body_param(Parameter()
                .value(body)
                .is_required(True))
            .header_param(Parameter()
                .key("accept")
                .value("application/json"))
            .body_serializer(APIHelper.json_serialize),
        ).response(
            ResponseHandler()
            .is_nullify404(True)
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(ServerResponse.from_dictionary)
            .is_api_response(True),
        ).execute()

    def send_rfc_339_date_time_in_nested_models(self,
                                                body):
        """Perform a POST request to /body/dateTimeInNestedModel.

        Args:
            body (SendRfc339DateTime): The request body parameter.

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
            .path("/body/dateTimeInNestedModel")
            .http_method(HttpMethodEnum.POST)
            .header_param(Parameter()
                .key("Content-Type")
                .value("application/json"))
            .body_param(Parameter()
                .value(body)
                .is_required(True))
            .header_param(Parameter()
                .key("accept")
                .value("application/json"))
            .body_serializer(APIHelper.json_serialize),
        ).response(
            ResponseHandler()
            .is_nullify404(True)
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(ServerResponse.from_dictionary)
            .is_api_response(True),
        ).execute()

    def uuid_as_optional(self,
                         body):
        """Perform a POST request to /body/optionalUUIDInModel.

        Args:
            body (UuidAsOptional): The request body parameter.

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
            .path("/body/optionalUUIDInModel")
            .http_method(HttpMethodEnum.POST)
            .header_param(Parameter()
                .key("Content-Type")
                .value("application/json"))
            .body_param(Parameter()
                .value(body)
                .is_required(True))
            .header_param(Parameter()
                .key("accept")
                .value("application/json"))
            .body_serializer(APIHelper.json_serialize),
        ).response(
            ResponseHandler()
            .is_nullify404(True)
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(ServerResponse.from_dictionary)
            .is_api_response(True),
        ).execute()

    def boolean_as_optional(self,
                            body):
        """Perform a POST request to /body/optionalBooleanInModel.

        Args:
            body (BooleanAsOptional): The request body parameter.

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
            .path("/body/optionalBooleanInModel")
            .http_method(HttpMethodEnum.POST)
            .header_param(Parameter()
                .key("Content-Type")
                .value("application/json"))
            .body_param(Parameter()
                .value(body)
                .is_required(True))
            .header_param(Parameter()
                .key("accept")
                .value("application/json"))
            .body_serializer(APIHelper.json_serialize),
        ).response(
            ResponseHandler()
            .is_nullify404(True)
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(ServerResponse.from_dictionary)
            .is_api_response(True),
        ).execute()

    def date_as_optional(self,
                         body):
        """Perform a POST request to /body/optionalDateInModel.

        Args:
            body (DateAsOptional): The request body parameter.

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
            .path("/body/optionalDateInModel")
            .http_method(HttpMethodEnum.POST)
            .header_param(Parameter()
                .key("Content-Type")
                .value("application/json"))
            .body_param(Parameter()
                .value(body)
                .is_required(True))
            .header_param(Parameter()
                .key("accept")
                .value("application/json"))
            .body_serializer(APIHelper.json_serialize),
        ).response(
            ResponseHandler()
            .is_nullify404(True)
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(ServerResponse.from_dictionary)
            .is_api_response(True),
        ).execute()

    def dynamic_as_optional(self,
                            body):
        """Perform a POST request to /body/optionalDynamicInModel.

        Args:
            body (DynamicAsOptional): The request body parameter.

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
            .path("/body/optionalDynamicInModel")
            .http_method(HttpMethodEnum.POST)
            .header_param(Parameter()
                .key("Content-Type")
                .value("application/json"))
            .body_param(Parameter()
                .value(body)
                .is_required(True))
            .header_param(Parameter()
                .key("accept")
                .value("application/json"))
            .body_serializer(APIHelper.json_serialize),
        ).response(
            ResponseHandler()
            .is_nullify404(True)
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(ServerResponse.from_dictionary)
            .is_api_response(True),
        ).execute()

    def all_optionals(self,
                      body,
                      option="empty"):
        """Perform a POST request to /body/alloptionals.

        Args:
            body (AllOptionals): The request body parameter.
            option (OptionalsEnum, optional): The request query parameter. Example:
                empty

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
            .path("/body/alloptionals")
            .http_method(HttpMethodEnum.POST)
            .header_param(Parameter()
                .key("Content-Type")
                .value("application/json"))
            .body_param(Parameter()
                .value(body)
                .is_required(True))
            .query_param(Parameter()
                .key("option")
                .value(option))
            .header_param(Parameter()
                .key("accept")
                .value("application/json"))
            .body_serializer(APIHelper.json_serialize),
        ).response(
            ResponseHandler()
            .is_nullify404(True)
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(ServerResponse.from_dictionary)
            .is_api_response(True),
        ).execute()

    def string_as_optional(self,
                           body):
        """Perform a POST request to /body/optionalStringInModel.

        Args:
            body (StringAsOptional): The request body parameter.

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
            .path("/body/optionalStringInModel")
            .http_method(HttpMethodEnum.POST)
            .header_param(Parameter()
                .key("Content-Type")
                .value("application/json"))
            .body_param(Parameter()
                .value(body)
                .is_required(True))
            .header_param(Parameter()
                .key("accept")
                .value("application/json"))
            .body_serializer(APIHelper.json_serialize),
        ).response(
            ResponseHandler()
            .is_nullify404(True)
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(ServerResponse.from_dictionary)
            .is_api_response(True),
        ).execute()

    def precision_as_optional(self,
                              body):
        """Perform a POST request to /body/optionalPrecisionInModel.

        Args:
            body (PrecisionAsOptional): The request body parameter.

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
            .path("/body/optionalPrecisionInModel")
            .http_method(HttpMethodEnum.POST)
            .header_param(Parameter()
                .key("Content-Type")
                .value("application/json"))
            .body_param(Parameter()
                .value(body)
                .is_required(True))
            .header_param(Parameter()
                .key("accept")
                .value("application/json"))
            .body_serializer(APIHelper.json_serialize),
        ).response(
            ResponseHandler()
            .is_nullify404(True)
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(ServerResponse.from_dictionary)
            .is_api_response(True),
        ).execute()

    def long_as_optional(self,
                         body):
        """Perform a POST request to /body/optionalLongInModel.

        Args:
            body (LongAsOptional): The request body parameter.

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
            .path("/body/optionalLongInModel")
            .http_method(HttpMethodEnum.POST)
            .header_param(Parameter()
                .key("Content-Type")
                .value("application/json"))
            .body_param(Parameter()
                .value(body)
                .is_required(True))
            .header_param(Parameter()
                .key("accept")
                .value("application/json"))
            .body_serializer(APIHelper.json_serialize),
        ).response(
            ResponseHandler()
            .is_nullify404(True)
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(ServerResponse.from_dictionary)
            .is_api_response(True),
        ).execute()

    def send_number_as_optional(self,
                                body):
        """Perform a POST request to /body/optionalNumberInModel.

        Args:
            body (NumberAsOptional): The request body parameter.

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
            .path("/body/optionalNumberInModel")
            .http_method(HttpMethodEnum.POST)
            .header_param(Parameter()
                .key("Content-Type")
                .value("application/json"))
            .body_param(Parameter()
                .value(body)
                .is_required(True))
            .header_param(Parameter()
                .key("accept")
                .value("application/json"))
            .body_serializer(APIHelper.json_serialize),
        ).response(
            ResponseHandler()
            .is_nullify404(True)
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(ServerResponse.from_dictionary)
            .is_api_response(True),
        ).execute()
