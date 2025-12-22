"""tester.

This file was automatically generated for Stamplay by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

class Status(object):
    """Implementation of the 'Status' model.

    Attributes:
        document_status (str): The model property of type str.
        completed_packages (List[str]): The model property of type List[str].
        attachment_packages (Any): The model property of type Any.
        additional_properties (Dict[str, object]): The additional properties for the
            model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "attachment_packages": "attachmentPackages",
        "completed_packages": "completedPackages",
        "document_status": "documentStatus",
    }

    def __init__(
        self,
        attachment_packages=None,
        completed_packages=None,
        document_status=None,
        additional_properties=None):
        """Initialize a Status instance."""
        # Initialize members of the class
        self.document_status = document_status
        self.completed_packages = completed_packages
        self.attachment_packages = attachment_packages

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
        attachment_packages =\
            dictionary.get("attachmentPackages")\
            if dictionary.get("attachmentPackages")\
                else None
        completed_packages =\
            dictionary.get("completedPackages")\
            if dictionary.get("completedPackages")\
                else None
        document_status =\
            dictionary.get("documentStatus")\
            if dictionary.get("documentStatus")\
                else None

        # Clean out expected properties from dictionary
        additional_properties =\
            {k: v for k, v in dictionary.items() if k not in cls._names.values()}
        # Return an object of this model
        return cls(attachment_packages,
                   completed_packages,
                   document_status,
                   additional_properties)

    def __repr__(self):
        """Return a unambiguous string representation."""
        _document_status=self.document_status
        _completed_packages=self.completed_packages
        _attachment_packages=self.attachment_packages
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"document_status={_document_status!r}"
            f"completed_packages={_completed_packages!r}"
            f"attachment_packages={_attachment_packages!r}"
            f"additional_properties={_additional_properties!r}"
            f")"
        )

    def __str__(self):
        """Return a human-readable string representation."""
        _document_status=self.document_status
        _completed_packages=self.completed_packages
        _attachment_packages=self.attachment_packages
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"document_status={_document_status!s}"
            f"completed_packages={_completed_packages!s}"
            f"attachment_packages={_attachment_packages!s}"
            f"additional_properties={_additional_properties!s}"
            f")"
        )
