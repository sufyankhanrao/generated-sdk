"""tester.

This file was automatically generated for Stamplay by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

class Lab(object):
    """Implementation of the 'Lab' model.

    Attributes:
        name (str): The model property of type str.
        time (str): The model property of type str.
        location (str): The model property of type str.
        additional_properties (Dict[str, object]): The additional properties for the
            model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "location": "location",
        "name": "name",
        "time": "time",
    }

    def __init__(
        self,
        location=None,
        name=None,
        time=None,
        additional_properties=None):
        """Initialize a Lab instance."""
        # Initialize members of the class
        self.name = name
        self.time = time
        self.location = location

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
        location =\
            dictionary.get("location")\
            if dictionary.get("location")\
                else None
        name =\
            dictionary.get("name")\
            if dictionary.get("name")\
                else None
        time =\
            dictionary.get("time")\
            if dictionary.get("time")\
                else None

        # Clean out expected properties from dictionary
        additional_properties =\
            {k: v for k, v in dictionary.items() if k not in cls._names.values()}
        # Return an object of this model
        return cls(location,
                   name,
                   time,
                   additional_properties)

    def __repr__(self):
        """Return a unambiguous string representation."""
        _name=self.name
        _time=self.time
        _location=self.location
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"name={_name!r}"
            f"time={_time!r}"
            f"location={_location!r}"
            f"additional_properties={_additional_properties!r}"
            f")"
        )

    def __str__(self):
        """Return a human-readable string representation."""
        _name=self.name
        _time=self.time
        _location=self.location
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"name={_name!s}"
            f"time={_time!s}"
            f"location={_location!s}"
            f"additional_properties={_additional_properties!s}"
            f")"
        )
