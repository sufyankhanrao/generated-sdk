"""tester.

This file was automatically generated for Stamplay by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

from tester.models.gloss_div import GlossDiv


class Glossary(object):
    """Implementation of the 'Glossary' model.

    Attributes:
        title (str): The model property of type str.
        gloss_div (GlossDiv): The model property of type GlossDiv.
        additional_properties (Dict[str, object]): The additional properties for the
            model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "gloss_div": "GlossDiv",
        "title": "title",
    }

    def __init__(
        self,
        gloss_div=None,
        title=None,
        additional_properties=None):
        """Initialize a Glossary instance."""
        # Initialize members of the class
        self.title = title
        self.gloss_div = gloss_div

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
        gloss_div =\
            GlossDiv.from_dictionary(
            dictionary.get("GlossDiv"))\
                if dictionary.get("GlossDiv") else None
        title =\
            dictionary.get("title")\
            if dictionary.get("title")\
                else None

        # Clean out expected properties from dictionary
        additional_properties =\
            {k: v for k, v in dictionary.items() if k not in cls._names.values()}
        # Return an object of this model
        return cls(gloss_div,
                   title,
                   additional_properties)

    def __repr__(self):
        """Return a unambiguous string representation."""
        _title=self.title
        _gloss_div=self.gloss_div
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"title={_title!r}"
            f"gloss_div={_gloss_div!r}"
            f"additional_properties={_additional_properties!r}"
            f")"
        )

    def __str__(self):
        """Return a human-readable string representation."""
        _title=self.title
        _gloss_div=self.gloss_div
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"title={_title!s}"
            f"gloss_div={_gloss_div!s}"
            f"additional_properties={_additional_properties!s}"
            f")"
        )
