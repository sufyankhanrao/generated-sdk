# -*- coding: utf-8 -*-

"""
tester

This file was automatically generated for Stamplay by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""


class Imaging(object):

    """Implementation of the 'Imaging' model.

    Attributes:
        name (str): The model property of type str.
        time (str): The model property of type str.
        location (str): The model property of type str.
        additional_properties (Dict[str, object]): The additional properties
            for the model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "location": 'location',
        "name": 'name',
        "time": 'time'
    }

    def __init__(self,
                 location=None,
                 name=None,
                 time=None,
                 additional_properties=None):
        """Constructor for the Imaging class"""

        # Initialize members of the class
        self.name = name 
        self.time = time 
        self.location = location 

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
        location = dictionary.get("location") if dictionary.get("location") else None
        name = dictionary.get("name") if dictionary.get("name") else None
        time = dictionary.get("time") if dictionary.get("time") else None
        # Clean out expected properties from dictionary
        additional_properties = {k: v for k, v in dictionary.items() if k not in cls._names.values()}
        # Return an object of this model
        return cls(location,
                   name,
                   time,
                   additional_properties)

    def __repr__(self):
        return (f'{self.__class__.__name__}('
                f'name={self.name!r}, '
                f'time={self.time!r}, '
                f'location={self.location!r}, '
                f'additional_properties={self.additional_properties!r})')

    def __str__(self):
        return (f'{self.__class__.__name__}('
                f'name={self.name!s}, '
                f'time={self.time!s}, '
                f'location={self.location!s}, '
                f'additional_properties={self.additional_properties!s})')
