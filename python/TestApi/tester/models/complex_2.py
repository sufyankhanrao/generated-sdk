# -*- coding: utf-8 -*-

"""
tester

This file was automatically generated for Stamplay by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from tester.models.glossary import Glossary


class Complex2(object):

    """Implementation of the 'complex2' model.

    Attributes:
        glossary (Glossary): The model property of type Glossary.
        additional_properties (Dict[str, object]): The additional properties
            for the model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "glossary": 'glossary'
    }

    def __init__(self,
                 glossary=None,
                 additional_properties=None):
        """Constructor for the Complex2 class"""

        # Initialize members of the class
        self.glossary = glossary 

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
        glossary = Glossary.from_dictionary(dictionary.get('glossary')) if dictionary.get('glossary') else None
        # Clean out expected properties from dictionary
        additional_properties = {k: v for k, v in dictionary.items() if k not in cls._names.values()}
        # Return an object of this model
        return cls(glossary,
                   additional_properties)

    def __repr__(self):
        return (f'{self.__class__.__name__}('
                f'glossary={self.glossary!r}, '
                f'additional_properties={self.additional_properties!r})')

    def __str__(self):
        return (f'{self.__class__.__name__}('
                f'glossary={self.glossary!s}, '
                f'additional_properties={self.additional_properties!s})')
