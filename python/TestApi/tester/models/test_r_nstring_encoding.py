"""tester.

This file was automatically generated for Stamplay by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

class TestRNstringEncoding(object):
    """Implementation of the 'test\r\nstringEncoding' model.

    Attributes:
        field (str): The model property of type str.
        name (str): The model property of type str.
        additional_properties (Dict[str, object]): The additional properties
            for the model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "field": "field",
        "name": "name",
    }

    def __init__(self,
                 field=None,
                 name=None,
                 additional_properties=None):
        """Initialize a TestRNstringEncoding instance."""
        # Initialize members of the class
        self.field = field
        self.name = name

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
        field = dictionary.get("field") if dictionary.get("field") else None
        name = dictionary.get("name") if dictionary.get("name") else None
        # Clean out expected properties from dictionary
        additional_properties =\
            {k: v for k, v in dictionary.items() if k not in cls._names.values()}
        # Return an object of this model
        return cls(field,
                   name,
                   additional_properties)

    def __repr__(self):
        """Return a unambiguous string representation."""
        return (f"{self.__class__.__name__}("
                f"field={self.field!r}, "
                f"name={self.name!r}, "
                f"additional_properties={self.additional_properties!r})")

    def __str__(self):
        """Return a human-readable string representation."""
        return (f"{self.__class__.__name__}("
                f"field={self.field!s}, "
                f"name={self.name!s}, "
                f"additional_properties={self.additional_properties!s})")
