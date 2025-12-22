"""tester.

This file was automatically generated for Stamplay by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

import dateutil.parser

from tester.api_helper import APIHelper


class InnerComplexType(object):
    """Implementation of the 'InnerComplexType' model.

    Attributes:
        string_type (str): The model property of type str.
        boolean_type (bool): The model property of type bool.
        date_time_type (datetime): The model property of type datetime.
        date_type (date): The model property of type date.
        uuid_type (uuid|str): The model property of type uuid|str.
        long_type (int): The model property of type int.
        precision_type (float): The model property of type float.
        object_type (Any): The model property of type Any.
        string_list_type (List[str]): The model property of type List[str].
        additional_properties (Dict[str, object]): The additional properties for the
            model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "boolean_type": "booleanType",
        "date_time_type": "dateTimeType",
        "date_type": "dateType",
        "long_type": "longType",
        "object_type": "objectType",
        "precision_type": "precisionType",
        "string_list_type": "stringListType",
        "string_type": "stringType",
        "uuid_type": "uuidType",
    }

    def __init__(
        self,
        boolean_type=None,
        date_time_type=None,
        date_type=None,
        long_type=None,
        object_type=None,
        precision_type=None,
        string_list_type=None,
        string_type=None,
        uuid_type=None,
        additional_properties=None):
        """Initialize a InnerComplexType instance."""
        # Initialize members of the class
        self.string_type = string_type
        self.boolean_type = boolean_type
        self.date_time_type =\
             APIHelper.apply_datetime_converter(
            date_time_type, APIHelper.RFC3339DateTime)\
             if date_time_type else None
        self.date_type = date_type
        self.uuid_type = uuid_type
        self.long_type = long_type
        self.precision_type = precision_type
        self.object_type = object_type
        self.string_list_type = string_list_type

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
        boolean_type =\
            dictionary.get("booleanType")\
            if "booleanType" in dictionary.keys()\
                else None
        date_time_type = APIHelper.RFC3339DateTime.from_value(
            dictionary.get("dateTimeType")).datetime\
            if dictionary.get("dateTimeType") else None
        date_type = dateutil.parser.parse(
            dictionary.get("dateType")).date()\
            if dictionary.get("dateType") else None
        long_type =\
            dictionary.get("longType")\
            if dictionary.get("longType")\
                else None
        object_type =\
            dictionary.get("objectType")\
            if dictionary.get("objectType")\
                else None
        precision_type =\
            dictionary.get("precisionType")\
            if dictionary.get("precisionType")\
                else None
        string_list_type =\
            dictionary.get("stringListType")\
            if dictionary.get("stringListType")\
                else None
        string_type =\
            dictionary.get("stringType")\
            if dictionary.get("stringType")\
                else None
        uuid_type =\
            dictionary.get("uuidType")\
            if dictionary.get("uuidType")\
                else None

        # Clean out expected properties from dictionary
        additional_properties =\
            {k: v for k, v in dictionary.items() if k not in cls._names.values()}
        # Return an object of this model
        return cls(boolean_type,
                   date_time_type,
                   date_type,
                   long_type,
                   object_type,
                   precision_type,
                   string_list_type,
                   string_type,
                   uuid_type,
                   additional_properties)

    def __repr__(self):
        """Return a unambiguous string representation."""
        _string_type=self.string_type
        _boolean_type=self.boolean_type
        _date_time_type=self.date_time_type
        _date_type=self.date_type
        _uuid_type=self.uuid_type
        _long_type=self.long_type
        _precision_type=self.precision_type
        _object_type=self.object_type
        _string_list_type=self.string_list_type
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"string_type={_string_type!r}"
            f"boolean_type={_boolean_type!r}"
            f"date_time_type={_date_time_type!r}"
            f"date_type={_date_type!r}"
            f"uuid_type={_uuid_type!r}"
            f"long_type={_long_type!r}"
            f"precision_type={_precision_type!r}"
            f"object_type={_object_type!r}"
            f"string_list_type={_string_list_type!r}"
            f"additional_properties={_additional_properties!r}"
            f")"
        )

    def __str__(self):
        """Return a human-readable string representation."""
        _string_type=self.string_type
        _boolean_type=self.boolean_type
        _date_time_type=self.date_time_type
        _date_type=self.date_type
        _uuid_type=self.uuid_type
        _long_type=self.long_type
        _precision_type=self.precision_type
        _object_type=self.object_type
        _string_list_type=self.string_list_type
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"string_type={_string_type!s}"
            f"boolean_type={_boolean_type!s}"
            f"date_time_type={_date_time_type!s}"
            f"date_type={_date_type!s}"
            f"uuid_type={_uuid_type!s}"
            f"long_type={_long_type!s}"
            f"precision_type={_precision_type!s}"
            f"object_type={_object_type!s}"
            f"string_list_type={_string_list_type!s}"
            f"additional_properties={_additional_properties!s}"
            f")"
        )
