"""tester.

This file was automatically generated for Stamplay by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

from tester.api_helper import APIHelper
from tester.exceptions.api_exception import (
    APIException,
)


class ExceptionWithStringException(APIException):
    def __init__(self, reason, response):
        """Initialize ExceptionWithStringException object.

        Args:
            reason (string): The reason (or error message) for the Exception
                to be raised.
            response (HttpResponse): The HttpResponse of the API call.

        """
        super(ExceptionWithStringException, self).__init__(reason, response)
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
        self.value =\
            dictionary.get("value")\
            if dictionary.get("value")\
                else None
        self.value_1 =\
            dictionary.get("value1")\
            if dictionary.get("value1")\
                else None


    def __str__(self):
        """Return a human-readable string representation."""
        _value=self.value
        _value_1=(
            self.value_1
            if hasattr(self, "value_1")
            else None
        )
        _base_str = super().__str__()
        _base_str = _base_str[_base_str.find("(") + 1:-1]
        return (
            f"{self.__class__.__name__}("
            f"base_str={_base_str!s}"
            f"value={_value!s}"
            f"value_1={_value_1!s}"
            f")"
        )
