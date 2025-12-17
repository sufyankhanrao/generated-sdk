"""postnlecommerce.

This file was automatically generated for PostNL by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""


class CurrencyEnum(object):
    """Implementation of the 'Currency' enum.

    Currency code. only EUR, GBP, USD and CNY are allowed.

    Attributes:
        EUR: The enum member of type str.
        GBP: The enum member of type str.
        USD: The enum member of type str.
        CNY: The enum member of type str.

    """

    EUR = "EUR"

    GBP = "GBP"

    USD = "USD"

    CNY = "CNY"

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
