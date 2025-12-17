# -*- coding: utf-8 -*-

"""
tester

This file was automatically generated for Stamplay by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

from tester.api_helper import APIHelper
from tester.configuration import Server
from tester.http.api_response import ApiResponse
from tester.utilities.file_wrapper import FileWrapper
from tester.controllers.base_controller import BaseController
from apimatic_core.request_builder import RequestBuilder
from apimatic_core.response_handler import ResponseHandler
from apimatic_core.types.parameter import Parameter
from tester.http.http_method_enum import HttpMethodEnum
from tester.models.server_response import ServerResponse


class FormParamsController(BaseController):

    """A Controller to access Endpoints in the tester API."""
    def __init__(self, config):
        super(FormParamsController, self).__init__(config)

    def send_delete_form(self,
                         body):
        """Does a DELETE request to /form/deleteForm.

        Args:
            body (DeleteBody): The request form parameter.

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
            .path('/form/deleteForm')
            .http_method(HttpMethodEnum.DELETE)
            .form_param(Parameter()
                        .key('body')
                        .value(body)
                        .is_required(True))
            .header_param(Parameter()
                          .key('content-type')
                          .value('application/x-www-form-urlencoded'))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
        ).response(
            ResponseHandler()
            .is_nullify404(True)
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(ServerResponse.from_dictionary)
            .is_api_response(True)
        ).execute()

    def send_delete_multipart(self,
                              file):
        """Does a DELETE request to /form/deleteMultipart.

        Args:
            file (typing.BinaryIO): The request form parameter.

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
            .path('/form/deleteMultipart')
            .http_method(HttpMethodEnum.DELETE)
            .multipart_param(Parameter()
                             .key('file')
                             .value(file)
                             .default_content_type('application/octet-stream')
                             .is_required(True))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
        ).response(
            ResponseHandler()
            .is_nullify404(True)
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(ServerResponse.from_dictionary)
            .is_api_response(True)
        ).execute()

    def send_date_array(self,
                        dates):
        """Does a POST request to /form/date.

        Args:
            dates (List[date]): The request form parameter.

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
            .path('/form/date')
            .http_method(HttpMethodEnum.POST)
            .query_param(Parameter()
                         .key('array')
                         .value(True))
            .form_param(Parameter()
                        .key('dates')
                        .value(dates)
                        .is_required(True))
            .header_param(Parameter()
                          .key('content-type')
                          .value('application/x-www-form-urlencoded'))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
        ).response(
            ResponseHandler()
            .is_nullify404(True)
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(ServerResponse.from_dictionary)
            .is_api_response(True)
        ).execute()

    def send_date(self,
                  date):
        """Does a POST request to /form/date.

        Args:
            date (date): The request form parameter.

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
            .path('/form/date')
            .http_method(HttpMethodEnum.POST)
            .form_param(Parameter()
                        .key('date')
                        .value(date)
                        .is_required(True))
            .header_param(Parameter()
                          .key('content-type')
                          .value('application/x-www-form-urlencoded'))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
        ).response(
            ResponseHandler()
            .is_nullify404(True)
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(ServerResponse.from_dictionary)
            .is_api_response(True)
        ).execute()

    def send_unix_date_time(self,
                            datetime):
        """Does a POST request to /form/unixdatetime.

        Args:
            datetime (datetime): The request form parameter.

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
            .path('/form/unixdatetime')
            .http_method(HttpMethodEnum.POST)
            .form_param(Parameter()
                        .key('datetime')
                        .value(APIHelper.when_defined(APIHelper.UnixDateTime, datetime))
                        .is_required(True))
            .header_param(Parameter()
                          .key('content-type')
                          .value('application/x-www-form-urlencoded'))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
        ).response(
            ResponseHandler()
            .is_nullify404(True)
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(ServerResponse.from_dictionary)
            .is_api_response(True)
        ).execute()

    def send_rfc_1123_date_time(self,
                                datetime):
        """Does a POST request to /form/rfc1123datetime.

        Args:
            datetime (datetime): The request form parameter.

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
            .path('/form/rfc1123datetime')
            .http_method(HttpMethodEnum.POST)
            .form_param(Parameter()
                        .key('datetime')
                        .value(APIHelper.when_defined(APIHelper.HttpDateTime, datetime))
                        .is_required(True))
            .header_param(Parameter()
                          .key('content-type')
                          .value('application/x-www-form-urlencoded'))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
        ).response(
            ResponseHandler()
            .is_nullify404(True)
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(ServerResponse.from_dictionary)
            .is_api_response(True)
        ).execute()

    def send_rfc_3339_date_time(self,
                                datetime):
        """Does a POST request to /form/rfc3339datetime.

        Args:
            datetime (datetime): The request form parameter.

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
            .path('/form/rfc3339datetime')
            .http_method(HttpMethodEnum.POST)
            .form_param(Parameter()
                        .key('datetime')
                        .value(APIHelper.when_defined(APIHelper.RFC3339DateTime, datetime))
                        .is_required(True))
            .header_param(Parameter()
                          .key('content-type')
                          .value('application/x-www-form-urlencoded'))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
        ).response(
            ResponseHandler()
            .is_nullify404(True)
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(ServerResponse.from_dictionary)
            .is_api_response(True)
        ).execute()

    def send_unix_date_time_array(self,
                                  datetimes):
        """Does a POST request to /form/unixdatetime.

        Args:
            datetimes (List[datetime]): The request form parameter.

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
            .path('/form/unixdatetime')
            .http_method(HttpMethodEnum.POST)
            .query_param(Parameter()
                         .key('array')
                         .value(True))
            .form_param(Parameter()
                        .key('datetimes')
                        .value([APIHelper.when_defined(APIHelper.UnixDateTime, element) for element in datetimes])
                        .is_required(True))
            .header_param(Parameter()
                          .key('content-type')
                          .value('application/x-www-form-urlencoded'))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
        ).response(
            ResponseHandler()
            .is_nullify404(True)
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(ServerResponse.from_dictionary)
            .is_api_response(True)
        ).execute()

    def send_rfc_1123_date_time_array(self,
                                      datetimes):
        """Does a POST request to /form/rfc1123datetime.

        Args:
            datetimes (List[datetime]): The request form parameter.

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
            .path('/form/rfc1123datetime')
            .http_method(HttpMethodEnum.POST)
            .query_param(Parameter()
                         .key('array')
                         .value(True))
            .form_param(Parameter()
                        .key('datetimes')
                        .value([APIHelper.when_defined(APIHelper.HttpDateTime, element) for element in datetimes])
                        .is_required(True))
            .header_param(Parameter()
                          .key('content-type')
                          .value('application/x-www-form-urlencoded'))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
        ).response(
            ResponseHandler()
            .is_nullify404(True)
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(ServerResponse.from_dictionary)
            .is_api_response(True)
        ).execute()

    def send_long(self,
                  value):
        """Does a POST request to /form/number.

        Args:
            value (int): The request form parameter.

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
            .path('/form/number')
            .http_method(HttpMethodEnum.POST)
            .form_param(Parameter()
                        .key('value')
                        .value(value)
                        .is_required(True))
            .header_param(Parameter()
                          .key('content-type')
                          .value('application/x-www-form-urlencoded'))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
        ).response(
            ResponseHandler()
            .is_nullify404(True)
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(ServerResponse.from_dictionary)
            .is_api_response(True)
        ).execute()

    def send_integer_array(self,
                           integers):
        """Does a POST request to /form/number.

        Args:
            integers (List[int]): The request form parameter.

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
            .path('/form/number')
            .http_method(HttpMethodEnum.POST)
            .query_param(Parameter()
                         .key('array')
                         .value(True))
            .form_param(Parameter()
                        .key('integers')
                        .value(integers)
                        .is_required(True))
            .header_param(Parameter()
                          .key('content-type')
                          .value('application/x-www-form-urlencoded'))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
        ).response(
            ResponseHandler()
            .is_nullify404(True)
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(ServerResponse.from_dictionary)
            .is_api_response(True)
        ).execute()

    def send_string_array(self,
                          strings):
        """Does a POST request to /form/string.

        Args:
            strings (List[str]): The request form parameter.

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
            .path('/form/string')
            .http_method(HttpMethodEnum.POST)
            .query_param(Parameter()
                         .key('array')
                         .value(True))
            .form_param(Parameter()
                        .key('strings')
                        .value(strings)
                        .is_required(True))
            .header_param(Parameter()
                          .key('content-type')
                          .value('application/x-www-form-urlencoded'))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
        ).response(
            ResponseHandler()
            .is_nullify404(True)
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(ServerResponse.from_dictionary)
            .is_api_response(True)
        ).execute()

    def allow_dynamic_form_fields(self,
                                  name,
                                  _optional_form_parameters=None):
        """Does a POST request to /form/allowDynamicFormFields.

        Args:
            name (str): The request form parameter.
            _optional_form_parameters (Array, optional): Additional optional
                form parameters are supported by this endpoint

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
            .path('/form/allowDynamicFormFields')
            .http_method(HttpMethodEnum.POST)
            .form_param(Parameter()
                        .key('name')
                        .value(name)
                        .is_required(True))
            .header_param(Parameter()
                          .key('content-type')
                          .value('application/x-www-form-urlencoded'))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .additional_form_params(_optional_form_parameters)
        ).response(
            ResponseHandler()
            .is_nullify404(True)
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(ServerResponse.from_dictionary)
            .is_api_response(True)
        ).execute()

    def send_model(self,
                   model):
        """Does a POST request to /form/model.

        Args:
            model (Employee): The request form parameter.

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
            .path('/form/model')
            .http_method(HttpMethodEnum.POST)
            .form_param(Parameter()
                        .key('model')
                        .value(model)
                        .is_required(True))
            .header_param(Parameter()
                          .key('content-type')
                          .value('application/x-www-form-urlencoded'))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
        ).response(
            ResponseHandler()
            .is_nullify404(True)
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(ServerResponse.from_dictionary)
            .is_api_response(True)
        ).execute()

    def send_model_array(self,
                         models):
        """Does a POST request to /form/model.

        Args:
            models (List[Employee]): The request form parameter.

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
            .path('/form/model')
            .http_method(HttpMethodEnum.POST)
            .query_param(Parameter()
                         .key('array')
                         .value(True))
            .form_param(Parameter()
                        .key('models')
                        .value(models)
                        .is_required(True))
            .header_param(Parameter()
                          .key('content-type')
                          .value('application/x-www-form-urlencoded'))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
        ).response(
            ResponseHandler()
            .is_nullify404(True)
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(ServerResponse.from_dictionary)
            .is_api_response(True)
        ).execute()

    def send_file(self,
                  file):
        """Does a POST request to /form/file.

        Args:
            file (typing.BinaryIO): The request form parameter.

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
            .path('/form/file')
            .http_method(HttpMethodEnum.POST)
            .multipart_param(Parameter()
                             .key('file')
                             .value(file)
                             .default_content_type('application/octet-stream')
                             .is_required(True))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
        ).response(
            ResponseHandler()
            .is_nullify404(True)
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(ServerResponse.from_dictionary)
            .is_api_response(True)
        ).execute()

    def send_multiple_files(self,
                            file,
                            file_1):
        """Does a POST request to /form/multipleFiles.

        Args:
            file (typing.BinaryIO): The request form parameter.
            file_1 (typing.BinaryIO): The request form parameter.

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
            .path('/form/multipleFiles')
            .http_method(HttpMethodEnum.POST)
            .multipart_param(Parameter()
                             .key('file')
                             .value(file)
                             .default_content_type('application/octet-stream')
                             .is_required(True))
            .multipart_param(Parameter()
                             .key('file1')
                             .value(file_1)
                             .default_content_type('application/octet-stream')
                             .is_required(True))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
        ).response(
            ResponseHandler()
            .is_nullify404(True)
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(ServerResponse.from_dictionary)
            .is_api_response(True)
        ).execute()

    def send_string(self,
                    value):
        """Does a POST request to /form/string.

        Args:
            value (str): The request form parameter.

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
            .path('/form/string')
            .http_method(HttpMethodEnum.POST)
            .form_param(Parameter()
                        .key('value')
                        .value(value)
                        .is_required(True))
            .header_param(Parameter()
                          .key('content-type')
                          .value('application/x-www-form-urlencoded'))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
        ).response(
            ResponseHandler()
            .is_nullify404(True)
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(ServerResponse.from_dictionary)
            .is_api_response(True)
        ).execute()

    def send_rfc_3339_date_time_array(self,
                                      datetimes):
        """Does a POST request to /form/rfc3339datetime.

        Args:
            datetimes (List[datetime]): The request form parameter.

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
            .path('/form/rfc3339datetime')
            .http_method(HttpMethodEnum.POST)
            .query_param(Parameter()
                         .key('array')
                         .value(True))
            .form_param(Parameter()
                        .key('datetimes')
                        .value([APIHelper.when_defined(APIHelper.RFC3339DateTime, element) for element in datetimes])
                        .is_required(True))
            .header_param(Parameter()
                          .key('content-type')
                          .value('application/x-www-form-urlencoded'))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
        ).response(
            ResponseHandler()
            .is_nullify404(True)
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(ServerResponse.from_dictionary)
            .is_api_response(True)
        ).execute()

    def send_mixed_array(self,
                         options=dict()):
        """Does a POST request to /form/mixed.

        Send a variety for form params. Returns file count and body params

        Args:
            options (dict, optional): Key-value pairs for any of the
                parameters to this API Endpoint. All parameters to the
                endpoint are supplied through the dictionary with their names
                being the key and their desired values being the value. A list
                of parameters that can be used are::

                    file -- typing.BinaryIO -- The request form parameter.
                    integers -- List[int] -- The request form parameter.
                    models -- List[Employee] -- The request form parameter.
                    strings -- List[str] -- The request form parameter.

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
            .path('/form/mixed')
            .http_method(HttpMethodEnum.POST)
            .multipart_param(Parameter()
                             .key('file')
                             .value(options.get('file', None))
                             .default_content_type('application/octet-stream')
                             .is_required(True))
            .form_param(Parameter()
                        .key('integers')
                        .value(options.get('integers', None))
                        .is_required(True))
            .form_param(Parameter()
                        .key('models')
                        .value(options.get('models', None))
                        .is_required(True))
            .form_param(Parameter()
                        .key('strings')
                        .value(options.get('strings', None))
                        .is_required(True))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
        ).response(
            ResponseHandler()
            .is_nullify404(True)
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(ServerResponse.from_dictionary)
            .is_api_response(True)
        ).execute()

    def update_model_with_form(self,
                               model):
        """Does a PUT request to /form/updateModel.

        Args:
            model (Employee): The request form parameter.

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
            .path('/form/updateModel')
            .http_method(HttpMethodEnum.PUT)
            .form_param(Parameter()
                        .key('model')
                        .value(model)
                        .is_required(True))
            .header_param(Parameter()
                          .key('content-type')
                          .value('application/x-www-form-urlencoded'))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
        ).response(
            ResponseHandler()
            .is_nullify404(True)
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(ServerResponse.from_dictionary)
            .is_api_response(True)
        ).execute()

    def send_delete_form_1(self,
                           model):
        """Does a DELETE request to /form/deleteForm1.

        Args:
            model (Employee): The request form parameter.

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
            .path('/form/deleteForm1')
            .http_method(HttpMethodEnum.DELETE)
            .form_param(Parameter()
                        .key('model')
                        .value(model)
                        .is_required(True))
            .header_param(Parameter()
                          .key('content-type')
                          .value('application/x-www-form-urlencoded'))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
        ).response(
            ResponseHandler()
            .is_nullify404(True)
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(ServerResponse.from_dictionary)
            .is_api_response(True)
        ).execute()

    def send_delete_form_with_model_array(self,
                                          models):
        """Does a DELETE request to /form/deleteForm1.

        Args:
            models (List[Employee]): The request form parameter.

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
            .path('/form/deleteForm1')
            .http_method(HttpMethodEnum.DELETE)
            .query_param(Parameter()
                         .key('array')
                         .value(True))
            .form_param(Parameter()
                        .key('models')
                        .value(models)
                        .is_required(True))
            .header_param(Parameter()
                          .key('content-type')
                          .value('application/x-www-form-urlencoded'))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
        ).response(
            ResponseHandler()
            .is_nullify404(True)
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(ServerResponse.from_dictionary)
            .is_api_response(True)
        ).execute()

    def update_model_array_with_form(self,
                                     models):
        """Does a PUT request to /form/updateModel.

        Args:
            models (List[Employee]): The request form parameter.

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
            .path('/form/updateModel')
            .http_method(HttpMethodEnum.PUT)
            .query_param(Parameter()
                         .key('array')
                         .value(True))
            .form_param(Parameter()
                        .key('models')
                        .value(models)
                        .is_required(True))
            .header_param(Parameter()
                          .key('content-type')
                          .value('application/x-www-form-urlencoded'))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
        ).response(
            ResponseHandler()
            .is_nullify404(True)
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(ServerResponse.from_dictionary)
            .is_api_response(True)
        ).execute()

    def update_string_with_form(self,
                                value):
        """Does a PUT request to /form/updateString.

        Args:
            value (str): The request form parameter.

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
            .path('/form/updateString')
            .http_method(HttpMethodEnum.PUT)
            .form_param(Parameter()
                        .key('value')
                        .value(value)
                        .is_required(True))
            .header_param(Parameter()
                          .key('content-type')
                          .value('application/x-www-form-urlencoded'))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
        ).response(
            ResponseHandler()
            .is_nullify404(True)
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(ServerResponse.from_dictionary)
            .is_api_response(True)
        ).execute()

    def update_string_array_with_form(self,
                                      strings):
        """Does a PUT request to /form/updateString.

        Args:
            strings (List[str]): The request form parameter.

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
            .path('/form/updateString')
            .http_method(HttpMethodEnum.PUT)
            .query_param(Parameter()
                         .key('array')
                         .value(True))
            .form_param(Parameter()
                        .key('strings')
                        .value(strings)
                        .is_required(True))
            .header_param(Parameter()
                          .key('content-type')
                          .value('application/x-www-form-urlencoded'))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
        ).response(
            ResponseHandler()
            .is_nullify404(True)
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(ServerResponse.from_dictionary)
            .is_api_response(True)
        ).execute()

    def send_integer_enum_array(self,
                                suites):
        """Does a POST request to /form/integerenum.

        Args:
            suites (List[SuiteCodeEnum]): The request form parameter.

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
            .path('/form/integerenum')
            .http_method(HttpMethodEnum.POST)
            .query_param(Parameter()
                         .key('array')
                         .value(True))
            .form_param(Parameter()
                        .key('suites')
                        .value(suites)
                        .is_required(True))
            .header_param(Parameter()
                          .key('content-type')
                          .value('application/x-www-form-urlencoded'))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
        ).response(
            ResponseHandler()
            .is_nullify404(True)
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(ServerResponse.from_dictionary)
            .is_api_response(True)
        ).execute()

    def send_string_enum_array(self,
                               days):
        """Does a POST request to /form/stringenum.

        Args:
            days (List[Days1Enum]): The request form parameter.

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
            .path('/form/stringenum')
            .http_method(HttpMethodEnum.POST)
            .query_param(Parameter()
                         .key('array')
                         .value(True))
            .form_param(Parameter()
                        .key('days')
                        .value(days)
                        .is_required(True))
            .header_param(Parameter()
                          .key('content-type')
                          .value('application/x-www-form-urlencoded'))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
        ).response(
            ResponseHandler()
            .is_nullify404(True)
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(ServerResponse.from_dictionary)
            .is_api_response(True)
        ).execute()

    def send_string_in_form_with_new_line(self,
                                          body):
        """Does a POST request to /form/stringEncoding.

        Args:
            body (TestNstringEncoding): The request form parameter.

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
            .path('/form/stringEncoding')
            .http_method(HttpMethodEnum.POST)
            .form_param(Parameter()
                        .key('body')
                        .value(body)
                        .is_required(True))
            .header_param(Parameter()
                          .key('content-type')
                          .value('application/x-www-form-urlencoded'))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
        ).response(
            ResponseHandler()
            .is_nullify404(True)
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(ServerResponse.from_dictionary)
            .is_api_response(True)
        ).execute()

    def send_string_in_form_with_r(self,
                                   body):
        """Does a POST request to /form/stringEncoding.

        Args:
            body (TestRstringEncoding): The request form parameter.

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
            .path('/form/stringEncoding')
            .http_method(HttpMethodEnum.POST)
            .form_param(Parameter()
                        .key('body')
                        .value(body)
                        .is_required(True))
            .header_param(Parameter()
                          .key('content-type')
                          .value('application/x-www-form-urlencoded'))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
        ).response(
            ResponseHandler()
            .is_nullify404(True)
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(ServerResponse.from_dictionary)
            .is_api_response(True)
        ).execute()

    def send_string_in_form_with_r_n(self,
                                     body):
        """Does a POST request to /form/stringEncoding.

        Args:
            body (TestRNstringEncoding): The request form parameter.

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
            .path('/form/stringEncoding')
            .http_method(HttpMethodEnum.POST)
            .form_param(Parameter()
                        .key('body')
                        .value(body)
                        .is_required(True))
            .header_param(Parameter()
                          .key('content-type')
                          .value('application/x-www-form-urlencoded'))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
        ).response(
            ResponseHandler()
            .is_nullify404(True)
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(ServerResponse.from_dictionary)
            .is_api_response(True)
        ).execute()

    def all_optionals(self,
                      model,
                      option='empty'):
        """Does a POST request to /form/alloptionals.

        Args:
            model (AllOptionals): The request form parameter.
            option (OptionalsEnum, optional): The request form parameter.
                Example: empty

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
            .path('/form/alloptionals')
            .http_method(HttpMethodEnum.POST)
            .form_param(Parameter()
                        .key('model')
                        .value(model)
                        .is_required(True))
            .form_param(Parameter()
                        .key('option')
                        .value(option))
            .header_param(Parameter()
                          .key('content-type')
                          .value('application/x-www-form-urlencoded'))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
        ).response(
            ResponseHandler()
            .is_nullify404(True)
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(ServerResponse.from_dictionary)
            .is_api_response(True)
        ).execute()

    def send_optional_unix_date_time_in_body(self,
                                             date_time=None):
        """Does a POST request to /form/optionalUnixTimeStamp.

        Args:
            date_time (datetime, optional): The request form parameter.

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
            .path('/form/optionalUnixTimeStamp')
            .http_method(HttpMethodEnum.POST)
            .form_param(Parameter()
                        .key('dateTime')
                        .value(APIHelper.when_defined(APIHelper.UnixDateTime, date_time)))
            .header_param(Parameter()
                          .key('content-type')
                          .value('application/x-www-form-urlencoded'))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
        ).response(
            ResponseHandler()
            .is_nullify404(True)
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(ServerResponse.from_dictionary)
            .is_api_response(True)
        ).execute()

    def send_optional_rfc_1123_in_body(self,
                                       body):
        """Does a POST request to /form/optionlRfc1123.

        Args:
            body (datetime): The request form parameter.

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
            .path('/form/optionlRfc1123')
            .http_method(HttpMethodEnum.POST)
            .form_param(Parameter()
                        .key('body')
                        .value(APIHelper.when_defined(APIHelper.HttpDateTime, body))
                        .is_required(True))
            .header_param(Parameter()
                          .key('content-type')
                          .value('application/x-www-form-urlencoded'))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
        ).response(
            ResponseHandler()
            .is_nullify404(True)
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(ServerResponse.from_dictionary)
            .is_api_response(True)
        ).execute()

    def send_datetime_optional_in_endpoint(self,
                                           body=None):
        """Does a POST request to /form/optionalDateTime.

        Args:
            body (datetime, optional): The request form parameter.

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
            .path('/form/optionalDateTime')
            .http_method(HttpMethodEnum.POST)
            .form_param(Parameter()
                        .key('body')
                        .value(APIHelper.when_defined(APIHelper.RFC3339DateTime, body)))
            .header_param(Parameter()
                          .key('content-type')
                          .value('application/x-www-form-urlencoded'))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
        ).response(
            ResponseHandler()
            .is_nullify404(True)
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(ServerResponse.from_dictionary)
            .is_api_response(True)
        ).execute()

    def send_optional_unix_time_stamp_in_model_body(self,
                                                    date_time):
        """Does a POST request to /form/optionalUnixDateTimeInModel.

        Args:
            date_time (UnixDateTime): The request form parameter.

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
            .path('/form/optionalUnixDateTimeInModel')
            .http_method(HttpMethodEnum.POST)
            .form_param(Parameter()
                        .key('dateTime')
                        .value(date_time)
                        .is_required(True))
            .header_param(Parameter()
                          .key('content-type')
                          .value('application/x-www-form-urlencoded'))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
        ).response(
            ResponseHandler()
            .is_nullify404(True)
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(ServerResponse.from_dictionary)
            .is_api_response(True)
        ).execute()

    def send_optional_unix_time_stamp_in_nested_model_body(self,
                                                           date_time):
        """Does a POST request to /form/optionalUnixTimeStampInNestedModel.

        Args:
            date_time (SendUnixDateTime): The request form parameter.

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
            .path('/form/optionalUnixTimeStampInNestedModel')
            .http_method(HttpMethodEnum.POST)
            .form_param(Parameter()
                        .key('dateTime')
                        .value(date_time)
                        .is_required(True))
            .header_param(Parameter()
                          .key('content-type')
                          .value('application/x-www-form-urlencoded'))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
        ).response(
            ResponseHandler()
            .is_nullify404(True)
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(ServerResponse.from_dictionary)
            .is_api_response(True)
        ).execute()

    def send_rfc_1123_date_time_in_nested_model(self,
                                                body):
        """Does a POST request to /form/rfc1123InNestedModel.

        Args:
            body (SendRfc1123DateTime): The request form parameter.

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
            .path('/form/rfc1123InNestedModel')
            .http_method(HttpMethodEnum.POST)
            .form_param(Parameter()
                        .key('body')
                        .value(body)
                        .is_required(True))
            .header_param(Parameter()
                          .key('content-type')
                          .value('application/x-www-form-urlencoded'))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
        ).response(
            ResponseHandler()
            .is_nullify404(True)
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(ServerResponse.from_dictionary)
            .is_api_response(True)
        ).execute()

    def send_rfc_1123_date_time_in_model(self,
                                         date_time):
        """Does a POST request to /form/OptionalRfc1123InModel.

        Args:
            date_time (ModelWithOptionalRfc1123DateTime): The request form
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
            .path('/form/OptionalRfc1123InModel')
            .http_method(HttpMethodEnum.POST)
            .form_param(Parameter()
                        .key('dateTime')
                        .value(date_time)
                        .is_required(True))
            .header_param(Parameter()
                          .key('content-type')
                          .value('application/x-www-form-urlencoded'))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
        ).response(
            ResponseHandler()
            .is_nullify404(True)
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(ServerResponse.from_dictionary)
            .is_api_response(True)
        ).execute()

    def send_optional_datetime_in_model(self,
                                        body):
        """Does a POST request to /form/optionalDateTimeInBody.

        Args:
            body (ModelWithOptionalRfc3339DateTime): The request form
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
            .path('/form/optionalDateTimeInBody')
            .http_method(HttpMethodEnum.POST)
            .form_param(Parameter()
                        .key('body')
                        .value(body)
                        .is_required(True))
            .header_param(Parameter()
                          .key('content-type')
                          .value('application/x-www-form-urlencoded'))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
        ).response(
            ResponseHandler()
            .is_nullify404(True)
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(ServerResponse.from_dictionary)
            .is_api_response(True)
        ).execute()

    def send_rfc_339_date_time_in_nested_models(self,
                                                body):
        """Does a POST request to /form/dateTimeInNestedModel.

        Args:
            body (SendRfc339DateTime): The request form parameter.

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
            .path('/form/dateTimeInNestedModel')
            .http_method(HttpMethodEnum.POST)
            .form_param(Parameter()
                        .key('body')
                        .value(body)
                        .is_required(True))
            .header_param(Parameter()
                          .key('content-type')
                          .value('application/x-www-form-urlencoded'))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
        ).response(
            ResponseHandler()
            .is_nullify404(True)
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(ServerResponse.from_dictionary)
            .is_api_response(True)
        ).execute()

    def uuid_as_optional(self,
                         body):
        """Does a POST request to /form/optionalUUIDInModel.

        Args:
            body (UuidAsOptional): The request form parameter.

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
            .path('/form/optionalUUIDInModel')
            .http_method(HttpMethodEnum.POST)
            .form_param(Parameter()
                        .key('body')
                        .value(body)
                        .is_required(True))
            .header_param(Parameter()
                          .key('content-type')
                          .value('application/x-www-form-urlencoded'))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
        ).response(
            ResponseHandler()
            .is_nullify404(True)
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(ServerResponse.from_dictionary)
            .is_api_response(True)
        ).execute()

    def boolean_as_optional(self,
                            body):
        """Does a POST request to /form/optionalBooleanInModel.

        Args:
            body (BooleanAsOptional): The request form parameter.

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
            .path('/form/optionalBooleanInModel')
            .http_method(HttpMethodEnum.POST)
            .form_param(Parameter()
                        .key('body')
                        .value(body)
                        .is_required(True))
            .header_param(Parameter()
                          .key('content-type')
                          .value('application/x-www-form-urlencoded'))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
        ).response(
            ResponseHandler()
            .is_nullify404(True)
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(ServerResponse.from_dictionary)
            .is_api_response(True)
        ).execute()

    def date_as_optional(self,
                         body):
        """Does a POST request to /form/optionalDateInModel.

        Args:
            body (DateAsOptional): The request form parameter.

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
            .path('/form/optionalDateInModel')
            .http_method(HttpMethodEnum.POST)
            .form_param(Parameter()
                        .key('body')
                        .value(body)
                        .is_required(True))
            .header_param(Parameter()
                          .key('content-type')
                          .value('application/x-www-form-urlencoded'))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
        ).response(
            ResponseHandler()
            .is_nullify404(True)
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(ServerResponse.from_dictionary)
            .is_api_response(True)
        ).execute()

    def dynamic_as_optional(self,
                            body):
        """Does a POST request to /form/optionalDynamicInModel.

        Args:
            body (DynamicAsOptional): The request form parameter.

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
            .path('/form/optionalDynamicInModel')
            .http_method(HttpMethodEnum.POST)
            .form_param(Parameter()
                        .key('body')
                        .value(body)
                        .is_required(True))
            .header_param(Parameter()
                          .key('content-type')
                          .value('application/x-www-form-urlencoded'))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
        ).response(
            ResponseHandler()
            .is_nullify404(True)
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(ServerResponse.from_dictionary)
            .is_api_response(True)
        ).execute()

    def string_as_optional(self,
                           body):
        """Does a POST request to /form/optionalStringInModel.

        Args:
            body (StringAsOptional): The request form parameter.

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
            .path('/form/optionalStringInModel')
            .http_method(HttpMethodEnum.POST)
            .form_param(Parameter()
                        .key('body')
                        .value(body)
                        .is_required(True))
            .header_param(Parameter()
                          .key('content-type')
                          .value('application/x-www-form-urlencoded'))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
        ).response(
            ResponseHandler()
            .is_nullify404(True)
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(ServerResponse.from_dictionary)
            .is_api_response(True)
        ).execute()

    def precision_as_optional(self,
                              body):
        """Does a POST request to /form/optionalPrecisionInModel.

        Args:
            body (PrecisionAsOptional): The request form parameter.

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
            .path('/form/optionalPrecisionInModel')
            .http_method(HttpMethodEnum.POST)
            .form_param(Parameter()
                        .key('body')
                        .value(body)
                        .is_required(True))
            .header_param(Parameter()
                          .key('content-type')
                          .value('application/x-www-form-urlencoded'))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
        ).response(
            ResponseHandler()
            .is_nullify404(True)
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(ServerResponse.from_dictionary)
            .is_api_response(True)
        ).execute()

    def long_as_optional(self,
                         body):
        """Does a POST request to /form/optionalLongInModel.

        Args:
            body (LongAsOptional): The request form parameter.

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
            .path('/form/optionalLongInModel')
            .http_method(HttpMethodEnum.POST)
            .form_param(Parameter()
                        .key('body')
                        .value(body)
                        .is_required(True))
            .header_param(Parameter()
                          .key('content-type')
                          .value('application/x-www-form-urlencoded'))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
        ).response(
            ResponseHandler()
            .is_nullify404(True)
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(ServerResponse.from_dictionary)
            .is_api_response(True)
        ).execute()

    def send_number_as_optional(self,
                                body):
        """Does a POST request to /form/optionalNumberInModel.

        Args:
            body (NumberAsOptional): The request form parameter.

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
            .path('/form/optionalNumberInModel')
            .http_method(HttpMethodEnum.POST)
            .form_param(Parameter()
                        .key('body')
                        .value(body)
                        .is_required(True))
            .header_param(Parameter()
                          .key('content-type')
                          .value('application/x-www-form-urlencoded'))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
        ).response(
            ResponseHandler()
            .is_nullify404(True)
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(ServerResponse.from_dictionary)
            .is_api_response(True)
        ).execute()
