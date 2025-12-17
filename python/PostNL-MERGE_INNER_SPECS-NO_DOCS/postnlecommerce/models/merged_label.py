"""postnlecommerce.

This file was automatically generated for PostNL by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

from postnlecommerce.api_helper import APIHelper
from postnlecommerce.models.label import Label


class MergedLabel(object):
    """Implementation of the 'MergedLabel' model.

    Attributes:
        barcodes (List[str]): The model property of type List[str].
        labels (List[Label]): The model property of type List[Label].

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "barcodes": "Barcodes",
        "labels": "Labels",
    }

    _optionals = [
        "barcodes",
        "labels",
    ]

    def __init__(self,
                 barcodes=APIHelper.SKIP,
                 labels=APIHelper.SKIP):
        """Initialize a MergedLabel instance."""
        # Initialize members of the class
        if barcodes is not APIHelper.SKIP:
            self.barcodes = barcodes
        if labels is not APIHelper.SKIP:
            self.labels = labels

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
        barcodes =\
            dictionary.get("Barcodes")\
            if dictionary.get("Barcodes") else APIHelper.SKIP
        labels = None
        if dictionary.get("Labels") is not None:
            labels = [
                Label.from_dictionary(x)
                    for x in dictionary.get("Labels")
            ]
        else:
            labels = APIHelper.SKIP
        # Return an object of this model
        return cls(barcodes,
                   labels)

    def __repr__(self):
        """Return a unambiguous string representation."""
        return (f"{self.__class__.__name__}("
                f"barcodes={(self.barcodes
                     if hasattr(self, 'barcodes') else None)!r}, "
                f"labels={(self.labels if hasattr(self, 'labels') else None)!r})")

    def __str__(self):
        """Return a human-readable string representation."""
        return (f"{self.__class__.__name__}("
                f"barcodes={(self.barcodes
                     if hasattr(self, 'barcodes') else None)!s}, "
                f"labels={(self.labels if hasattr(self, 'labels') else None)!s})")
