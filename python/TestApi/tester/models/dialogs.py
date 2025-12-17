"""tester.

This file was automatically generated for Stamplay by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

from tester.models.before import Before


class Dialogs(object):
    """Implementation of the 'Dialogs' model.

    Attributes:
        before (Before): The model property of type Before.
        additional_properties (Dict[str, object]): The additional properties
            for the model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "before": "before",
    }

    def __init__(self,
                 before=None,
                 additional_properties=None):
        """Initialize a Dialogs instance."""
        # Initialize members of the class
        self.before = before

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
        before = Before.from_dictionary(
            dictionary.get("before"))\
            if dictionary.get("before") else None
        # Clean out expected properties from dictionary
        additional_properties =\
            {k: v for k, v in dictionary.items() if k not in cls._names.values()}
        # Return an object of this model
        return cls(before,
                   additional_properties)

    def __repr__(self):
        """Return a unambiguous string representation."""
        return (f"{self.__class__.__name__}("
                f"before={self.before!r}, "
                f"additional_properties={self.additional_properties!r})")

    def __str__(self):
        """Return a human-readable string representation."""
        return (f"{self.__class__.__name__}("
                f"before={self.before!s}, "
                f"additional_properties={self.additional_properties!s})")
