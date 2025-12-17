# -*- coding: utf-8 -*-

"""
tester

This file was automatically generated for Stamplay by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""


class Styling(object):

    """Implementation of the 'Styling' model.

    Attributes:
        color_theme (str): The model property of type str.
        spinner (str): The model property of type str.
        additional_properties (Dict[str, object]): The additional properties
            for the model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "color_theme": 'colorTheme',
        "spinner": 'spinner'
    }

    def __init__(self,
                 color_theme=None,
                 spinner=None,
                 additional_properties=None):
        """Constructor for the Styling class"""

        # Initialize members of the class
        self.color_theme = color_theme 
        self.spinner = spinner 

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
        color_theme = dictionary.get("colorTheme") if dictionary.get("colorTheme") else None
        spinner = dictionary.get("spinner") if dictionary.get("spinner") else None
        # Clean out expected properties from dictionary
        additional_properties = {k: v for k, v in dictionary.items() if k not in cls._names.values()}
        # Return an object of this model
        return cls(color_theme,
                   spinner,
                   additional_properties)

    def __repr__(self):
        return (f'{self.__class__.__name__}('
                f'color_theme={self.color_theme!r}, '
                f'spinner={self.spinner!r}, '
                f'additional_properties={self.additional_properties!r})')

    def __str__(self):
        return (f'{self.__class__.__name__}('
                f'color_theme={self.color_theme!s}, '
                f'spinner={self.spinner!s}, '
                f'additional_properties={self.additional_properties!s})')
