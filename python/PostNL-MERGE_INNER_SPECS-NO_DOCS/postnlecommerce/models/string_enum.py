"""postnlecommerce.

This file was automatically generated for PostNL by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""


class StringEnum(object):
    """Implementation of the 'String' enum.

    Attributes:
        DAYTIME: The enum member of type str.
        EVENING: The enum member of type str.
        MORNING: The enum member of type str.
        NOON: The enum member of type str.
        SUNDAY: The enum member of type str.
        TODAY: The enum member of type str.
        AFTERNOON: The enum member of type str.

    """

    DAYTIME = "Daytime"

    EVENING = "Evening"

    MORNING = "Morning"

    NOON = "Noon"

    SUNDAY = "Sunday"

    TODAY = "Today"

    AFTERNOON = "Afternoon"

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
