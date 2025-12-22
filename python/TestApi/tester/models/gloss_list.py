"""tester.

This file was automatically generated for Stamplay by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

from tester.models.gloss_entry import GlossEntry


class GlossList(object):
    """Implementation of the 'GlossList' model.

    Attributes:
        gloss_entry (GlossEntry): The model property of type GlossEntry.
        additional_properties (Dict[str, object]): The additional properties for the
            model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "gloss_entry": "GlossEntry",
    }

    def __init__(
        self,
        gloss_entry=None,
        additional_properties=None):
        """Initialize a GlossList instance."""
        # Initialize members of the class
        self.gloss_entry = gloss_entry

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
        gloss_entry =\
            GlossEntry.from_dictionary(
            dictionary.get("GlossEntry"))\
                if dictionary.get("GlossEntry") else None

        # Clean out expected properties from dictionary
        additional_properties =\
            {k: v for k, v in dictionary.items() if k not in cls._names.values()}
        # Return an object of this model
        return cls(gloss_entry,
                   additional_properties)

    def __repr__(self):
        """Return a unambiguous string representation."""
        _gloss_entry=self.gloss_entry
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"gloss_entry={_gloss_entry!r}"
            f"additional_properties={_additional_properties!r}"
            f")"
        )

    def __str__(self):
        """Return a human-readable string representation."""
        _gloss_entry=self.gloss_entry
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"gloss_entry={_gloss_entry!s}"
            f"additional_properties={_additional_properties!s}"
            f")"
        )
