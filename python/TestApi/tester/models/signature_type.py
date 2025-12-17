# -*- coding: utf-8 -*-

"""
tester

This file was automatically generated for Stamplay by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""


class SignatureType(object):

    """Implementation of the 'SignatureType' model.

    Attributes:
        mechanism (str): The model property of type str.
        on_eaccept_use_hand_written_signature (bool): The model property of
            type bool.
        additional_properties (Dict[str, object]): The additional properties
            for the model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "mechanism": 'mechanism',
        "on_eaccept_use_hand_written_signature": 'onEacceptUseHandWrittenSignature'
    }

    def __init__(self,
                 mechanism=None,
                 on_eaccept_use_hand_written_signature=None,
                 additional_properties=None):
        """Constructor for the SignatureType class"""

        # Initialize members of the class
        self.mechanism = mechanism 
        self.on_eaccept_use_hand_written_signature = on_eaccept_use_hand_written_signature 

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
        mechanism = dictionary.get("mechanism") if dictionary.get("mechanism") else None
        on_eaccept_use_hand_written_signature = dictionary.get("onEacceptUseHandWrittenSignature") if "onEacceptUseHandWrittenSignature" in dictionary.keys() else None
        # Clean out expected properties from dictionary
        additional_properties = {k: v for k, v in dictionary.items() if k not in cls._names.values()}
        # Return an object of this model
        return cls(mechanism,
                   on_eaccept_use_hand_written_signature,
                   additional_properties)

    def __repr__(self):
        return (f'{self.__class__.__name__}('
                f'mechanism={self.mechanism!r}, '
                f'on_eaccept_use_hand_written_signature={self.on_eaccept_use_hand_written_signature!r}, '
                f'additional_properties={self.additional_properties!r})')

    def __str__(self):
        return (f'{self.__class__.__name__}('
                f'mechanism={self.mechanism!s}, '
                f'on_eaccept_use_hand_written_signature={self.on_eaccept_use_hand_written_signature!s}, '
                f'additional_properties={self.additional_properties!s})')
