"""tester.

This file was automatically generated for Stamplay by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

from tester.api_helper import APIHelper


class AddUnixTimeStampInGlobalException(object):
    """Implementation of the 'Add unix time stamp in global exception' model.

    Attributes:
        date_time (datetime): The model property of type datetime.
        date_time_1 (datetime): The model property of type datetime.
        additional_properties (Dict[str, object]): The additional properties for the
            model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "date_time": "dateTime",
        "date_time_1": "dateTime1",
    }

    _optionals = [
        "date_time_1",
    ]

    def __init__(
        self,
        date_time=None,
        date_time_1=APIHelper.SKIP,
        additional_properties=None):
        """Initialize a AddUnixTimeStampInGlobalException instance."""
        # Initialize members of the class
        self.date_time =\
             APIHelper.apply_datetime_converter(
            date_time, APIHelper.UnixDateTime)\
             if date_time else None
        if date_time_1 is not APIHelper.SKIP:
            self.date_time_1 =\
                 APIHelper.apply_datetime_converter(
                date_time_1, APIHelper.UnixDateTime)\
                 if date_time_1 else None

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
        date_time = APIHelper.UnixDateTime.from_value(
            dictionary.get("dateTime")).datetime\
            if dictionary.get("dateTime") else None
        date_time_1 = APIHelper.UnixDateTime.from_value(
            dictionary.get("dateTime1")).datetime\
            if dictionary.get("dateTime1") else APIHelper.SKIP

        # Clean out expected properties from dictionary
        additional_properties =\
            {k: v for k, v in dictionary.items() if k not in cls._names.values()}
        # Return an object of this model
        return cls(date_time,
                   date_time_1,
                   additional_properties)

    def __repr__(self):
        """Return a unambiguous string representation."""
        _date_time=self.date_time
        _date_time_1=(
            self.date_time_1
            if hasattr(self, "date_time_1")
            else None
        )
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"date_time={_date_time!r}"
            f"date_time_1={_date_time_1!r}"
            f"additional_properties={_additional_properties!r}"
            f")"
        )

    def __str__(self):
        """Return a human-readable string representation."""
        _date_time=self.date_time
        _date_time_1=(
            self.date_time_1
            if hasattr(self, "date_time_1")
            else None
        )
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"date_time={_date_time!s}"
            f"date_time_1={_date_time_1!s}"
            f"additional_properties={_additional_properties!s}"
            f")"
        )
