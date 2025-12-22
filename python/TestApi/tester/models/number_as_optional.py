"""tester.

This file was automatically generated for Stamplay by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

from tester.api_helper import APIHelper


class NumberAsOptional(object):
    """Implementation of the 'number as optional' model.

    Attributes:
        number (int): The model property of type int.
        additional_properties (Dict[str, object]): The additional properties for the
            model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "number": "number",
    }

    _optionals = [
        "number",
    ]

    def __init__(
        self,
        number=APIHelper.SKIP,
        additional_properties=None):
        """Initialize a NumberAsOptional instance."""
        # Initialize members of the class
        if number is not APIHelper.SKIP:
            self.number = number

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
        number =\
            dictionary.get("number")\
            if dictionary.get("number")\
                else APIHelper.SKIP

        # Clean out expected properties from dictionary
        additional_properties =\
            {k: v for k, v in dictionary.items() if k not in cls._names.values()}
        # Return an object of this model
        return cls(number,
                   additional_properties)

    def __repr__(self):
        """Return a unambiguous string representation."""
        _number=(
            self.number
            if hasattr(self, "number")
            else None
        )
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"number={_number!r}"
            f"additional_properties={_additional_properties!r}"
            f")"
        )

    def __str__(self):
        """Return a human-readable string representation."""
        _number=(
            self.number
            if hasattr(self, "number")
            else None
        )
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"number={_number!s}"
            f"additional_properties={_additional_properties!s}"
            f")"
        )
