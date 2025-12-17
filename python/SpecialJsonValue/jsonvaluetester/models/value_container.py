# -*- coding: utf-8 -*-

"""
jsonvaluetester

This file was automatically generated for Stamplay by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from jsonvaluetester.api_helper import APIHelper


class ValueContainer(object):

    """Implementation of the 'ValueContainer' model.

    Attributes:
        name (str): The model property of type str.
        id (str): The model property of type str.
        value (Any): The model property of type Any.
        value_array (List[Any]): The model property of type List[Any].
        value_map (Dict[str, Any]): The model property of type Dict[str, Any].
        additional_properties (Dict[str, object]): The additional properties
            for the model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "id": 'id',
        "name": 'name',
        "value": 'value',
        "value_array": 'valueArray',
        "value_map": 'valueMap'
    }

    _optionals = [
        'value_array',
        'value_map',
    ]

    def __init__(self,
                 id=None,
                 name=None,
                 value=None,
                 value_array=APIHelper.SKIP,
                 value_map=APIHelper.SKIP,
                 additional_properties=None):
        """Constructor for the ValueContainer class"""

        # Initialize members of the class
        self.name = name 
        self.id = id 
        self.value = value 
        if value_array is not APIHelper.SKIP:
            self.value_array = value_array 
        if value_map is not APIHelper.SKIP:
            self.value_map = value_map 

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
        id = dictionary.get("id") if dictionary.get("id") else None
        name = dictionary.get("name") if dictionary.get("name") else None
        value = dictionary.get("value") if dictionary.get("value") else None
        value_array = dictionary.get("valueArray") if dictionary.get("valueArray") else APIHelper.SKIP
        value_map = dictionary.get("valueMap") if dictionary.get("valueMap") else APIHelper.SKIP
        # Clean out expected properties from dictionary
        additional_properties = {k: v for k, v in dictionary.items() if k not in cls._names.values()}
        # Return an object of this model
        return cls(id,
                   name,
                   value,
                   value_array,
                   value_map,
                   additional_properties)

    def __repr__(self):
        return (f'{self.__class__.__name__}('
                f'name={self.name!r}, '
                f'id={self.id!r}, '
                f'value={self.value!r}, '
                f'value_array={(self.value_array if hasattr(self, "value_array") else None)!r}, '
                f'value_map={(self.value_map if hasattr(self, "value_map") else None)!r}, '
                f'additional_properties={self.additional_properties!r})')

    def __str__(self):
        return (f'{self.__class__.__name__}('
                f'name={self.name!s}, '
                f'id={self.id!s}, '
                f'value={self.value!s}, '
                f'value_array={(self.value_array if hasattr(self, "value_array") else None)!s}, '
                f'value_map={(self.value_map if hasattr(self, "value_map") else None)!s}, '
                f'additional_properties={self.additional_properties!s})')
