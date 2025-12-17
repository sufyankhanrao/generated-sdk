# -*- coding: utf-8 -*-

"""
tester

This file was automatically generated for Stamplay by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

from tester.api_helper import APIHelper
from tester.exceptions.api_exception import APIException


class ExceptionWithRfc3339DateTimeException(APIException):
    def __init__(self, reason, response):
        """Constructor for the ExceptionWithRfc3339DateTimeException class

        Args:
            reason (string): The reason (or error message) for the Exception
                to be raised.
            response (HttpResponse): The HttpResponse of the API call.

        """
        super(ExceptionWithRfc3339DateTimeException, self).__init__(reason, response)
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
        self.date_time = APIHelper.RFC3339DateTime.from_value(dictionary.get("dateTime")).datetime if dictionary.get("dateTime") else None
        self.date_time_1 = APIHelper.RFC3339DateTime.from_value(dictionary.get("dateTime1")).datetime if dictionary.get("dateTime1") else None

    def __str__(self):
        base_str = super().__str__()
        return (f'{self.__class__.__name__}('
                f'{base_str[base_str.find("(") + 1:-1]}, '
                f'date_time={self.date_time!s}, '
                f'date_time_1={(self.date_time_1 if hasattr(self, "date_time_1") else None)!s})')
