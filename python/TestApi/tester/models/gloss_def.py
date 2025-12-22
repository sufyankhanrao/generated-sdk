"""tester.

This file was automatically generated for Stamplay by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

class GlossDef(object):
    """Implementation of the 'GlossDef' model.

    Attributes:
        para (str): The model property of type str.
        gloss_see_also (List[str]): The model property of type List[str].
        additional_properties (Dict[str, object]): The additional properties for the
            model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "gloss_see_also": "GlossSeeAlso",
        "para": "para",
    }

    def __init__(
        self,
        gloss_see_also=None,
        para=None,
        additional_properties=None):
        """Initialize a GlossDef instance."""
        # Initialize members of the class
        self.para = para
        self.gloss_see_also = gloss_see_also

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
        gloss_see_also =\
            dictionary.get("GlossSeeAlso")\
            if dictionary.get("GlossSeeAlso")\
                else None
        para =\
            dictionary.get("para")\
            if dictionary.get("para")\
                else None

        # Clean out expected properties from dictionary
        additional_properties =\
            {k: v for k, v in dictionary.items() if k not in cls._names.values()}
        # Return an object of this model
        return cls(gloss_see_also,
                   para,
                   additional_properties)

    def __repr__(self):
        """Return a unambiguous string representation."""
        _para=self.para
        _gloss_see_also=self.gloss_see_also
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"para={_para!r}"
            f"gloss_see_also={_gloss_see_also!r}"
            f"additional_properties={_additional_properties!r}"
            f")"
        )

    def __str__(self):
        """Return a human-readable string representation."""
        _para=self.para
        _gloss_see_also=self.gloss_see_also
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"para={_para!s}"
            f"gloss_see_also={_gloss_see_also!s}"
            f"additional_properties={_additional_properties!s}"
            f")"
        )
