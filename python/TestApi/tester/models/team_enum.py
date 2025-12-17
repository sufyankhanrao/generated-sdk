# -*- coding: utf-8 -*-

"""
tester

This file was automatically generated for Stamplay by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""


class TeamEnum(object):

    """Implementation of the 'team' enum.

    Attributes:
        CODEGEN: The enum member of type str.
        CGAAS: The enum member of type str.
        UX: The enum member of type str.
        QA: The enum member of type str.
        additional_properties (Dict[str, object]): The additional properties
            for the model.

    """
    CODEGEN = 'codegen'

    CGAAS = 'cgaas'

    UX = 'ux'

    QA = 'qa'

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
