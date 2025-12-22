"""tester.

This file was automatically generated for Stamplay by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

from tester.api_helper import APIHelper
from tester.exceptions.api_exception import (
    APIException,
)


class RFC7807ErrorResponseErrorException(APIException):
    def __init__(self, reason, response):
        """Initialize RFC7807ErrorResponseErrorException object.

        Args:
            reason (string): The reason (or error message) for the Exception
                to be raised.
            response (HttpResponse): The HttpResponse of the API call.

        """
        super(RFC7807ErrorResponseErrorException, self).__init__(reason, response)
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
        self.title =\
            dictionary.get("title")\
            if dictionary.get("title")\
                else None
        self.detail =\
            dictionary.get("detail")\
            if dictionary.get("detail")\
                else None


    def __str__(self):
        """Return a human-readable string representation."""
        _title=(
            self.title
            if hasattr(self, "title")
            else None
        )
        _detail=(
            self.detail
            if hasattr(self, "detail")
            else None
        )
        _base_str = super().__str__()
        _base_str = _base_str[_base_str.find("(") + 1:-1]
        return (
            f"{self.__class__.__name__}("
            f"base_str={_base_str!s}"
            f"title={_title!s}"
            f"detail={_detail!s}"
            f")"
        )
