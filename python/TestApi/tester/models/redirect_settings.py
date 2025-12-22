"""tester.

This file was automatically generated for Stamplay by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

class RedirectSettings(object):
    """Implementation of the 'RedirectSettings' model.

    Attributes:
        redirect_mode (str): The model property of type str.
        additional_properties (Dict[str, object]): The additional properties for the
            model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "redirect_mode": "redirectMode",
    }

    def __init__(
        self,
        redirect_mode=None,
        additional_properties=None):
        """Initialize a RedirectSettings instance."""
        # Initialize members of the class
        self.redirect_mode = redirect_mode

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
        redirect_mode =\
            dictionary.get("redirectMode")\
            if dictionary.get("redirectMode")\
                else None

        # Clean out expected properties from dictionary
        additional_properties =\
            {k: v for k, v in dictionary.items() if k not in cls._names.values()}
        # Return an object of this model
        return cls(redirect_mode,
                   additional_properties)

    def __repr__(self):
        """Return a unambiguous string representation."""
        _redirect_mode=self.redirect_mode
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"redirect_mode={_redirect_mode!r}"
            f"additional_properties={_additional_properties!r}"
            f")"
        )

    def __str__(self):
        """Return a human-readable string representation."""
        _redirect_mode=self.redirect_mode
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"redirect_mode={_redirect_mode!s}"
            f"additional_properties={_additional_properties!s}"
            f")"
        )
