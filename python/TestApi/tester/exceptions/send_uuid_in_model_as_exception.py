"""tester.

This file was automatically generated for Stamplay by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

from tester.api_helper import APIHelper
from tester.exceptions.api_exception import (
    APIException,
)
from tester.models.add_uuid_in_global_exception import (
    AddUuidInGlobalException,
)


class SendUuidInModelAsException(APIException):
    def __init__(self, reason, response):
        """Initialize SendUuidInModelAsException object.

        Args:
            reason (string): The reason (or error message) for the Exception
                to be raised.
            response (HttpResponse): The HttpResponse of the API call.

        """
        super(SendUuidInModelAsException, self).__init__(reason, response)
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
        self.body =\
            AddUuidInGlobalException.from_dictionary(
            dictionary.get("body"))\
                if dictionary.get("body") else None


    def __str__(self):
        """Return a human-readable string representation."""
        _body=self.body
        _base_str = super().__str__()
        _base_str = _base_str[_base_str.find("(") + 1:-1]
        return (
            f"{self.__class__.__name__}("
            f"base_str={_base_str!s}"
            f"body={_body!s}"
            f")"
        )
