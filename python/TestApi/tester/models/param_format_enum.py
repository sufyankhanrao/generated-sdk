"""tester.

This file was automatically generated for Stamplay by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""


class ParamFormatEnum(object):
    """Implementation of the 'ParamFormat' enum.

    Attributes:
        TEMPLATE: The enum member of type str.
        FORM: The enum member of type str.
        BODY: The enum member of type str.
        HEADER: The enum member of type str.
        QUERY: The enum member of type str.
        additional_properties (Dict[str, object]): The additional properties
            for the model.

    """

    TEMPLATE = "Template"

    FORM = "Form"

    BODY = "Body"

    HEADER = "Header"

    QUERY = "Query"

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
