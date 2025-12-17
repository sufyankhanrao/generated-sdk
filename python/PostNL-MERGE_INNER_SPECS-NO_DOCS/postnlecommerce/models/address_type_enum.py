"""postnlecommerce.

This file was automatically generated for PostNL by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""


class AddressTypeEnum(object):
    """Implementation of the 'AddressType' enum.

    Address type. 01 is for the receiver address, 02 is for the sender address.

    Attributes:
        ENUM_01: The enum member of type str.
        ENUM_02: The enum member of type str.

    """

    ENUM_01 = "01"

    ENUM_02 = "02"

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
