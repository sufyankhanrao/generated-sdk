# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.api_helper import APIHelper
from advancedbilling.models.overage_pricing import OveragePricing
from advancedbilling.models.price import Price


class PrepaidComponentPricePoint(object):

    """Implementation of the 'Prepaid Component Price Point' model.

    Attributes:
        name (str): The model property of type str.
        handle (str): The model property of type str.
        pricing_scheme (PricingScheme): The identifier for the pricing scheme.
            See [Product
            Components](https://help.chargify.com/products/product-components.h
            tml) for an overview of pricing schemes.
        prices (List[Price]): The model property of type List[Price].
        overage_pricing (OveragePricing): The model property of type
            OveragePricing.
        additional_properties (Dict[str, object]): The additional properties
            for the model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "name": 'name',
        "handle": 'handle',
        "pricing_scheme": 'pricing_scheme',
        "prices": 'prices',
        "overage_pricing": 'overage_pricing'
    }

    _optionals = [
        'name',
        'handle',
        'pricing_scheme',
        'prices',
        'overage_pricing',
    ]

    def __init__(self,
                 name=APIHelper.SKIP,
                 handle=APIHelper.SKIP,
                 pricing_scheme=APIHelper.SKIP,
                 prices=APIHelper.SKIP,
                 overage_pricing=APIHelper.SKIP,
                 additional_properties=None):
        """Constructor for the PrepaidComponentPricePoint class"""

        # Initialize members of the class
        if name is not APIHelper.SKIP:
            self.name = name 
        if handle is not APIHelper.SKIP:
            self.handle = handle 
        if pricing_scheme is not APIHelper.SKIP:
            self.pricing_scheme = pricing_scheme 
        if prices is not APIHelper.SKIP:
            self.prices = prices 
        if overage_pricing is not APIHelper.SKIP:
            self.overage_pricing = overage_pricing 

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
        name = dictionary.get("name") if dictionary.get("name") else APIHelper.SKIP
        handle = dictionary.get("handle") if dictionary.get("handle") else APIHelper.SKIP
        pricing_scheme = dictionary.get("pricing_scheme") if dictionary.get("pricing_scheme") else APIHelper.SKIP
        prices = None
        if dictionary.get('prices') is not None:
            prices = [Price.from_dictionary(x) for x in dictionary.get('prices')]
        else:
            prices = APIHelper.SKIP
        overage_pricing = OveragePricing.from_dictionary(dictionary.get('overage_pricing')) if 'overage_pricing' in dictionary.keys() else APIHelper.SKIP
        # Clean out expected properties from dictionary
        additional_properties = {k: v for k, v in dictionary.items() if k not in cls._names.values()}
        # Return an object of this model
        return cls(name,
                   handle,
                   pricing_scheme,
                   prices,
                   overage_pricing,
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
                f'name={(self.name if hasattr(self, "name") else None)!r}, '
                f'handle={(self.handle if hasattr(self, "handle") else None)!r}, '
                f'pricing_scheme={(self.pricing_scheme if hasattr(self, "pricing_scheme") else None)!r}, '
                f'prices={(self.prices if hasattr(self, "prices") else None)!r}, '
                f'overage_pricing={(self.overage_pricing if hasattr(self, "overage_pricing") else None)!r}, '
                f'additional_properties={self.additional_properties!r})')

    def __str__(self):
        return (f'{self.__class__.__name__}('
                f'name={(self.name if hasattr(self, "name") else None)!s}, '
                f'handle={(self.handle if hasattr(self, "handle") else None)!s}, '
                f'pricing_scheme={(self.pricing_scheme if hasattr(self, "pricing_scheme") else None)!s}, '
                f'prices={(self.prices if hasattr(self, "prices") else None)!s}, '
                f'overage_pricing={(self.overage_pricing if hasattr(self, "overage_pricing") else None)!s}, '
                f'additional_properties={self.additional_properties!s})')
