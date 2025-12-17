"""tester.

This file was automatically generated for Stamplay by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

from tester.api_helper import APIHelper
from tester.models.long_as_optional import LongAsOptional
from tester.models.number_as_optional import (
    NumberAsOptional,
)
from tester.models.precision_as_optional import (
    PrecisionAsOptional,
)


class StringAsOptional(object):
    """Implementation of the 'string as optional' model.

    Attributes:
        string (str): The model property of type str.
        additional_properties (Dict[str, object]): The additional properties
            for the model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "string": "string",
    }

    _optionals = [
        "string",
    ]

    def __init__(self,
                 string=APIHelper.SKIP,
                 additional_properties=None):
        """Initialize a StringAsOptional instance."""
        # Initialize members of the class
        if string is not APIHelper.SKIP:
            self.string = string

        # Add additional model properties to the instance
        if additional_properties is None:
            additional_properties = {}
        self.additional_properties = additional_properties

    @classmethod
    def from_dictionary(cls,
                        dictionary):
        """Create an instance of this model from a dictionary

        Args:
            dictionary (dictionary): A dictionary representation of the object
            as obtained from the deserialization of the server's response. The
            keys MUST match property names in the API description.

        Returns:
            object: An instance of this structure class.

        """
        if not isinstance(dictionary, dict) or dictionary is None:
            return None

        # Extract variables from the dictionary
        string =\
            dictionary.get("string")\
            if dictionary.get("string") else APIHelper.SKIP
        # Clean out expected properties from dictionary
        additional_properties =\
            {k: v for k, v in dictionary.items() if k not in cls._names.values()}
        # Return an object of this model
        return cls(string,
                   additional_properties)

    def __repr__(self):
        """Return a unambiguous string representation."""
        return (f"{self.__class__.__name__}("
                f"string={(self.string if hasattr(self, 'string') else None)!r}, "
                f"additional_properties={self.additional_properties!r})")

    def __str__(self):
        """Return a human-readable string representation."""
        return (f"{self.__class__.__name__}("
                f"string={(self.string if hasattr(self, 'string') else None)!s}, "
                f"additional_properties={self.additional_properties!s})")

class AllOptionals(StringAsOptional):
    """Implementation of the 'all optionals' model.
    NOTE: This class inherits from 'StringAsOptional'.

    Attributes:
        id (int): The model property of type int.
        optional_numbers (List[NumberAsOptional]): The model property of type
            List[NumberAsOptional].
        optional_long (LongAsOptional): The model property of type
            LongAsOptional.
        optional_precision (PrecisionAsOptional): The model property of type
            PrecisionAsOptional.
        additional_properties (Dict[str, object]): The additional properties
            for the model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "id": "id",
        "optional_long": "optionalLong",
        "optional_numbers": "optionalNumbers",
        "optional_precision": "optionalPrecision",
        "string": "string",
    }

    _optionals = [
        "id",
        "optional_numbers",
        "optional_long",
        "optional_precision",
    ]
    _optionals.extend(StringAsOptional._optionals)

    _nullables = [
        "id",
    ]

    def __init__(self,
                 id=APIHelper.SKIP,
                 optional_long=APIHelper.SKIP,
                 optional_numbers=APIHelper.SKIP,
                 optional_precision=APIHelper.SKIP,
                 string=APIHelper.SKIP,
                 additional_properties=None):
        """Initialize a AllOptionals instance."""
        # Initialize members of the class
        if id is not APIHelper.SKIP:
            self.id = id
        if optional_numbers is not APIHelper.SKIP:
            self.optional_numbers = optional_numbers
        if optional_long is not APIHelper.SKIP:
            self.optional_long = optional_long
        if optional_precision is not APIHelper.SKIP:
            self.optional_precision = optional_precision

        # Call the constructor for the base class
        super(AllOptionals, self).__init__(string,
                                           additional_properties)

    @classmethod
    def from_dictionary(cls,
                        dictionary):
        """Create an instance of this model from a dictionary

        Args:
            dictionary (dictionary): A dictionary representation of the object
            as obtained from the deserialization of the server's response. The
            keys MUST match property names in the API description.

        Returns:
            object: An instance of this structure class.

        """
        if not isinstance(dictionary, dict) or dictionary is None:
            return None

        # Extract variables from the dictionary
        id = dictionary.get("id") if "id" in dictionary.keys() else APIHelper.SKIP
        optional_long = LongAsOptional.from_dictionary(
            dictionary.get("optionalLong"))\
            if "optionalLong" in dictionary.keys() else APIHelper.SKIP
        optional_numbers = None
        if dictionary.get("optionalNumbers") is not None:
            optional_numbers = [
                NumberAsOptional.from_dictionary(x)
                    for x in dictionary.get("optionalNumbers")
            ]
        else:
            optional_numbers = APIHelper.SKIP
        optional_precision = PrecisionAsOptional.from_dictionary(
            dictionary.get("optionalPrecision"))\
            if "optionalPrecision" in dictionary.keys() else APIHelper.SKIP
        string =\
            dictionary.get("string")\
            if dictionary.get("string") else APIHelper.SKIP
        # Clean out expected properties from dictionary
        additional_properties =\
            {k: v for k, v in dictionary.items() if k not in cls._names.values()}
        # Return an object of this model
        return cls(id,
                   optional_long,
                   optional_numbers,
                   optional_precision,
                   string,
                   additional_properties)

    def __repr__(self):
        """Return a unambiguous string representation."""
        base_repr = super().__repr__()
        return (f"{self.__class__.__name__}("
                f"{base_repr[base_repr.find('(') + 1:-1]}, "
                f"id={(self.id if hasattr(self, 'id') else None)!r}, "
                f"optional_numbers={(self.optional_numbers
                     if hasattr(self, 'optional_numbers') else None)!r}, "
                f"optional_long={(self.optional_long
                     if hasattr(self, 'optional_long') else None)!r}, "
                f"optional_precision={(self.optional_precision
                     if hasattr(self, 'optional_precision') else None)!r})")

    def __str__(self):
        """Return a human-readable string representation."""
        base_str = super().__str__()
        return (f"{self.__class__.__name__}("
                f"{base_str[base_str.find('(') + 1:-1]}, "
                f"id={(self.id if hasattr(self, 'id') else None)!s}, "
                f"optional_numbers={(self.optional_numbers
                     if hasattr(self, 'optional_numbers') else None)!s}, "
                f"optional_long={(self.optional_long
                     if hasattr(self, 'optional_long') else None)!s}, "
                f"optional_precision={(self.optional_precision
                     if hasattr(self, 'optional_precision') else None)!s})")
