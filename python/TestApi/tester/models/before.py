"""tester.

This file was automatically generated for Stamplay by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

class Before(object):
    """Implementation of the 'Before' model.

    Attributes:
        use_check_box (bool): The model property of type bool.
        title (str): The model property of type str.
        message (str): The model property of type str.
        additional_properties (Dict[str, object]): The additional properties for the
            model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "message": "message",
        "title": "title",
        "use_check_box": "useCheckBox",
    }

    def __init__(
        self,
        message=None,
        title=None,
        use_check_box=None,
        additional_properties=None):
        """Initialize a Before instance."""
        # Initialize members of the class
        self.use_check_box = use_check_box
        self.title = title
        self.message = message

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
        message =\
            dictionary.get("message")\
            if dictionary.get("message")\
                else None
        title =\
            dictionary.get("title")\
            if dictionary.get("title")\
                else None
        use_check_box =\
            dictionary.get("useCheckBox")\
            if "useCheckBox" in dictionary.keys()\
                else None

        # Clean out expected properties from dictionary
        additional_properties =\
            {k: v for k, v in dictionary.items() if k not in cls._names.values()}
        # Return an object of this model
        return cls(message,
                   title,
                   use_check_box,
                   additional_properties)

    def __repr__(self):
        """Return a unambiguous string representation."""
        _use_check_box=self.use_check_box
        _title=self.title
        _message=self.message
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"use_check_box={_use_check_box!r}"
            f"title={_title!r}"
            f"message={_message!r}"
            f"additional_properties={_additional_properties!r}"
            f")"
        )

    def __str__(self):
        """Return a human-readable string representation."""
        _use_check_box=self.use_check_box
        _title=self.title
        _message=self.message
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"use_check_box={_use_check_box!s}"
            f"title={_title!s}"
            f"message={_message!s}"
            f"additional_properties={_additional_properties!s}"
            f")"
        )
