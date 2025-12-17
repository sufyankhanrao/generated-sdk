# -*- coding: utf-8 -*-

"""
jsonvaluetester

This file was automatically generated for Stamplay by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from jsonvaluetester.api_helper import APIHelper


class ServerResponse(object):

    """Implementation of the 'ServerResponse' model.

    Attributes:
        passed (bool): The model property of type bool.
        message (str): The model property of type str.
        input (Dict[str, dict]): The model property of type Dict[str, dict].
        nullable_number_map (Dict[str, float]): The model property of type
            Dict[str, float].
        nullable_number_array (List[float]): The model property of type
            List[float].
        additional_properties (Dict[str, object]): The additional properties
            for the model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "passed": 'passed',
        "message": 'Message',
        "input": 'input',
        "nullable_number_array": 'nullableNumberArray',
        "nullable_number_map": 'nullableNumberMap'
    }

    _optionals = [
        'message',
        'input',
        'nullable_number_map',
        'nullable_number_array',
    ]

    def __init__(self,
                 passed=None,
                 message=APIHelper.SKIP,
                 input=APIHelper.SKIP,
                 nullable_number_array=APIHelper.SKIP,
                 nullable_number_map=APIHelper.SKIP,
                 additional_properties=None):
        """Constructor for the ServerResponse class"""

        # Initialize members of the class
        self.passed = passed 
        if message is not APIHelper.SKIP:
            self.message = message 
        if input is not APIHelper.SKIP:
            self.input = input 
        if nullable_number_map is not APIHelper.SKIP:
            self.nullable_number_map = nullable_number_map 
        if nullable_number_array is not APIHelper.SKIP:
            self.nullable_number_array = nullable_number_array 

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
        passed = dictionary.get("passed") if "passed" in dictionary.keys() else None
        message = dictionary.get("Message") if dictionary.get("Message") else APIHelper.SKIP
        input = dictionary.get("input") if dictionary.get("input") else APIHelper.SKIP
        nullable_number_array = dictionary.get("nullableNumberArray") if dictionary.get("nullableNumberArray") else APIHelper.SKIP
        nullable_number_map = dictionary.get("nullableNumberMap") if dictionary.get("nullableNumberMap") else APIHelper.SKIP
        # Clean out expected properties from dictionary
        additional_properties = {k: v for k, v in dictionary.items() if k not in cls._names.values()}
        # Return an object of this model
        return cls(passed,
                   message,
                   input,
                   nullable_number_array,
                   nullable_number_map,
                   additional_properties)

    def __repr__(self):
        return (f'{self.__class__.__name__}('
                f'passed={self.passed!r}, '
                f'message={(self.message if hasattr(self, "message") else None)!r}, '
                f'input={(self.input if hasattr(self, "input") else None)!r}, '
                f'nullable_number_map={(self.nullable_number_map if hasattr(self, "nullable_number_map") else None)!r}, '
                f'nullable_number_array={(self.nullable_number_array if hasattr(self, "nullable_number_array") else None)!r}, '
                f'additional_properties={self.additional_properties!r})')

    def __str__(self):
        return (f'{self.__class__.__name__}('
                f'passed={self.passed!s}, '
                f'message={(self.message if hasattr(self, "message") else None)!s}, '
                f'input={(self.input if hasattr(self, "input") else None)!s}, '
                f'nullable_number_map={(self.nullable_number_map if hasattr(self, "nullable_number_map") else None)!s}, '
                f'nullable_number_array={(self.nullable_number_array if hasattr(self, "nullable_number_array") else None)!s}, '
                f'additional_properties={self.additional_properties!s})')
