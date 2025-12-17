# -*- coding: utf-8 -*-

"""
tester

This file was automatically generated for Stamplay by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from tester.api_helper import APIHelper


class PrecisionAsOptional(object):

    """Implementation of the 'precision as optional' model.

    Attributes:
        precision (float): The model property of type float.
        additional_properties (Dict[str, object]): The additional properties
            for the model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "precision": 'precision'
    }

    _optionals = [
        'precision',
    ]

    def __init__(self,
                 precision=APIHelper.SKIP,
                 additional_properties=None):
        """Constructor for the PrecisionAsOptional class"""

        # Initialize members of the class
        if precision is not APIHelper.SKIP:
            self.precision = precision 

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
        precision = dictionary.get("precision") if dictionary.get("precision") else APIHelper.SKIP
        # Clean out expected properties from dictionary
        additional_properties = {k: v for k, v in dictionary.items() if k not in cls._names.values()}
        # Return an object of this model
        return cls(precision,
                   additional_properties)

    def __repr__(self):
        return (f'{self.__class__.__name__}('
                f'precision={(self.precision if hasattr(self, "precision") else None)!r}, '
                f'additional_properties={self.additional_properties!r})')

    def __str__(self):
        return (f'{self.__class__.__name__}('
                f'precision={(self.precision if hasattr(self, "precision") else None)!s}, '
                f'additional_properties={self.additional_properties!s})')
