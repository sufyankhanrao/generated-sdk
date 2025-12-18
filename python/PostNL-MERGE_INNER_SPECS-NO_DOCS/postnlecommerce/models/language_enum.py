# -*- coding: utf-8 -*-

"""
postnlecommerce

This file was automatically generated for PostNL by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""


class LanguageEnum(object):

    """Implementation of the 'language' enum.

    Attributes:
        NL: The enum member of type str.
        EN: The enum member of type str.
        CN: The enum member of type str.
        DE: The enum member of type str.
        FR: The enum member of type str.

    """
    NL = 'NL'

    EN = 'EN'

    CN = 'CN'

    DE = 'DE'

    FR = 'FR'

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
