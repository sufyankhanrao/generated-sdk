# -*- coding: utf-8 -*-

"""
jsonvaluetester

This file was automatically generated for Stamplay by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from jsonvaluetester.api_helper import APIHelper


class SchemaContainer(object):

    """Implementation of the 'SchemaContainer' model.

    Attributes:
        name (str): The model property of type str.
        id (str): The model property of type str.
        schema (dict): The model property of type dict.
        schema_array (List[dict]): The model property of type List[dict].
        schema_map (Dict[str, dict]): The model property of type Dict[str,
            dict].
        additional_properties (Dict[str, object]): The additional properties
            for the model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "id": 'id',
        "name": 'name',
        "schema": 'schema',
        "schema_array": 'schemaArray',
        "schema_map": 'schemaMap'
    }

    _optionals = [
        'schema_array',
        'schema_map',
    ]

    def __init__(self,
                 id=None,
                 name=None,
                 schema=None,
                 schema_array=APIHelper.SKIP,
                 schema_map=APIHelper.SKIP,
                 additional_properties=None):
        """Constructor for the SchemaContainer class"""

        # Initialize members of the class
        self.name = name 
        self.id = id 
        self.schema = schema 
        if schema_array is not APIHelper.SKIP:
            self.schema_array = schema_array 
        if schema_map is not APIHelper.SKIP:
            self.schema_map = schema_map 

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
        schema = dictionary.get("schema") if dictionary.get("schema") else None
        schema_array = dictionary.get("schemaArray") if dictionary.get("schemaArray") else APIHelper.SKIP
        schema_map = dictionary.get("schemaMap") if dictionary.get("schemaMap") else APIHelper.SKIP
        # Clean out expected properties from dictionary
        additional_properties = {k: v for k, v in dictionary.items() if k not in cls._names.values()}
        # Return an object of this model
        return cls(id,
                   name,
                   schema,
                   schema_array,
                   schema_map,
                   additional_properties)

    def __repr__(self):
        return (f'{self.__class__.__name__}('
                f'name={self.name!r}, '
                f'id={self.id!r}, '
                f'schema={self.schema!r}, '
                f'schema_array={(self.schema_array if hasattr(self, "schema_array") else None)!r}, '
                f'schema_map={(self.schema_map if hasattr(self, "schema_map") else None)!r}, '
                f'additional_properties={self.additional_properties!r})')

    def __str__(self):
        return (f'{self.__class__.__name__}('
                f'name={self.name!s}, '
                f'id={self.id!s}, '
                f'schema={self.schema!s}, '
                f'schema_array={(self.schema_array if hasattr(self, "schema_array") else None)!s}, '
                f'schema_map={(self.schema_map if hasattr(self, "schema_map") else None)!s}, '
                f'additional_properties={self.additional_properties!s})')
