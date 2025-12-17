# -*- coding: utf-8 -*-

"""
tester

This file was automatically generated for Stamplay by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from tester.models.time_to_live import TimeToLive


class Advanced(object):

    """Implementation of the 'Advanced' model.

    Attributes:
        tags (List[str]): The model property of type List[str].
        attachments (int): The model property of type int.
        required_signatures (int): The model property of type int.
        get_social_security_number (bool): The model property of type bool.
        time_to_live (TimeToLive): The model property of type TimeToLive.
        additional_properties (Dict[str, object]): The additional properties
            for the model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "attachments": 'attachments',
        "get_social_security_number": 'getSocialSecurityNumber',
        "required_signatures": 'requiredSignatures',
        "tags": 'tags',
        "time_to_live": 'timeToLive'
    }

    def __init__(self,
                 attachments=None,
                 get_social_security_number=None,
                 required_signatures=None,
                 tags=None,
                 time_to_live=None,
                 additional_properties=None):
        """Constructor for the Advanced class"""

        # Initialize members of the class
        self.tags = tags 
        self.attachments = attachments 
        self.required_signatures = required_signatures 
        self.get_social_security_number = get_social_security_number 
        self.time_to_live = time_to_live 

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
        attachments = dictionary.get("attachments") if dictionary.get("attachments") else None
        get_social_security_number = dictionary.get("getSocialSecurityNumber") if "getSocialSecurityNumber" in dictionary.keys() else None
        required_signatures = dictionary.get("requiredSignatures") if dictionary.get("requiredSignatures") else None
        tags = dictionary.get("tags") if dictionary.get("tags") else None
        time_to_live = TimeToLive.from_dictionary(dictionary.get('timeToLive')) if dictionary.get('timeToLive') else None
        # Clean out expected properties from dictionary
        additional_properties = {k: v for k, v in dictionary.items() if k not in cls._names.values()}
        # Return an object of this model
        return cls(attachments,
                   get_social_security_number,
                   required_signatures,
                   tags,
                   time_to_live,
                   additional_properties)

    def __repr__(self):
        return (f'{self.__class__.__name__}('
                f'tags={self.tags!r}, '
                f'attachments={self.attachments!r}, '
                f'required_signatures={self.required_signatures!r}, '
                f'get_social_security_number={self.get_social_security_number!r}, '
                f'time_to_live={self.time_to_live!r}, '
                f'additional_properties={self.additional_properties!r})')

    def __str__(self):
        return (f'{self.__class__.__name__}('
                f'tags={self.tags!s}, '
                f'attachments={self.attachments!s}, '
                f'required_signatures={self.required_signatures!s}, '
                f'get_social_security_number={self.get_social_security_number!s}, '
                f'time_to_live={self.time_to_live!s}, '
                f'additional_properties={self.additional_properties!s})')
