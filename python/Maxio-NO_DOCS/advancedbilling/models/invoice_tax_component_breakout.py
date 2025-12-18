# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.api_helper import APIHelper


class InvoiceTaxComponentBreakout(object):

    """Implementation of the 'Invoice Tax Component Breakout' model.

    Attributes:
        tax_rule_id (int): The model property of type int.
        percentage (str): The model property of type str.
        country_code (str): The model property of type str.
        subdivision_code (str): The model property of type str.
        additional_properties (Dict[str, object]): The additional properties
            for the model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "tax_rule_id": 'tax_rule_id',
        "percentage": 'percentage',
        "country_code": 'country_code',
        "subdivision_code": 'subdivision_code'
    }

    _optionals = [
        'tax_rule_id',
        'percentage',
        'country_code',
        'subdivision_code',
    ]

    def __init__(self,
                 tax_rule_id=APIHelper.SKIP,
                 percentage=APIHelper.SKIP,
                 country_code=APIHelper.SKIP,
                 subdivision_code=APIHelper.SKIP,
                 additional_properties=None):
        """Constructor for the InvoiceTaxComponentBreakout class"""

        # Initialize members of the class
        if tax_rule_id is not APIHelper.SKIP:
            self.tax_rule_id = tax_rule_id 
        if percentage is not APIHelper.SKIP:
            self.percentage = percentage 
        if country_code is not APIHelper.SKIP:
            self.country_code = country_code 
        if subdivision_code is not APIHelper.SKIP:
            self.subdivision_code = subdivision_code 

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
        tax_rule_id = dictionary.get("tax_rule_id") if dictionary.get("tax_rule_id") else APIHelper.SKIP
        percentage = dictionary.get("percentage") if dictionary.get("percentage") else APIHelper.SKIP
        country_code = dictionary.get("country_code") if dictionary.get("country_code") else APIHelper.SKIP
        subdivision_code = dictionary.get("subdivision_code") if dictionary.get("subdivision_code") else APIHelper.SKIP
        # Clean out expected properties from dictionary
        additional_properties = {k: v for k, v in dictionary.items() if k not in cls._names.values()}
        # Return an object of this model
        return cls(tax_rule_id,
                   percentage,
                   country_code,
                   subdivision_code,
                   additional_properties)

    @classmethod
    def validate(cls, dictionary):
        """Validates dictionary against class required properties

        Args:
            dictionary (dictionary): A dictionary representation of the object
            as obtained from the deserialization of the server's response. The
            keys MUST match property names in the API description.

        Returns:
            boolean : if dictionary is valid contains required properties.

        """

        if isinstance(dictionary, cls):
            return True

        if not isinstance(dictionary, dict):
            return False

        return True

    def __repr__(self):
        return (f'{self.__class__.__name__}('
                f'tax_rule_id={(self.tax_rule_id if hasattr(self, "tax_rule_id") else None)!r}, '
                f'percentage={(self.percentage if hasattr(self, "percentage") else None)!r}, '
                f'country_code={(self.country_code if hasattr(self, "country_code") else None)!r}, '
                f'subdivision_code={(self.subdivision_code if hasattr(self, "subdivision_code") else None)!r}, '
                f'additional_properties={self.additional_properties!r})')

    def __str__(self):
        return (f'{self.__class__.__name__}('
                f'tax_rule_id={(self.tax_rule_id if hasattr(self, "tax_rule_id") else None)!s}, '
                f'percentage={(self.percentage if hasattr(self, "percentage") else None)!s}, '
                f'country_code={(self.country_code if hasattr(self, "country_code") else None)!s}, '
                f'subdivision_code={(self.subdivision_code if hasattr(self, "subdivision_code") else None)!s}, '
                f'additional_properties={self.additional_properties!s})')
