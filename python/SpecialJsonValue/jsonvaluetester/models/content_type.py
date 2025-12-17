# -*- coding: utf-8 -*-

"""
jsonvaluetester

This file was automatically generated for Stamplay by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""


class ContentType(object):

    """Implementation of the 'Content-Type' enum.

    Attributes:
        ENUM_APPLICATIONXWWWFORMURLENCODED: The enum member of type str.
        additional_properties (Dict[str, object]): The additional properties
            for the model.

    """
    ENUM_APPLICATIONXWWWFORMURLENCODED = 'application/x-www-form-urlencoded'

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
