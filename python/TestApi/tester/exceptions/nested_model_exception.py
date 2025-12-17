"""tester.

This file was automatically generated for Stamplay by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

from tester.api_helper import APIHelper
from tester.exceptions.api_exception import (
    APIException,
)
from tester.models.validate import Validate


class NestedModelException(APIException):
    def __init__(self, reason, response):
        """Initialize NestedModelException object.

        Args:
            reason (string): The reason (or error message) for the Exception
                to be raised.
            response (HttpResponse): The HttpResponse of the API call.

        """
        super(NestedModelException, self).__init__(reason, response)
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
        self.server_message =\
            dictionary.get("ServerMessage")\
            if dictionary.get("ServerMessage") else None
        self.server_code =\
            dictionary.get("ServerCode")\
            if dictionary.get("ServerCode") else None
        self.model = Validate.from_dictionary(
            dictionary.get("model"))\
            if dictionary.get("model") else None

    def __str__(self):
        """Return a human-readable string representation."""
        base_str = super().__str__()
        return (f"{self.__class__.__name__}("
                f"{base_str[base_str.find('(') + 1:-1]}, "
                f"server_message={self.server_message!s}, "
                f"server_code={self.server_code!s}, "
                f"model={self.model!s})")
