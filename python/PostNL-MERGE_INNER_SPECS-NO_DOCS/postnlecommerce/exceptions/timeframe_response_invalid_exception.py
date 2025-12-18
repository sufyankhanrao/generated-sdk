# -*- coding: utf-8 -*-

"""
postnlecommerce

This file was automatically generated for PostNL by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

from postnlecommerce.api_helper import APIHelper
from postnlecommerce.exceptions.api_exception import APIException
from postnlecommerce.models.error_1 import Error1


class TimeframeResponseInvalidException(APIException):
    def __init__(self, reason, response):
        """Constructor for the TimeframeResponseInvalidException class

        Args:
            reason (string): The reason (or error message) for the Exception
                to be raised.
            response (HttpResponse): The HttpResponse of the API call.

        """
        super(TimeframeResponseInvalidException, self).__init__(reason, response)
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
        self.date = APIHelper.RFC3339DateTime.from_value(dictionary.get("Date")).datetime if dictionary.get("Date") else None
        self.error = Error1.from_dictionary(dictionary.get('Error')) if 'Error' in dictionary.keys() else None
        self.request_id = dictionary.get("RequestId") if dictionary.get("RequestId") else None

    def __str__(self):
        base_str = super().__str__()
        return (f'{self.__class__.__name__}('
                f'{base_str[base_str.find("(") + 1:-1]}, '
                f'date={(self.date if hasattr(self, "date") else None)!s}, '
                f'error={(self.error if hasattr(self, "error") else None)!s}, '
                f'request_id={(self.request_id if hasattr(self, "request_id") else None)!s})')
