# -*- coding: utf-8 -*-

"""
tester

This file was automatically generated for Stamplay by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from tester.models.ace_inhibitor import AceInhibitor
from tester.models.antianginal import Antianginal
from tester.models.anticoagulant import Anticoagulant
from tester.models.beta_blocker import BetaBlocker
from tester.models.diuretic import Diuretic
from tester.models.mineral import Mineral


class Medication(object):

    """Implementation of the 'Medication' model.

    Attributes:
        ace_inhibitors (List[AceInhibitor]): The model property of type
            List[AceInhibitor].
        antianginal (List[Antianginal]): The model property of type
            List[Antianginal].
        anticoagulants (List[Anticoagulant]): The model property of type
            List[Anticoagulant].
        beta_blocker (List[BetaBlocker]): The model property of type
            List[BetaBlocker].
        diuretic (List[Diuretic]): The model property of type List[Diuretic].
        mineral (List[Mineral]): The model property of type List[Mineral].
        additional_properties (Dict[str, object]): The additional properties
            for the model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "ace_inhibitors": 'aceInhibitors',
        "antianginal": 'antianginal',
        "anticoagulants": 'anticoagulants',
        "beta_blocker": 'betaBlocker',
        "diuretic": 'diuretic',
        "mineral": 'mineral'
    }

    def __init__(self,
                 ace_inhibitors=None,
                 antianginal=None,
                 anticoagulants=None,
                 beta_blocker=None,
                 diuretic=None,
                 mineral=None,
                 additional_properties=None):
        """Constructor for the Medication class"""

        # Initialize members of the class
        self.ace_inhibitors = ace_inhibitors 
        self.antianginal = antianginal 
        self.anticoagulants = anticoagulants 
        self.beta_blocker = beta_blocker 
        self.diuretic = diuretic 
        self.mineral = mineral 

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
        ace_inhibitors = None
        if dictionary.get('aceInhibitors') is not None:
            ace_inhibitors = [AceInhibitor.from_dictionary(x) for x in dictionary.get('aceInhibitors')]
        antianginal = None
        if dictionary.get('antianginal') is not None:
            antianginal = [Antianginal.from_dictionary(x) for x in dictionary.get('antianginal')]
        anticoagulants = None
        if dictionary.get('anticoagulants') is not None:
            anticoagulants = [Anticoagulant.from_dictionary(x) for x in dictionary.get('anticoagulants')]
        beta_blocker = None
        if dictionary.get('betaBlocker') is not None:
            beta_blocker = [BetaBlocker.from_dictionary(x) for x in dictionary.get('betaBlocker')]
        diuretic = None
        if dictionary.get('diuretic') is not None:
            diuretic = [Diuretic.from_dictionary(x) for x in dictionary.get('diuretic')]
        mineral = None
        if dictionary.get('mineral') is not None:
            mineral = [Mineral.from_dictionary(x) for x in dictionary.get('mineral')]
        # Clean out expected properties from dictionary
        additional_properties = {k: v for k, v in dictionary.items() if k not in cls._names.values()}
        # Return an object of this model
        return cls(ace_inhibitors,
                   antianginal,
                   anticoagulants,
                   beta_blocker,
                   diuretic,
                   mineral,
                   additional_properties)

    def __repr__(self):
        return (f'{self.__class__.__name__}('
                f'ace_inhibitors={self.ace_inhibitors!r}, '
                f'antianginal={self.antianginal!r}, '
                f'anticoagulants={self.anticoagulants!r}, '
                f'beta_blocker={self.beta_blocker!r}, '
                f'diuretic={self.diuretic!r}, '
                f'mineral={self.mineral!r}, '
                f'additional_properties={self.additional_properties!r})')

    def __str__(self):
        return (f'{self.__class__.__name__}('
                f'ace_inhibitors={self.ace_inhibitors!s}, '
                f'antianginal={self.antianginal!s}, '
                f'anticoagulants={self.anticoagulants!s}, '
                f'beta_blocker={self.beta_blocker!s}, '
                f'diuretic={self.diuretic!s}, '
                f'mineral={self.mineral!s}, '
                f'additional_properties={self.additional_properties!s})')
