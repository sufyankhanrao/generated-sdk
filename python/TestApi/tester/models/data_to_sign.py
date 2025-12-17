"""tester.

This file was automatically generated for Stamplay by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

class DataToSign(object):
    """Implementation of the 'DataToSign' model.

    Attributes:
        file_name (str): The model property of type str.
        convert_to_pdf (bool): The model property of type bool.
        additional_properties (Dict[str, object]): The additional properties
            for the model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "convert_to_pdf": "convertToPDF",
        "file_name": "fileName",
    }

    def __init__(self,
                 convert_to_pdf=None,
                 file_name=None,
                 additional_properties=None):
        """Initialize a DataToSign instance."""
        # Initialize members of the class
        self.file_name = file_name
        self.convert_to_pdf = convert_to_pdf

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
        convert_to_pdf =\
            dictionary.get("convertToPDF")\
            if "convertToPDF" in dictionary.keys() else None
        file_name =\
            dictionary.get("fileName")\
            if dictionary.get("fileName") else None
        # Clean out expected properties from dictionary
        additional_properties =\
            {k: v for k, v in dictionary.items() if k not in cls._names.values()}
        # Return an object of this model
        return cls(convert_to_pdf,
                   file_name,
                   additional_properties)

    def __repr__(self):
        """Return a unambiguous string representation."""
        return (f"{self.__class__.__name__}("
                f"file_name={self.file_name!r}, "
                f"convert_to_pdf={self.convert_to_pdf!r}, "
                f"additional_properties={self.additional_properties!r})")

    def __str__(self):
        """Return a human-readable string representation."""
        return (f"{self.__class__.__name__}("
                f"file_name={self.file_name!s}, "
                f"convert_to_pdf={self.convert_to_pdf!s}, "
                f"additional_properties={self.additional_properties!s})")
