"""tester.

This file was automatically generated for Stamplay by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

class Job(object):
    """Implementation of the 'Job' model.

    Attributes:
        company (str): The model property of type str.
        additional_properties (Dict[str, object]): The additional properties for the
            model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "company": "company",
    }

    def __init__(
        self,
        company=None,
        additional_properties=None):
        """Initialize a Job instance."""
        # Initialize members of the class
        self.company = company

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
        company =\
            dictionary.get("company")\
            if dictionary.get("company")\
                else None

        # Clean out expected properties from dictionary
        additional_properties =\
            {k: v for k, v in dictionary.items() if k not in cls._names.values()}
        # Return an object of this model
        return cls(company,
                   additional_properties)

    def __repr__(self):
        """Return a unambiguous string representation."""
        _company=self.company
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"company={_company!r}"
            f"additional_properties={_additional_properties!r}"
            f")"
        )

    def __str__(self):
        """Return a human-readable string representation."""
        _company=self.company
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"company={_company!s}"
            f"additional_properties={_additional_properties!s}"
            f")"
        )
