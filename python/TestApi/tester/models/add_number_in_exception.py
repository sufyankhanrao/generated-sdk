"""tester.

This file was automatically generated for Stamplay by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

from tester.api_helper import APIHelper


class AddNumberInException(object):
    """Implementation of the 'Add number in exception' model.

    Attributes:
        value (int): The model property of type int.
        value_1 (int): The model property of type int.
        additional_properties (Dict[str, object]): The additional properties for the
            model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "value": "value",
        "value_1": "value1",
    }

    _optionals = [
        "value_1",
    ]

    def __init__(
        self,
        value=None,
        value_1=APIHelper.SKIP,
        additional_properties=None):
        """Initialize a AddNumberInException instance."""
        # Initialize members of the class
        self.value = value
        if value_1 is not APIHelper.SKIP:
            self.value_1 = value_1

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
        value =\
            dictionary.get("value")\
            if dictionary.get("value")\
                else None
        value_1 =\
            dictionary.get("value1")\
            if dictionary.get("value1")\
                else APIHelper.SKIP

        # Clean out expected properties from dictionary
        additional_properties =\
            {k: v for k, v in dictionary.items() if k not in cls._names.values()}
        # Return an object of this model
        return cls(value,
                   value_1,
                   additional_properties)

    def __repr__(self):
        """Return a unambiguous string representation."""
        _value=self.value
        _value_1=(
            self.value_1
            if hasattr(self, "value_1")
            else None
        )
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"value={_value!r}"
            f"value_1={_value_1!r}"
            f"additional_properties={_additional_properties!r}"
            f")"
        )

    def __str__(self):
        """Return a human-readable string representation."""
        _value=self.value
        _value_1=(
            self.value_1
            if hasattr(self, "value_1")
            else None
        )
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"value={_value!s}"
            f"value_1={_value_1!s}"
            f"additional_properties={_additional_properties!s}"
            f")"
        )
