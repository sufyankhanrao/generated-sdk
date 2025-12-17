"""tester.

This file was automatically generated for Stamplay by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

from tester.models.gloss_def import GlossDef


class GlossEntry(object):
    """Implementation of the 'GlossEntry' model.

    Attributes:
        id (str): The model property of type str.
        sort_as (str): The model property of type str.
        gloss_term (str): The model property of type str.
        acronym (str): The model property of type str.
        abbrev (str): The model property of type str.
        gloss_def (GlossDef): The model property of type GlossDef.
        gloss_see (str): The model property of type str.
        additional_properties (Dict[str, object]): The additional properties
            for the model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "abbrev": "Abbrev",
        "acronym": "Acronym",
        "gloss_def": "GlossDef",
        "gloss_see": "GlossSee",
        "gloss_term": "GlossTerm",
        "id": "ID",
        "sort_as": "SortAs",
    }

    def __init__(self,
                 abbrev=None,
                 acronym=None,
                 gloss_def=None,
                 gloss_see=None,
                 gloss_term=None,
                 id=None,
                 sort_as=None,
                 additional_properties=None):
        """Initialize a GlossEntry instance."""
        # Initialize members of the class
        self.id = id
        self.sort_as = sort_as
        self.gloss_term = gloss_term
        self.acronym = acronym
        self.abbrev = abbrev
        self.gloss_def = gloss_def
        self.gloss_see = gloss_see

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
        abbrev = dictionary.get("Abbrev") if dictionary.get("Abbrev") else None
        acronym = dictionary.get("Acronym") if dictionary.get("Acronym") else None
        gloss_def = GlossDef.from_dictionary(
            dictionary.get("GlossDef"))\
            if dictionary.get("GlossDef") else None
        gloss_see =\
            dictionary.get("GlossSee")\
            if dictionary.get("GlossSee") else None
        gloss_term =\
            dictionary.get("GlossTerm")\
            if dictionary.get("GlossTerm") else None
        id = dictionary.get("ID") if dictionary.get("ID") else None
        sort_as = dictionary.get("SortAs") if dictionary.get("SortAs") else None
        # Clean out expected properties from dictionary
        additional_properties =\
            {k: v for k, v in dictionary.items() if k not in cls._names.values()}
        # Return an object of this model
        return cls(abbrev,
                   acronym,
                   gloss_def,
                   gloss_see,
                   gloss_term,
                   id,
                   sort_as,
                   additional_properties)

    def __repr__(self):
        """Return a unambiguous string representation."""
        return (f"{self.__class__.__name__}("
                f"id={self.id!r}, "
                f"sort_as={self.sort_as!r}, "
                f"gloss_term={self.gloss_term!r}, "
                f"acronym={self.acronym!r}, "
                f"abbrev={self.abbrev!r}, "
                f"gloss_def={self.gloss_def!r}, "
                f"gloss_see={self.gloss_see!r}, "
                f"additional_properties={self.additional_properties!r})")

    def __str__(self):
        """Return a human-readable string representation."""
        return (f"{self.__class__.__name__}("
                f"id={self.id!s}, "
                f"sort_as={self.sort_as!s}, "
                f"gloss_term={self.gloss_term!s}, "
                f"acronym={self.acronym!s}, "
                f"abbrev={self.abbrev!s}, "
                f"gloss_def={self.gloss_def!s}, "
                f"gloss_see={self.gloss_see!s}, "
                f"additional_properties={self.additional_properties!s})")
