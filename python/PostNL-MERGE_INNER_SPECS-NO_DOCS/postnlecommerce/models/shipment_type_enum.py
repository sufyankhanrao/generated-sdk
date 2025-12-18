# -*- coding: utf-8 -*-

"""
postnlecommerce

This file was automatically generated for PostNL by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""


class ShipmentTypeEnum(object):

    """Implementation of the 'ShipmentType' enum.

    Type of shipment, possible values: Gift, Documents, Commercial Goods,
    Commercial Sample, Returned Goods. Is used to fill in the checkbox on the
    customs form on the shipment label.

    Attributes:
        GIFT: The enum member of type str.
        DOCUMENTS: The enum member of type str.
        ENUM_COMMERCIAL GOODS: The enum member of type str.
        ENUM_COMMERCIAL SAMPLE: The enum member of type str.
        ENUM_RETURNED GOODS: The enum member of type str.

    """
    GIFT = 'Gift'

    DOCUMENTS = 'Documents'

    ENUM_COMMERCIAL_GOODS = 'Commercial Goods'

    ENUM_COMMERCIAL_SAMPLE = 'Commercial Sample'

    ENUM_RETURNED_GOODS = 'Returned Goods'

    @classmethod
    def from_value(cls, value, default=None):
        if value is None:
            return default

        # If numeric and matches directly
        if isinstance(value, int):
            for name, val in cls.__dict__.items():
                if not name.startswith("_") and val == value:
                    return val

        # If string, perform case-insensitive match
        if isinstance(value, str):
            value_lower = value.lower()
            for name, val in cls.__dict__.items():
                if not name.startswith("_") and (
                    name.lower() == value_lower or str(val).lower() == value_lower
                ):
                    return val

        # Fallback to default
        return default
