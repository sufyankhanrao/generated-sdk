"""tester.

This file was automatically generated for Stamplay by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

from tester.api_helper import APIHelper


class UuidAsOptional(object):
    """Implementation of the 'uuid as optional' model.

    Attributes:
        uuid (uuid|str): The model property of type uuid|str.
        additional_properties (Dict[str, object]): The additional properties
            for the model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "uuid": "uuid",
    }

    _optionals = [
        "uuid",
    ]

    def __init__(self,
                 uuid=APIHelper.SKIP,
                 additional_properties=None):
        """Initialize a UuidAsOptional instance."""
        # Initialize members of the class
        if uuid is not APIHelper.SKIP:
            self.uuid = uuid

        # Add additional model properties to the instance
        if additional_properties is None:
            additional_properties = {}
        self.additional_properties = additional_properties

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
        uuid =\
            dictionary.get("uuid")\
            if dictionary.get("uuid") else APIHelper.SKIP
        # Clean out expected properties from dictionary
        additional_properties =\
            {k: v for k, v in dictionary.items() if k not in cls._names.values()}
        # Return an object of this model
        return cls(uuid,
                   additional_properties)

    def __repr__(self):
        """Return a unambiguous string representation."""
        return (f"{self.__class__.__name__}("
                f"uuid={(self.uuid if hasattr(self, 'uuid') else None)!r}, "
                f"additional_properties={self.additional_properties!r})")

    def __str__(self):
        """Return a human-readable string representation."""
        return (f"{self.__class__.__name__}("
                f"uuid={(self.uuid if hasattr(self, 'uuid') else None)!s}, "
                f"additional_properties={self.additional_properties!s})")
