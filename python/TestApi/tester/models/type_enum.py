"""tester.

This file was automatically generated for Stamplay by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""


class TypeEnum(object):
    """Implementation of the 'Type' enum.

    Attributes:
        LONG: The enum member of type str.
        NUMBER: The enum member of type str.
        PRECISION: The enum member of type str.
        BOOLEAN: The enum member of type str.
        DATETIME: The enum member of type str.
        DATE: The enum member of type str.
        STRING: The enum member of type str.
        additional_properties (Dict[str, object]): The additional properties for the
            model.

    """

    LONG = "Long"

    NUMBER = "Number"

    PRECISION = "Precision"

    BOOLEAN = "Boolean"

    DATETIME = "DateTime"

    DATE = "Date"

    STRING = "String"

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
