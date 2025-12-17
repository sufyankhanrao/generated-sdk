"""tester.

This file was automatically generated for Stamplay by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

from tester.api_helper import APIHelper


class ModelWithOptionalRfc3339DateTime(object):
    """Implementation of the 'Model With optional rfc3339 DateTime' model.

    Attributes:
        date_time (datetime): The model property of type datetime.
        additional_properties (Dict[str, object]): The additional properties
            for the model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "date_time": "dateTime",
    }

    _optionals = [
        "date_time",
    ]

    def __init__(self,
                 date_time=APIHelper.SKIP,
                 additional_properties=None):
        """Initialize a ModelWithOptionalRfc3339DateTime instance."""
        # Initialize members of the class
        if date_time is not APIHelper.SKIP:
            self.date_time =\
                 APIHelper.apply_datetime_converter(
                date_time, APIHelper.RFC3339DateTime) if date_time else None

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
        date_time = APIHelper.RFC3339DateTime.from_value(
            dictionary.get("dateTime")).datetime\
            if dictionary.get("dateTime") else APIHelper.SKIP
        # Clean out expected properties from dictionary
        additional_properties =\
            {k: v for k, v in dictionary.items() if k not in cls._names.values()}
        # Return an object of this model
        return cls(date_time,
                   additional_properties)

    def __repr__(self):
        """Return a unambiguous string representation."""
        return (f"{self.__class__.__name__}("
                f"date_time={(self.date_time
                     if hasattr(self, 'date_time') else None)!r}, "
                f"additional_properties={self.additional_properties!r})")

    def __str__(self):
        """Return a human-readable string representation."""
        return (f"{self.__class__.__name__}("
                f"date_time={(self.date_time
                     if hasattr(self, 'date_time') else None)!s}, "
                f"additional_properties={self.additional_properties!s})")
