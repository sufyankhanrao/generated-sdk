# -*- coding: utf-8 -*-

"""
tester

This file was automatically generated for Stamplay by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

import platform
from apimatic_core.api_call import ApiCall
from apimatic_core.types.error_case import ErrorCase
from tester.exceptions.api_exception import APIException
from tester.exceptions.nested_model_exception import NestedModelException
from tester.exceptions.custom_error_response_exception import CustomErrorResponseException
from tester.exceptions.exception_with_string_exception import ExceptionWithStringException
from tester.exceptions.exception_with_boolean_exception import ExceptionWithBooleanException
from tester.exceptions.exception_with_dynamic_exception import ExceptionWithDynamicException
from tester.exceptions.exception_with_uuid_exception import ExceptionWithUUIDException
from tester.exceptions.exception_with_date_exception import ExceptionWithDateException
from tester.exceptions.exception_with_number_exception import ExceptionWithNumberException
from tester.exceptions.exception_with_long_exception import ExceptionWithLongException
from tester.exceptions.exception_with_precision_exception import ExceptionWithPrecisionException
from tester.exceptions.exception_with_rfc_3339_date_time_exception import ExceptionWithRfc3339DateTimeException
from tester.exceptions.unix_time_stamp_exception import UnixTimeStampException
from tester.exceptions.rfc_1123_exception import Rfc1123Exception
from tester.exceptions.send_boolean_in_model_as_exception import SendBooleanInModelAsException
from tester.exceptions.send_rfc_3339_in_model_as_exception import SendRfc3339InModelAsException
from tester.exceptions.send_rfc_1123_in_model_as_exception import SendRfc1123InModelAsException
from tester.exceptions.send_unix_time_stamp_in_model_as_exception import SendUnixTimeStampInModelAsException
from tester.exceptions.send_date_in_model_as_exception import SendDateInModelAsException
from tester.exceptions.send_dynamic_in_model_as_exception import SendDynamicInModelAsException
from tester.exceptions.send_string_in_model_as_exception import SendStringInModelAsException
from tester.exceptions.send_long_in_model_as_exception import SendLongInModelAsException
from tester.exceptions.send_number_in_model_as_exception import SendNumberInModelAsException
from tester.exceptions.send_precision_in_model_as_exception import SendPrecisionInModelAsException
from tester.exceptions.send_uuid_in_model_as_exception import SendUuidInModelAsException
from tester.exceptions.global_test_exception import GlobalTestException


class BaseController(object):

    """All controllers inherit from this base class.

    Attributes:
        config (Configuration): The HttpClient which a specific controller
            instance will use. By default all the controller objects share
            the same HttpClient. A user can use his own custom HttpClient
            as well.
        http_call_back (HttpCallBack): An object which holds call back
            methods to be called before and after the execution of an HttpRequest.
        new_api_call_builder (APICall): Returns the API Call builder instance.

    """


    @staticmethod
    def global_errors():
        return {
            'default': ErrorCase().error_message('Invalid response.').exception_type(GlobalTestException),
            '400': ErrorCase().error_message('400 Global').exception_type(APIException),
            '402': ErrorCase().error_message('402 Global').exception_type(APIException),
            '403': ErrorCase().error_message('403 Global').exception_type(APIException),
            '404': ErrorCase().error_message('404 Global').exception_type(APIException),
            '412': ErrorCase().error_message('Precondition Failed').exception_type(NestedModelException),
            '450': ErrorCase().error_message('caught global exception').exception_type(CustomErrorResponseException),
            '452': ErrorCase().error_message('global exception with string').exception_type(ExceptionWithStringException),
            '453': ErrorCase().error_message('boolean in global exception').exception_type(ExceptionWithBooleanException),
            '454': ErrorCase().error_message('dynamic in global exception').exception_type(ExceptionWithDynamicException),
            '455': ErrorCase().error_message('uuid in global exception').exception_type(ExceptionWithUUIDException),
            '456': ErrorCase().error_message('date in global exception').exception_type(ExceptionWithDateException),
            '457': ErrorCase().error_message('number in global  exception').exception_type(ExceptionWithNumberException),
            '458': ErrorCase().error_message('long in global exception').exception_type(ExceptionWithLongException),
            '459': ErrorCase().error_message('precision in global  exception').exception_type(ExceptionWithPrecisionException),
            '460': ErrorCase().error_message('rfc3339 in global exception').exception_type(ExceptionWithRfc3339DateTimeException),
            '461': ErrorCase().error_message('unix time stamp in global exception').exception_type(UnixTimeStampException),
            '462': ErrorCase().error_message('rfc1123 in global exception').exception_type(Rfc1123Exception),
            '463': ErrorCase().error_message('boolean in model as global exception').exception_type(SendBooleanInModelAsException),
            '464': ErrorCase().error_message('rfc3339 in model as global exception').exception_type(SendRfc3339InModelAsException),
            '465': ErrorCase().error_message('rfc1123 in model as global exception').exception_type(SendRfc1123InModelAsException),
            '466': ErrorCase().error_message('unix time stamp in model as global exception').exception_type(SendUnixTimeStampInModelAsException),
            '467': ErrorCase().error_message('send date in model as global exception').exception_type(SendDateInModelAsException),
            '468': ErrorCase().error_message('send dynamic in model as global exception').exception_type(SendDynamicInModelAsException),
            '469': ErrorCase().error_message('send string in model as global exception').exception_type(SendStringInModelAsException),
            '470': ErrorCase().error_message('send long in model as global exception').exception_type(SendLongInModelAsException),
            '471': ErrorCase().error_message('send number in model as global exception').exception_type(SendNumberInModelAsException),
            '472': ErrorCase().error_message('send precision in model as global exception').exception_type(SendPrecisionInModelAsException),
            '473': ErrorCase().error_message('send uuid in model as global exception').exception_type(SendUuidInModelAsException),
            '500': ErrorCase().error_message('500 Global').exception_type(GlobalTestException),
        }

    def __init__(self, config):
        self._config = config.get_http_client_configuration()
        self._http_call_back = self.config.http_callback
        self.api_call = ApiCall(config)

    @property
    def config(self):
        return self._config

    @property
    def http_call_back(self):
        return self._http_call_back

    @property
    def new_api_call_builder(self):
        return self.api_call.new_builder
