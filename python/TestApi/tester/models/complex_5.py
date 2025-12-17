"""tester.

This file was automatically generated for Stamplay by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

from tester.models.response_data import ResponseData


class Complex5(object):
    """Implementation of the 'complex5' model.

    Attributes:
        response_data (ResponseData): The model property of type ResponseData.
        response_details (str): The model property of type str.
        response_status (int): The model property of type int.
        additional_properties (Dict[str, object]): The additional properties
            for the model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "response_data": "responseData",
        "response_details": "responseDetails",
        "response_status": "responseStatus",
    }

    _nullables = [
        "response_details",
    ]

    def __init__(self,
                 response_data=None,
                 response_details=None,
                 response_status=None,
                 additional_properties=None):
        """Initialize a Complex5 instance."""
        # Initialize members of the class
        self.response_data = response_data
        self.response_details = response_details
        self.response_status = response_status

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
        response_data = ResponseData.from_dictionary(
            dictionary.get("responseData"))\
            if dictionary.get("responseData") else None
        response_details =\
            dictionary.get("responseDetails")\
            if dictionary.get("responseDetails") else None
        response_status =\
            dictionary.get("responseStatus")\
            if dictionary.get("responseStatus") else None
        # Clean out expected properties from dictionary
        additional_properties =\
            {k: v for k, v in dictionary.items() if k not in cls._names.values()}
        # Return an object of this model
        return cls(response_data,
                   response_details,
                   response_status,
                   additional_properties)

    def __repr__(self):
        """Return a unambiguous string representation."""
        return (f"{self.__class__.__name__}("
                f"response_data={self.response_data!r}, "
                f"response_details={self.response_details!r}, "
                f"response_status={self.response_status!r}, "
                f"additional_properties={self.additional_properties!r})")

    def __str__(self):
        """Return a human-readable string representation."""
        return (f"{self.__class__.__name__}("
                f"response_data={self.response_data!s}, "
                f"response_details={self.response_details!s}, "
                f"response_status={self.response_status!s}, "
                f"additional_properties={self.additional_properties!s})")
