# -*- coding: utf-8 -*-

"""
tester

This file was automatically generated for Stamplay by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from tester.models.inner_complex_type import InnerComplexType


class ComplexType(object):

    """Implementation of the 'ComplexType' model.

    Attributes:
        number_list_type (List[int]): The model property of type List[int].
        number_map_type (Dict[str, int]): The model property of type Dict[str,
            int].
        inner_complex_type (InnerComplexType): The model property of type
            InnerComplexType.
        inner_complex_list_type (List[InnerComplexType]): The model property
            of type List[InnerComplexType].
        additional_properties (Dict[str, object]): The additional properties
            for the model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "inner_complex_list_type": 'innerComplexListType',
        "inner_complex_type": 'innerComplexType',
        "number_list_type": 'numberListType',
        "number_map_type": 'numberMapType'
    }

    def __init__(self,
                 inner_complex_list_type=None,
                 inner_complex_type=None,
                 number_list_type=None,
                 number_map_type=None,
                 additional_properties=None):
        """Constructor for the ComplexType class"""

        # Initialize members of the class
        self.number_list_type = number_list_type 
        self.number_map_type = number_map_type 
        self.inner_complex_type = inner_complex_type 
        self.inner_complex_list_type = inner_complex_list_type 

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
        inner_complex_list_type = None
        if dictionary.get('innerComplexListType') is not None:
            inner_complex_list_type = [InnerComplexType.from_dictionary(x) for x in dictionary.get('innerComplexListType')]
        inner_complex_type = InnerComplexType.from_dictionary(dictionary.get('innerComplexType')) if dictionary.get('innerComplexType') else None
        number_list_type = dictionary.get("numberListType") if dictionary.get("numberListType") else None
        number_map_type = dictionary.get("numberMapType") if dictionary.get("numberMapType") else None
        # Clean out expected properties from dictionary
        additional_properties = {k: v for k, v in dictionary.items() if k not in cls._names.values()}
        # Return an object of this model
        return cls(inner_complex_list_type,
                   inner_complex_type,
                   number_list_type,
                   number_map_type,
                   additional_properties)

    def __repr__(self):
        return (f'{self.__class__.__name__}('
                f'number_list_type={self.number_list_type!r}, '
                f'number_map_type={self.number_map_type!r}, '
                f'inner_complex_type={self.inner_complex_type!r}, '
                f'inner_complex_list_type={self.inner_complex_list_type!r}, '
                f'additional_properties={self.additional_properties!r})')

    def __str__(self):
        return (f'{self.__class__.__name__}('
                f'number_list_type={self.number_list_type!s}, '
                f'number_map_type={self.number_map_type!s}, '
                f'inner_complex_type={self.inner_complex_type!s}, '
                f'inner_complex_list_type={self.inner_complex_list_type!s}, '
                f'additional_properties={self.additional_properties!s})')
