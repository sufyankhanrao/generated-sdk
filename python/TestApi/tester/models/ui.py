"""tester.

This file was automatically generated for Stamplay by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

from tester.models.dialogs import Dialogs
from tester.models.styling import Styling


class Ui(object):
    """Implementation of the 'Ui' model.

    Attributes:
        dialogs (Dialogs): The model property of type Dialogs.
        language (LanguageEnum): The model property of type LanguageEnum.
        styling (Styling): The model property of type Styling.
        additional_properties (Dict[str, object]): The additional properties
            for the model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "dialogs": "dialogs",
        "language": "language",
        "styling": "styling",
    }

    def __init__(self,
                 dialogs=None,
                 language=None,
                 styling=None,
                 additional_properties=None):
        """Initialize a Ui instance."""
        # Initialize members of the class
        self.dialogs = dialogs
        self.language = language
        self.styling = styling

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
        dialogs = Dialogs.from_dictionary(
            dictionary.get("dialogs"))\
            if dictionary.get("dialogs") else None
        language =\
            dictionary.get("language")\
            if dictionary.get("language") else None
        styling = Styling.from_dictionary(
            dictionary.get("styling"))\
            if dictionary.get("styling") else None
        # Clean out expected properties from dictionary
        additional_properties =\
            {k: v for k, v in dictionary.items() if k not in cls._names.values()}
        # Return an object of this model
        return cls(dialogs,
                   language,
                   styling,
                   additional_properties)

    def __repr__(self):
        """Return a unambiguous string representation."""
        return (f"{self.__class__.__name__}("
                f"dialogs={self.dialogs!r}, "
                f"language={self.language!r}, "
                f"styling={self.styling!r}, "
                f"additional_properties={self.additional_properties!r})")

    def __str__(self):
        """Return a human-readable string representation."""
        return (f"{self.__class__.__name__}("
                f"dialogs={self.dialogs!s}, "
                f"language={self.language!s}, "
                f"styling={self.styling!s}, "
                f"additional_properties={self.additional_properties!s})")
