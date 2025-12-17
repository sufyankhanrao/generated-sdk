# -*- coding: utf-8 -*-

"""
tester

This file was automatically generated for Stamplay by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""


class Attributes(object):

    """Implementation of the 'Attributes' model.

    Attributes:
        exclusive_maximum (bool): The model property of type bool.
        exclusive_minimum (bool): The model property of type bool.
        id (str): The model property of type str.
        additional_properties (Dict[str, object]): The additional properties
            for the model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "exclusive_maximum": 'exclusiveMaximum',
        "exclusive_minimum": 'exclusiveMinimum',
        "id": 'id'
    }

    def __init__(self,
                 exclusive_maximum=None,
                 exclusive_minimum=None,
                 id=None,
                 additional_properties=None):
        """Constructor for the Attributes class"""

        # Initialize members of the class
        self.exclusive_maximum = exclusive_maximum 
        self.exclusive_minimum = exclusive_minimum 
        self.id = id 

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
        exclusive_maximum = dictionary.get("exclusiveMaximum") if "exclusiveMaximum" in dictionary.keys() else None
        exclusive_minimum = dictionary.get("exclusiveMinimum") if "exclusiveMinimum" in dictionary.keys() else None
        id = dictionary.get("id") if dictionary.get("id") else None
        # Clean out expected properties from dictionary
        additional_properties = {k: v for k, v in dictionary.items() if k not in cls._names.values()}
        # Return an object of this model
        return cls(exclusive_maximum,
                   exclusive_minimum,
                   id,
                   additional_properties)

    def __repr__(self):
        return (f'{self.__class__.__name__}('
                f'exclusive_maximum={self.exclusive_maximum!r}, '
                f'exclusive_minimum={self.exclusive_minimum!r}, '
                f'id={self.id!r}, '
                f'additional_properties={self.additional_properties!r})')

    def __str__(self):
        return (f'{self.__class__.__name__}('
                f'exclusive_maximum={self.exclusive_maximum!s}, '
                f'exclusive_minimum={self.exclusive_minimum!s}, '
                f'id={self.id!s}, '
                f'additional_properties={self.additional_properties!s})')
