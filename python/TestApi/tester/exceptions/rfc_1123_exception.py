"""tester.

This file was automatically generated for Stamplay by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

from tester.api_helper import APIHelper
from tester.exceptions.api_exception import (
    APIException,
)


class Rfc1123Exception(APIException):
    def __init__(self, reason, response):
        """Initialize Rfc1123Exception object.

        Args:
            reason (string): The reason (or error message) for the Exception
                to be raised.
            response (HttpResponse): The HttpResponse of the API call.

        """
        super(Rfc1123Exception, self).__init__(reason, response)
        dictionary = APIHelper.json_deserialize(self.response.text)
        if isinstance(dictionary, dict):
            self.unbox(dictionary)

    def unbox(self, dictionary):
        """Populate the properties of this object by extracting them from a dictionary.

        Args:
            dictionary (dictionary): A dictionary representation of the object as
            obtained from the deserialization of the server's response. The keys
            MUST match property names in the API description.

        """
        self.date_time = APIHelper.HttpDateTime.from_value(
            dictionary.get("dateTime")).datetime\
            if dictionary.get("dateTime") else None
        self.date_time_1 = APIHelper.HttpDateTime.from_value(
            dictionary.get("dateTime1")).datetime\
            if dictionary.get("dateTime1") else None


    def __str__(self):
        """Return a human-readable string representation."""
        _date_time=self.date_time
        _date_time_1=(
            self.date_time_1
            if hasattr(self, "date_time_1")
            else None
        )
        _base_str = super().__str__()
        _base_str = _base_str[_base_str.find("(") + 1:-1]
        return (
            f"{self.__class__.__name__}("
            f"base_str={_base_str!s}"
            f"date_time={_date_time!s}"
            f"date_time_1={_date_time_1!s}"
            f")"
        )
