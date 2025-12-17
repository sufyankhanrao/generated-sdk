# -*- coding: utf-8 -*-

"""
tester

This file was automatically generated for Stamplay by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

from tester.api_helper import APIHelper
from tester.configuration import Server
from tester.http.api_response import ApiResponse
from tester.controllers.base_controller import BaseController
from apimatic_core.request_builder import RequestBuilder
from apimatic_core.response_handler import ResponseHandler
from apimatic_core.types.parameter import Parameter
from tester.http.http_method_enum import HttpMethodEnum
from apimatic_core.types.datetime_format import DateTimeFormat
from apimatic_core.configurations.endpoint_configuration import EndpointConfiguration
import dateutil.parser
from tester.models.company import Company
from tester.models.company import BossCompany
from tester.models.company import EmployeeComp
from tester.models.company import Developer
from tester.models.company import SoftwareTester
from tester.models.complex_1 import Complex1
from tester.models.response_with_enum import ResponseWithEnum
from tester.models.complex_2 import Complex2
from tester.models.complex_3 import Complex3
from tester.models.person import Person
from tester.models.void import Void


class ResponseTypesController(BaseController):

    """A Controller to access Endpoints in the tester API."""
    def __init__(self, config):
        super(ResponseTypesController, self).__init__(config)

    def get_date_array(self):
        """Does a GET request to /response/date.

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
            .path('/response/date')
            .http_method(HttpMethodEnum.GET)
            .query_param(Parameter()
                         .key('array')
                         .value(True))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
        ).response(
            ResponseHandler()
            .is_nullify404(True)
            .deserializer(APIHelper.date_deserialize)
            .is_api_response(True)
        ).execute()

    def get_date(self):
        """Does a GET request to /response/date.

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
            .path('/response/date')
            .http_method(HttpMethodEnum.GET)
        ).response(
            ResponseHandler()
            .is_nullify404(True)
            .deserializer(APIHelper.date_deserialize)
            .is_api_response(True)
        ).execute()

    def return_company_model(self):
        """Does a GET request to /response/company.

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
            .path('/response/company')
            .http_method(HttpMethodEnum.GET)
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
        ).response(
            ResponseHandler()
            .is_nullify404(True)
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(Company.from_dictionary)
            .is_api_response(True)
        ).execute()

    def return_boss_model(self):
        """Does a GET request to /response/boss.

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
            .path('/response/boss')
            .http_method(HttpMethodEnum.GET)
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
        ).response(
            ResponseHandler()
            .is_nullify404(True)
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(BossCompany.from_dictionary)
            .is_api_response(True)
        ).execute()

    def return_employee_model(self):
        """Does a GET request to /response/employee.

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
            .path('/response/employee')
            .http_method(HttpMethodEnum.GET)
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
        ).response(
            ResponseHandler()
            .is_nullify404(True)
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(EmployeeComp.from_dictionary)
            .is_api_response(True)
        ).execute()

    def return_developer_model(self):
        """Does a GET request to /response/developer.

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
            .path('/response/developer')
            .http_method(HttpMethodEnum.GET)
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
        ).response(
            ResponseHandler()
            .is_nullify404(True)
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(Developer.from_dictionary)
            .is_api_response(True)
        ).execute()

    def return_tester_model(self):
        """Does a GET request to /response/tester.

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
            .path('/response/tester')
            .http_method(HttpMethodEnum.GET)
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
        ).response(
            ResponseHandler()
            .is_nullify404(True)
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(SoftwareTester.from_dictionary)
            .is_api_response(True)
        ).execute()

    def return_complex_1_object(self):
        """Does a GET request to /response/complex1.

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
            .path('/response/complex1')
            .http_method(HttpMethodEnum.GET)
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
        ).response(
            ResponseHandler()
            .is_nullify404(True)
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(Complex1.from_dictionary)
            .is_api_response(True)
        ).execute()

    def return_response_with_enums(self):
        """Does a GET request to /response/responseWitEnum.

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
            .path('/response/responseWitEnum')
            .http_method(HttpMethodEnum.GET)
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
        ).response(
            ResponseHandler()
            .is_nullify404(True)
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(ResponseWithEnum.from_dictionary)
            .is_api_response(True)
        ).execute()

    def return_complex_2_object(self):
        """Does a GET request to /response/complex2.

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
            .path('/response/complex2')
            .http_method(HttpMethodEnum.GET)
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
        ).response(
            ResponseHandler()
            .is_nullify404(True)
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(Complex2.from_dictionary)
            .is_api_response(True)
        ).execute()

    def return_complex_3_object(self):
        """Does a GET request to /response/complex3.

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
            .path('/response/complex3')
            .http_method(HttpMethodEnum.GET)
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
        ).response(
            ResponseHandler()
            .is_nullify404(True)
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(Complex3.from_dictionary)
            .is_api_response(True)
        ).execute()

    def get_long(self):
        """Does a GET request to /response/long.

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
            .path('/response/long')
            .http_method(HttpMethodEnum.GET)
        ).response(
            ResponseHandler()
            .is_nullify404(True)
            .deserializer(APIHelper.json_deserialize)
            .is_api_response(True)
        ).execute()

    def get_model(self):
        """Does a GET request to /response/model.

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
            .path('/response/model')
            .http_method(HttpMethodEnum.GET)
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
        ).response(
            ResponseHandler()
            .is_nullify404(True)
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(Person.from_dictionary)
            .is_api_response(True)
        ).execute()

    def get_void_model(self):
        """Does a GET request to /response/getVoidModel.

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
            .path('/response/getVoidModel')
            .http_method(HttpMethodEnum.GET)
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
        ).response(
            ResponseHandler()
            .is_nullify404(True)
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(Void.from_dictionary)
            .is_api_response(True)
        ).execute()

    def get_string_enum_array(self):
        """Does a GET request to /response/enum.

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
            .path('/response/enum')
            .http_method(HttpMethodEnum.GET)
            .query_param(Parameter()
                         .key('array')
                         .value(True))
            .query_param(Parameter()
                         .key('type')
                         .value('string'))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
        ).response(
            ResponseHandler()
            .is_nullify404(True)
            .deserializer(APIHelper.json_deserialize)
            .is_api_response(True)
        ).execute()

    def get_string_enum(self):
        """Does a GET request to /response/enum.

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
            .path('/response/enum')
            .http_method(HttpMethodEnum.GET)
            .query_param(Parameter()
                         .key('type')
                         .value('string'))
        ).response(
            ResponseHandler()
            .is_nullify404(True)
            .deserializer(APIHelper.json_deserialize)
            .is_api_response(True)
        ).execute()

    def get_model_array(self):
        """Does a GET request to /response/model.

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
            .path('/response/model')
            .http_method(HttpMethodEnum.GET)
            .query_param(Parameter()
                         .key('array')
                         .value(True))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
        ).response(
            ResponseHandler()
            .is_nullify404(True)
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(Person.from_dictionary)
            .is_api_response(True)
        ).execute()

    def get_int_enum(self):
        """Does a GET request to /response/enum.

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
            .path('/response/enum')
            .http_method(HttpMethodEnum.GET)
            .query_param(Parameter()
                         .key('type')
                         .value('int'))
        ).response(
            ResponseHandler()
            .is_nullify404(True)
            .deserializer(APIHelper.json_deserialize)
            .is_api_response(True)
        ).execute()

    def get_int_enum_array(self):
        """Does a GET request to /response/enum.

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
            .path('/response/enum')
            .http_method(HttpMethodEnum.GET)
            .query_param(Parameter()
                         .key('array')
                         .value(True))
            .query_param(Parameter()
                         .key('type')
                         .value('int'))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
        ).response(
            ResponseHandler()
            .is_nullify404(True)
            .deserializer(APIHelper.json_deserialize)
            .is_api_response(True)
        ).execute()

    def get_precision(self):
        """Does a GET request to /response/precision.

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
            .path('/response/precision')
            .http_method(HttpMethodEnum.GET)
        ).response(
            ResponseHandler()
            .is_nullify404(True)
            .deserializer(APIHelper.json_deserialize)
            .is_api_response(True)
        ).execute()

    def get_binary(self):
        """Does a GET request to /response/binary.

        ﻿gets a binary﻿ object

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
            .path('/response/binary')
            .http_method(HttpMethodEnum.GET)
        ).response(
            ResponseHandler()
            .is_nullify404(True)
            .deserializer(APIHelper.json_deserialize)
            .is_api_response(True)
        ).endpoint_configuration(
            EndpointConfiguration()
            .has_binary_response(True)
        ).execute()

    def get_integer(self):
        """Does a GET request to /response/integer.

        Gets a integer response

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
            .path('/response/integer')
            .http_method(HttpMethodEnum.GET)
        ).response(
            ResponseHandler()
            .is_nullify404(True)
            .deserializer(APIHelper.json_deserialize)
            .is_api_response(True)
        ).execute()

    def get_integer_array(self):
        """Does a GET request to /response/integer.

        Get an array of integers.

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
            .path('/response/integer')
            .http_method(HttpMethodEnum.GET)
            .query_param(Parameter()
                         .key('array')
                         .value(True))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
        ).response(
            ResponseHandler()
            .is_nullify404(True)
            .deserializer(APIHelper.json_deserialize)
            .is_api_response(True)
        ).execute()

    def get_dynamic(self):
        """Does a GET request to /response/dynamic.

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
            .path('/response/dynamic')
            .http_method(HttpMethodEnum.GET)
            .query_param(Parameter()
                         .key('echo')
                         .value(True))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
        ).response(
            ResponseHandler()
            .is_nullify404(True)
            .deserializer(APIHelper.dynamic_deserialize)
            .is_api_response(True)
        ).execute()

    def get_dynamic_array(self):
        """Does a GET request to /response/dynamic.

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
            .path('/response/dynamic')
            .http_method(HttpMethodEnum.GET)
            .query_param(Parameter()
                         .key('array')
                         .value(True))
            .query_param(Parameter()
                         .key('echo')
                         .value(True))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
        ).response(
            ResponseHandler()
            .is_nullify404(True)
            .deserializer(APIHelper.dynamic_deserialize)
            .is_api_response(True)
        ).execute()

    def get_3339_datetime(self):
        """Does a GET request to /response/3339datetime.

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
            .path('/response/3339datetime')
            .http_method(HttpMethodEnum.GET)
        ).response(
            ResponseHandler()
            .is_nullify404(True)
            .deserializer(APIHelper.datetime_deserialize)
            .is_api_response(True)
            .datetime_format(DateTimeFormat.RFC3339_DATE_TIME)
        ).execute()

    def get_3339_datetime_array(self):
        """Does a GET request to /response/3339datetime.

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
            .path('/response/3339datetime')
            .http_method(HttpMethodEnum.GET)
            .query_param(Parameter()
                         .key('array')
                         .value(True))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
        ).response(
            ResponseHandler()
            .is_nullify404(True)
            .deserializer(APIHelper.datetime_deserialize)
            .is_api_response(True)
            .datetime_format(DateTimeFormat.RFC3339_DATE_TIME)
        ).execute()

    def get_boolean(self):
        """Does a GET request to /response/boolean.

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
            .path('/response/boolean')
            .http_method(HttpMethodEnum.GET)
        ).response(
            ResponseHandler()
            .is_nullify404(True)
            .deserializer(APIHelper.json_deserialize)
            .is_api_response(True)
        ).execute()

    def get_boolean_array(self):
        """Does a GET request to /response/boolean.

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
            .path('/response/boolean')
            .http_method(HttpMethodEnum.GET)
            .query_param(Parameter()
                         .key('array')
                         .value(True))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
        ).response(
            ResponseHandler()
            .is_nullify404(True)
            .deserializer(APIHelper.json_deserialize)
            .is_api_response(True)
        ).execute()

    def get_headers(self):
        """Does a GET request to /response/headers.

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
            .path('/response/headers')
            .http_method(HttpMethodEnum.GET)
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
        ).response(
            ResponseHandler()
            .is_nullify404(True)
            .is_api_response(True)
        ).execute()

    def get_1123_date_time(self):
        """Does a GET request to /response/1123datetime.

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
            .path('/response/1123datetime')
            .http_method(HttpMethodEnum.GET)
        ).response(
            ResponseHandler()
            .is_nullify404(True)
            .deserializer(APIHelper.datetime_deserialize)
            .is_api_response(True)
            .datetime_format(DateTimeFormat.HTTP_DATE_TIME)
        ).execute()

    def get_unix_date_time(self):
        """Does a GET request to /response/unixdatetime.

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
            .path('/response/unixdatetime')
            .http_method(HttpMethodEnum.GET)
        ).response(
            ResponseHandler()
            .is_nullify404(True)
            .deserializer(APIHelper.datetime_deserialize)
            .is_api_response(True)
            .datetime_format(DateTimeFormat.UNIX_DATE_TIME)
        ).execute()

    def get_1123_date_time_array(self):
        """Does a GET request to /response/1123datetime.

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
            .path('/response/1123datetime')
            .http_method(HttpMethodEnum.GET)
            .query_param(Parameter()
                         .key('array')
                         .value(True))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
        ).response(
            ResponseHandler()
            .is_nullify404(True)
            .deserializer(APIHelper.datetime_deserialize)
            .is_api_response(True)
            .datetime_format(DateTimeFormat.HTTP_DATE_TIME)
        ).execute()

    def get_unix_date_time_array(self):
        """Does a GET request to /response/unixdatetime.

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
            .path('/response/unixdatetime')
            .http_method(HttpMethodEnum.GET)
            .query_param(Parameter()
                         .key('array')
                         .value(True))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
        ).response(
            ResponseHandler()
            .is_nullify404(True)
            .deserializer(APIHelper.datetime_deserialize)
            .is_api_response(True)
            .datetime_format(DateTimeFormat.UNIX_DATE_TIME)
        ).execute()

    def get_content_type_headers(self):
        """Does a GET request to /response/getContentType.

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
            .path('/response/getContentType')
            .http_method(HttpMethodEnum.GET)
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
        ).response(
            ResponseHandler()
            .is_nullify404(True)
            .is_api_response(True)
        ).execute()
