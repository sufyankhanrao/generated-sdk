"""postnlecommerce.

This file was automatically generated for PostNL by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""


class Option1Enum(object):
    """Implementation of the 'Option1' enum.

    Attributes:
        DAYTIME: The enum member of type str.
        EVENING: The enum member of type str.
        SUNDAY: The enum member of type str.
        SAMEDAY: The enum member of type str.
        TODAY: The enum member of type str.
        ENUM_08001000: The enum member of type str.
        ENUM_08001200: The enum member of type str.
        ENUM_08001700: The enum member of type str.

    """

    DAYTIME = "Daytime"

    EVENING = "Evening"

    SUNDAY = "Sunday"

    SAMEDAY = "Sameday"

    TODAY = "Today"

    ENUM_08001000 = "08:00-10:00"

    ENUM_08001200 = "08:00-12:00"

    ENUM_08001700 = "08:00-17:00"

    @classmethod
    def from_value(cls, value, default=None):
        """Return the matching enum value for the given input."""
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
