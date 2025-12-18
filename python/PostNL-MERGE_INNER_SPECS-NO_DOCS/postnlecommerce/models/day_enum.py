# -*- coding: utf-8 -*-

"""
postnlecommerce

This file was automatically generated for PostNL by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""


class DayEnum(object):

    """Implementation of the 'Day' enum.

    The day for which the cutoff time applies. 00 is your default cutoff that
    applies to all otherwise not specified days, 01 to 07 is Monday to Sunday.

    Attributes:
        ENUM_00: The enum member of type str.
        ENUM_01: The enum member of type str.
        ENUM_02: The enum member of type str.
        ENUM_03: The enum member of type str.
        ENUM_04: The enum member of type str.
        ENUM_05: The enum member of type str.
        ENUM_06: The enum member of type str.
        ENUM_07: The enum member of type str.

    """
    ENUM_00 = '00'

    ENUM_01 = '01'

    ENUM_02 = '02'

    ENUM_03 = '03'

    ENUM_04 = '04'

    ENUM_05 = '05'

    ENUM_06 = '06'

    ENUM_07 = '07'

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
