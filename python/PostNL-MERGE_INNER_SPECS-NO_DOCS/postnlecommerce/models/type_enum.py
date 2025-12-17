"""postnlecommerce.

This file was automatically generated for PostNL by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""


class TypeEnum(object):
    """Implementation of the 'Type' enum.

    Attributes:
        ENUM_2S: The enum member of type str.
        ENUM_3S: The enum member of type str.
        CC: The enum member of type str.
        CP: The enum member of type str.
        CD: The enum member of type str.
        CF: The enum member of type str.
        LA: The enum member of type str.
        RI: The enum member of type str.
        UE: The enum member of type str.

    """

    ENUM_2S = "2S"

    ENUM_3S = "3S"

    CC = "CC"

    CP = "CP"

    CD = "CD"

    CF = "CF"

    LA = "LA"

    RI = "RI"

    UE = "UE"

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
