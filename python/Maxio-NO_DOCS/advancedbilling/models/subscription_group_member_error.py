# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.api_helper import APIHelper


class SubscriptionGroupMemberError(object):

    """Implementation of the 'Subscription Group Member Error' model.

    Attributes:
        id (int): The model property of type int.
        mtype (str): The model property of type str.
        message (str): The model property of type str.
        additional_properties (Dict[str, object]): The additional properties
            for the model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "id": 'id',
        "mtype": 'type',
        "message": 'message'
    }

    _optionals = [
        'id',
        'mtype',
        'message',
    ]

    def __init__(self,
                 id=APIHelper.SKIP,
                 mtype=APIHelper.SKIP,
                 message=APIHelper.SKIP,
                 additional_properties=None):
        """Constructor for the SubscriptionGroupMemberError class"""

        # Initialize members of the class
        if id is not APIHelper.SKIP:
            self.id = id 
        if mtype is not APIHelper.SKIP:
            self.mtype = mtype 
        if message is not APIHelper.SKIP:
            self.message = message 

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
        id = dictionary.get("id") if dictionary.get("id") else APIHelper.SKIP
        mtype = dictionary.get("type") if dictionary.get("type") else APIHelper.SKIP
        message = dictionary.get("message") if dictionary.get("message") else APIHelper.SKIP
        # Clean out expected properties from dictionary
        additional_properties = {k: v for k, v in dictionary.items() if k not in cls._names.values()}
        # Return an object of this model
        return cls(id,
                   mtype,
                   message,
                   additional_properties)

    def __repr__(self):
        return (f'{self.__class__.__name__}('
                f'id={(self.id if hasattr(self, "id") else None)!r}, '
                f'mtype={(self.mtype if hasattr(self, "mtype") else None)!r}, '
                f'message={(self.message if hasattr(self, "message") else None)!r}, '
                f'additional_properties={self.additional_properties!r})')

    def __str__(self):
        return (f'{self.__class__.__name__}('
                f'id={(self.id if hasattr(self, "id") else None)!s}, '
                f'mtype={(self.mtype if hasattr(self, "mtype") else None)!s}, '
                f'message={(self.message if hasattr(self, "message") else None)!s}, '
                f'additional_properties={self.additional_properties!s})')
