"""postnlecommerce.

This file was automatically generated for PostNL by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

from postnlecommerce.api_helper import APIHelper
from postnlecommerce.models.location_1 import (
    Location1,
)


class GetLocationsResult1(object):
    """Implementation of the 'GetLocationsResult1' model.

    Attributes:
        response_location (Location1): The model property of type Location1.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "response_location": "ResponseLocation",
    }

    _optionals = [
        "response_location",
    ]

    def __init__(self,
                 response_location=APIHelper.SKIP):
        """Initialize a GetLocationsResult1 instance."""
        # Initialize members of the class
        if response_location is not APIHelper.SKIP:
            self.response_location = response_location

    @classmethod
    def from_dictionary(cls,
                        dictionary):
        """Create an instance of this model from a dictionary

        Args:
            dictionary (dictionary): A dictionary representation of the object
            as obtained from the deserialization of the server's response. The
            keys MUST match property names in the API description.

        Returns:
            object: An instance of this structure class.

        """
        if not isinstance(dictionary, dict) or dictionary is None:
            return None

        # Extract variables from the dictionary
        response_location = Location1.from_dictionary(
            dictionary.get("ResponseLocation"))\
            if "ResponseLocation" in dictionary.keys() else APIHelper.SKIP
        # Return an object of this model
        return cls(response_location)

    def __repr__(self):
        """Return a unambiguous string representation."""
        return (f"{self.__class__.__name__}("
                f"response_location={(self.response_location
                     if hasattr(self, 'response_location') else None)!r})")

    def __str__(self):
        """Return a human-readable string representation."""
        return (f"{self.__class__.__name__}("
                f"response_location={(self.response_location
                     if hasattr(self, 'response_location') else None)!s})")
