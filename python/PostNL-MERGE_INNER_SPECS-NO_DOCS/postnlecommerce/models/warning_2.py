"""postnlecommerce.

This file was automatically generated for PostNL by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

from postnlecommerce.api_helper import APIHelper


class Warning2(object):
    """Implementation of the 'Warning2' model.

    Attributes:
        message (str): The warning message
        code (str): The warning code

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "message": "Message",
        "code": "Code",
    }

    _optionals = [
        "message",
        "code",
    ]

    def __init__(self,
                 message=APIHelper.SKIP,
                 code=APIHelper.SKIP):
        """Initialize a Warning2 instance."""
        # Initialize members of the class
        if message is not APIHelper.SKIP:
            self.message = message
        if code is not APIHelper.SKIP:
            self.code = code

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
        message =\
            dictionary.get("Message")\
            if dictionary.get("Message") else APIHelper.SKIP
        code =\
            dictionary.get("Code")\
            if dictionary.get("Code") else APIHelper.SKIP
        # Return an object of this model
        return cls(message,
                   code)

    def __repr__(self):
        """Return a unambiguous string representation."""
        return (f"{self.__class__.__name__}("
                f"message={(self.message
                     if hasattr(self, 'message') else None)!r}, "
                f"code={(self.code if hasattr(self, 'code') else None)!r})")

    def __str__(self):
        """Return a human-readable string representation."""
        return (f"{self.__class__.__name__}("
                f"message={(self.message
                     if hasattr(self, 'message') else None)!s}, "
                f"code={(self.code if hasattr(self, 'code') else None)!s})")
