# -*- coding: utf-8 -*-

"""
postnlecommerce

This file was automatically generated for PostNL by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""


class Type1Enum(object):

    """Implementation of the 'Type1' enum.

    Specifies the type belonging to the cutoff time.

    Attributes:
        REGULAR: The enum member of type str.
        SAMEDAY: The enum member of type str.
        TODAY: The enum member of type str.

    """
    REGULAR = 'Regular'

    SAMEDAY = 'Sameday'

    TODAY = 'Today'

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
