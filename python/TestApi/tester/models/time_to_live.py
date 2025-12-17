"""tester.

This file was automatically generated for Stamplay by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

class TimeToLive(object):
    """Implementation of the 'TimeToLive' model.

    Attributes:
        deadline (str): The model property of type str.
        delete_after_hours (int): The model property of type int.
        additional_properties (Dict[str, object]): The additional properties
            for the model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "deadline": "deadline",
        "delete_after_hours": "deleteAfterHours",
    }

    def __init__(self,
                 deadline=None,
                 delete_after_hours=None,
                 additional_properties=None):
        """Initialize a TimeToLive instance."""
        # Initialize members of the class
        self.deadline = deadline
        self.delete_after_hours = delete_after_hours

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
        deadline =\
            dictionary.get("deadline")\
            if dictionary.get("deadline") else None
        delete_after_hours =\
            dictionary.get("deleteAfterHours")\
            if dictionary.get("deleteAfterHours") else None
        # Clean out expected properties from dictionary
        additional_properties =\
            {k: v for k, v in dictionary.items() if k not in cls._names.values()}
        # Return an object of this model
        return cls(deadline,
                   delete_after_hours,
                   additional_properties)

    def __repr__(self):
        """Return a unambiguous string representation."""
        return (f"{self.__class__.__name__}("
                f"deadline={self.deadline!r}, "
                f"delete_after_hours={self.delete_after_hours!r}, "
                f"additional_properties={self.additional_properties!r})")

    def __str__(self):
        """Return a human-readable string representation."""
        return (f"{self.__class__.__name__}("
                f"deadline={self.deadline!s}, "
                f"delete_after_hours={self.delete_after_hours!s}, "
                f"additional_properties={self.additional_properties!s})")
