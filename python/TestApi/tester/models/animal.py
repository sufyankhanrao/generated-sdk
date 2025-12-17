# -*- coding: utf-8 -*-

"""
tester

This file was automatically generated for Stamplay by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from tester.models.base_color import Color


class Animal(object):

    """Implementation of the 'Animal' model.

    Attributes:
        name (str): The model property of type str.
        color (Color): The model property of type Color.
        additional_properties (Dict[str, object]): The additional properties
            for the model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "color": 'color',
        "name": 'name'
    }

    def __init__(self,
                 color=None,
                 name=None,
                 additional_properties=None):
        """Constructor for the Animal class"""

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
        """Creates an instance of this model from a dictionary

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
        color = Color.from_dictionary(dictionary.get('color')) if dictionary.get('color') else None
        name = dictionary.get("name") if dictionary.get("name") else None
        # Clean out expected properties from dictionary
        additional_properties = {k: v for k, v in dictionary.items() if k not in cls._names.values()}
        # Return an object of this model
        return cls(color,
                   name,
                   additional_properties)

    def __repr__(self):
        return (f'{self.__class__.__name__}('
                f'name={self.name!r}, '
                f'color={self.color!r}, '
                f'additional_properties={self.additional_properties!r})')

    def __str__(self):
        return (f'{self.__class__.__name__}('
                f'name={self.name!s}, '
                f'color={self.color!s}, '
                f'additional_properties={self.additional_properties!s})')

class Cat(Animal):

    """Implementation of the 'Cat' model.
    NOTE: This class inherits from 'Animal'.

    Attributes:
        mtype (str): The model property of type str.
        additional_properties (Dict[str, object]): The additional properties
            for the model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "color": 'color',
        "name": 'name',
        "mtype": 'type'
    }

    def __init__(self,
                 color=None,
                 name=None,
                 mtype=None,
                 additional_properties=None):
        """Constructor for the Cat class"""

        # Initialize members of the class
        self.mtype = mtype 

        # Call the constructor for the base class
        super(Cat, self).__init__(color,
                                  name,
                                  additional_properties)

    @classmethod
    def from_dictionary(cls,
                        dictionary):
        """Creates an instance of this model from a dictionary

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
        color = Color.from_dictionary(dictionary.get('color')) if dictionary.get('color') else None
        name = dictionary.get("name") if dictionary.get("name") else None
        mtype = dictionary.get("type") if dictionary.get("type") else None
        # Clean out expected properties from dictionary
        additional_properties = {k: v for k, v in dictionary.items() if k not in cls._names.values()}
        # Return an object of this model
        return cls(color,
                   name,
                   mtype,
                   additional_properties)

    def __repr__(self):
        base_repr = super().__repr__()
        return (f'{self.__class__.__name__}('
                f'{base_repr[base_repr.find("(") + 1:-1]}, '
                f'mtype={self.mtype!r})')

    def __str__(self):
        base_str = super().__str__()
        return (f'{self.__class__.__name__}('
                f'{base_str[base_str.find("(") + 1:-1]}, '
                f'mtype={self.mtype!s})')
