# -*- coding: utf-8 -*-

"""
postnlecommerce

This file was automatically generated for PostNL by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""


class String1Enum(object):

    """Implementation of the 'String1' enum.

    Attributes:
        DAYTIME: The enum member of type str.
        TODAY: The enum member of type str.
        SAMEDAY: The enum member of type str.
        EVENING: The enum member of type str.
        MORNING: The enum member of type str.
        NOON: The enum member of type str.
        SUNDAY: The enum member of type str.
        AFTERNOON: The enum member of type str.

    """
    DAYTIME = 'Daytime'

    TODAY = 'Today'

    SAMEDAY = 'Sameday'

    EVENING = 'Evening'

    MORNING = 'Morning'

    NOON = 'Noon'

    SUNDAY = 'Sunday'

    AFTERNOON = 'Afternoon'

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
