# -*- coding: utf-8 -*-

"""
tester

This file was automatically generated for Stamplay by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from tester.api_helper import APIHelper


class Validate(object):

    """Implementation of the 'validate' model.

    Attributes:
        field (str): The model property of type str.
        name (str): The model property of type str.
        address (str): The model property of type str.
        additional_properties (Dict[str, object]): The additional properties
            for the model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "field": 'field',
        "name": 'name',
        "address": 'address'
    }

    _optionals = [
        'address',
    ]

    def __init__(self,
                 field=None,
                 name=None,
                 address=APIHelper.SKIP,
                 additional_properties=None):
        """Constructor for the Validate class"""

        # Initialize members of the class
        self.field = field 
        self.name = name 
        if address is not APIHelper.SKIP:
            self.address = address 

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
        field = dictionary.get("field") if dictionary.get("field") else None
        name = dictionary.get("name") if dictionary.get("name") else None
        address = dictionary.get("address") if dictionary.get("address") else APIHelper.SKIP
        # Clean out expected properties from dictionary
        additional_properties = {k: v for k, v in dictionary.items() if k not in cls._names.values()}
        # Return an object of this model
        return cls(field,
                   name,
                   address,
                   additional_properties)

    def __repr__(self):
        return (f'{self.__class__.__name__}('
                f'field={self.field!r}, '
                f'name={self.name!r}, '
                f'address={(self.address if hasattr(self, "address") else None)!r}, '
                f'additional_properties={self.additional_properties!r})')

    def __str__(self):
        return (f'{self.__class__.__name__}('
                f'field={self.field!s}, '
                f'name={self.name!s}, '
                f'address={(self.address if hasattr(self, "address") else None)!s}, '
                f'additional_properties={self.additional_properties!s})')
