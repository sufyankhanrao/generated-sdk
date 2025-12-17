"""postnlecommerce.

This file was automatically generated for PostNL by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

from postnlecommerce.api_helper import APIHelper
from postnlecommerce.exceptions.api_exception import (
    APIException,
)
from postnlecommerce.models.error_3 import Error3


class LabellingResponseInvalidException(APIException):
    def __init__(self, reason, response):
        """Initialize LabellingResponseInvalidException object.

        Args:
            reason (string): The reason (or error message) for the Exception
                to be raised.
            response (HttpResponse): The HttpResponse of the API call.

        """
        super(LabellingResponseInvalidException, self).__init__(reason, response)
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
        self.errors = None
        if dictionary.get("Errors") is not None:
            self.errors = [
                Error3.from_dictionary(x)
                    for x in dictionary.get("Errors")
            ]
        else:
            self.errors = None

    def __str__(self):
        """Return a human-readable string representation."""
        base_str = super().__str__()
        return (f"{self.__class__.__name__}("
                f"{base_str[base_str.find('(') + 1:-1]}, "
                f"errors={(self.errors if hasattr(self, 'errors') else None)!s})")
