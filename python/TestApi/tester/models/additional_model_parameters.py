# -*- coding: utf-8 -*-

"""
tester

This file was automatically generated for Stamplay by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from tester.models.job import Job


class AdditionalModelParameters(object):

    """Implementation of the 'AdditionalModelParameters' model.

    Attributes:
        name (str): The model property of type str.
        field (str): The model property of type str.
        address (str): The model property of type str.
        job (Job): The model property of type Job.
        additional_properties (Dict[str, object]): The additional properties
            for the model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "job": 'Job',
        "address": 'address',
        "field": 'field',
        "name": 'name'
    }

    def __init__(self,
                 job=None,
                 address=None,
                 field=None,
                 name=None,
                 additional_properties=None):
        """Constructor for the AdditionalModelParameters class"""

        # Initialize members of the class
        self.name = name 
        self.field = field 
        self.address = address 
        self.job = job 

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
        job = Job.from_dictionary(dictionary.get('Job')) if dictionary.get('Job') else None
        address = dictionary.get("address") if dictionary.get("address") else None
        field = dictionary.get("field") if dictionary.get("field") else None
        name = dictionary.get("name") if dictionary.get("name") else None
        # Clean out expected properties from dictionary
        additional_properties = {k: v for k, v in dictionary.items() if k not in cls._names.values()}
        # Return an object of this model
        return cls(job,
                   address,
                   field,
                   name,
                   additional_properties)

    def __repr__(self):
        return (f'{self.__class__.__name__}('
                f'name={self.name!r}, '
                f'field={self.field!r}, '
                f'address={self.address!r}, '
                f'job={self.job!r}, '
                f'additional_properties={self.additional_properties!r})')

    def __str__(self):
        return (f'{self.__class__.__name__}('
                f'name={self.name!s}, '
                f'field={self.field!s}, '
                f'address={self.address!s}, '
                f'job={self.job!s}, '
                f'additional_properties={self.additional_properties!s})')
