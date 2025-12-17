# -*- coding: utf-8 -*-

"""
tester

This file was automatically generated for Stamplay by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from tester.api_helper import APIHelper


class AddUuidInGlobalException(object):

    """Implementation of the 'Add uuid in global exception' model.

    Attributes:
        value (uuid|str): The model property of type uuid|str.
        value_1 (uuid|str): The model property of type uuid|str.
        additional_properties (Dict[str, object]): The additional properties
            for the model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "value": 'value',
        "value_1": 'value1'
    }

    _optionals = [
        'value_1',
    ]

    def __init__(self,
                 value=None,
                 value_1=APIHelper.SKIP,
                 additional_properties=None):
        """Constructor for the AddUuidInGlobalException class"""

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
        value = dictionary.get("value") if dictionary.get("value") else None
        value_1 = dictionary.get("value1") if dictionary.get("value1") else APIHelper.SKIP
        # Clean out expected properties from dictionary
        additional_properties = {k: v for k, v in dictionary.items() if k not in cls._names.values()}
        # Return an object of this model
        return cls(value,
                   value_1,
                   additional_properties)

    def __repr__(self):
        return (f'{self.__class__.__name__}('
                f'value={self.value!r}, '
                f'value_1={(self.value_1 if hasattr(self, "value_1") else None)!r}, '
                f'additional_properties={self.additional_properties!r})')

    def __str__(self):
        return (f'{self.__class__.__name__}('
                f'value={self.value!s}, '
                f'value_1={(self.value_1 if hasattr(self, "value_1") else None)!s}, '
                f'additional_properties={self.additional_properties!s})')
