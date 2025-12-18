# -*- coding: utf-8 -*-

"""
postnlecommerce

This file was automatically generated for PostNL by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""


class CodeEnum(object):

    """Implementation of the 'Code' enum.

    Sustainability score code

    Attributes:
        ENUM_00: The enum member of type str.
        ENUM_01: The enum member of type str.
        ENUM_02: The enum member of type str.
        ENUM_03: The enum member of type str.

    """
    ENUM_00 = '00'

    ENUM_01 = '01'

    ENUM_02 = '02'

    ENUM_03 = '03'

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
