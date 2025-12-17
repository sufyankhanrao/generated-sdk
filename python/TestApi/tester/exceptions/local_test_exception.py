# -*- coding: utf-8 -*-

"""
tester

This file was automatically generated for Stamplay by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

from tester.api_helper import APIHelper
from tester.exceptions.global_test_exception import GlobalTestException


class LocalTestException(GlobalTestException):
    def __init__(self, reason, response):
        """Constructor for the LocalTestException class

        Args:
            reason (string): The reason (or error message) for the Exception
                to be raised.
            response (HttpResponse): The HttpResponse of the API call.

        """
        super(LocalTestException, self).__init__(reason, response)
        dictionary = APIHelper.json_deserialize(self.response.text)
        if isinstance(dictionary, dict):
            self.unbox(dictionary)

    def unbox(self, dictionary):
        """Populates the properties of this object by extracting them from a dictionary.

        Args:
            dictionary (dictionary): A dictionary representation of the object as
            obtained from the deserialization of the server's response. The keys
            MUST match property names in the API description.

        """
        super(LocalTestException, self).unbox(dictionary)
        self.secret_message_for_endpoint = dictionary.get("SecretMessageForEndpoint") if dictionary.get("SecretMessageForEndpoint") else None
        self.error_days = dictionary.get("errorDays") if dictionary.get("errorDays") else 'Friday'

    def __str__(self):
        base_str = super().__str__()
        return (f'{self.__class__.__name__}('
                f'{base_str[base_str.find("(") + 1:-1]}, '
                f'secret_message_for_endpoint={self.secret_message_for_endpoint!s}, '
                f'error_days={(self.error_days if hasattr(self, "error_days") else None)!s})')
