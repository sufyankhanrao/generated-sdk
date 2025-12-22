"""tester.

This file was automatically generated for Stamplay by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

from tester.models.base_color import Color


class Animal(object):
    """Implementation of the 'Animal' model.

    Attributes:
        name (str): The model property of type str.
        color (Color): The model property of type Color.
        additional_properties (Dict[str, object]): The additional properties for the
            model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "color": "color",
        "name": "name",
    }

    def __init__(
        self,
        color=None,
        name=None,
        additional_properties=None):
        """Initialize a Animal instance."""
        # Initialize members of the class
        self.name = name
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
        color =\
            Color.from_dictionary(
            dictionary.get("color"))\
                if dictionary.get("color") else None
        name =\
            dictionary.get("name")\
            if dictionary.get("name")\
                else None

        # Clean out expected properties from dictionary
        additional_properties =\
            {k: v for k, v in dictionary.items() if k not in cls._names.values()}
        # Return an object of this model
        return cls(color,
                   name,
                   additional_properties)

    def __repr__(self):
        """Return a unambiguous string representation."""
        _name=self.name
        _color=self.color
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"name={_name!r}"
            f"color={_color!r}"
            f"additional_properties={_additional_properties!r}"
            f")"
        )

    def __str__(self):
        """Return a human-readable string representation."""
        _name=self.name
        _color=self.color
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"name={_name!s}"
            f"color={_color!s}"
            f"additional_properties={_additional_properties!s}"
            f")"
        )

class Cat(Animal):
    """Implementation of the 'Cat' model.
    NOTE: This class inherits from 'Animal'.

    Attributes:
        mtype (str): The model property of type str.
        additional_properties (Dict[str, object]): The additional properties for the
            model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "color": "color",
        "name": "name",
        "mtype": "type",
    }

    def __init__(
        self,
        color=None,
        name=None,
        mtype=None,
        additional_properties=None):
        """Initialize a Cat instance."""
        # Initialize members of the class
        self.mtype = mtype

        # Call the constructor for the base class
        super(Cat, self).__init__(
            color,
            name,
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
        color =\
            Color.from_dictionary(
            dictionary.get("color"))\
                if dictionary.get("color") else None
        name =\
            dictionary.get("name")\
            if dictionary.get("name")\
                else None
        mtype =\
            dictionary.get("type")\
            if dictionary.get("type")\
                else None

        # Clean out expected properties from dictionary
        additional_properties =\
            {k: v for k, v in dictionary.items() if k not in cls._names.values()}
        # Return an object of this model
        return cls(color,
                   name,
                   mtype,
                   additional_properties)

    def __repr__(self):
        """Return a unambiguous string representation."""
        _mtype=self.mtype
        _base_repr = super().__repr__()
        _base_repr = _base_repr[_base_repr.find("(") + 1:-1]
        return (
            f"{self.__class__.__name__}("
            f"base_repr={_base_repr!r}"
            f"mtype={_mtype!r}"
            f")"
        )

    def __str__(self):
        """Return a human-readable string representation."""
        _mtype=self.mtype
        _base_str = super().__str__()
        _base_str = _base_str[_base_str.find("(") + 1:-1]
        return (
            f"{self.__class__.__name__}("
            f"base_str={_base_str!s}"
            f"mtype={_mtype!s}"
            f")"
        )
