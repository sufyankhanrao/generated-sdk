"""tester.

This file was automatically generated for Stamplay by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

class BaseColor(object):
    """Implementation of the 'BaseColor' model.

    Attributes:
        color (str): The model property of type str.
        additional_properties (Dict[str, object]): The additional properties
            for the model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "color": "color",
    }

    def __init__(self,
                 color=None,
                 additional_properties=None):
        """Initialize a BaseColor instance."""
        # Initialize members of the class
        self.color = color

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
        color = dictionary.get("color") if dictionary.get("color") else None
        # Clean out expected properties from dictionary
        additional_properties =\
            {k: v for k, v in dictionary.items() if k not in cls._names.values()}
        # Return an object of this model
        return cls(color,
                   additional_properties)

    def __repr__(self):
        """Return a unambiguous string representation."""
        return (f"{self.__class__.__name__}("
                f"color={self.color!r}, "
                f"additional_properties={self.additional_properties!r})")

    def __str__(self):
        """Return a human-readable string representation."""
        return (f"{self.__class__.__name__}("
                f"color={self.color!s}, "
                f"additional_properties={self.additional_properties!s})")

class Color(BaseColor):
    """Implementation of the 'Color' model.
    NOTE: This class inherits from 'BaseColor'.

    Attributes:
        alpha (str): The model property of type str.
        additional_properties (Dict[str, object]): The additional properties
            for the model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "alpha": "alpha",
        "color": "color",
    }

    def __init__(self,
                 alpha=None,
                 color=None,
                 additional_properties=None):
        """Initialize a Color instance."""
        # Initialize members of the class
        self.alpha = alpha

        # Call the constructor for the base class
        super(Color, self).__init__(color,
                                    additional_properties)

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
        alpha = dictionary.get("alpha") if dictionary.get("alpha") else None
        color = dictionary.get("color") if dictionary.get("color") else None
        # Clean out expected properties from dictionary
        additional_properties =\
            {k: v for k, v in dictionary.items() if k not in cls._names.values()}
        # Return an object of this model
        return cls(alpha,
                   color,
                   additional_properties)

    def __repr__(self):
        """Return a unambiguous string representation."""
        base_repr = super().__repr__()
        return (f"{self.__class__.__name__}("
                f"{base_repr[base_repr.find('(') + 1:-1]}, "
                f"alpha={self.alpha!r})")

    def __str__(self):
        """Return a human-readable string representation."""
        base_str = super().__str__()
        return (f"{self.__class__.__name__}("
                f"{base_str[base_str.find('(') + 1:-1]}, "
                f"alpha={self.alpha!s})")
