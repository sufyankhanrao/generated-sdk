"""tester.

This file was automatically generated for Stamplay by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

from tester.models.advanced import Advanced
from tester.models.contact_details import ContactDetails
from tester.models.data_to_sign import DataToSign
from tester.models.signer import Signer
from tester.models.status import Status


class Complex3(object):
    """Implementation of the 'complex3' model.

    Attributes:
        document_id (str): The model property of type str.
        signers (List[Signer]): The model property of type List[Signer].
        status (Status): The model property of type Status.
        title (str): The model property of type str.
        description (str): The model property of type str.
        external_id (str): The model property of type str.
        data_to_sign (DataToSign): The model property of type DataToSign.
        contact_details (ContactDetails): The model property of type ContactDetails.
        advanced (Advanced): The model property of type Advanced.
        additional_properties (Dict[str, object]): The additional properties for the
            model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "advanced": "advanced",
        "contact_details": "contactDetails",
        "data_to_sign": "dataToSign",
        "description": "description",
        "document_id": "documentId",
        "external_id": "externalId",
        "signers": "signers",
        "status": "status",
        "title": "title",
    }

    def __init__(
        self,
        advanced=None,
        contact_details=None,
        data_to_sign=None,
        description=None,
        document_id=None,
        external_id=None,
        signers=None,
        status=None,
        title=None,
        additional_properties=None):
        """Initialize a Complex3 instance."""
        # Initialize members of the class
        self.document_id = document_id
        self.signers = signers
        self.status = status
        self.title = title
        self.description = description
        self.external_id = external_id
        self.data_to_sign = data_to_sign
        self.contact_details = contact_details
        self.advanced = advanced

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
        advanced =\
            Advanced.from_dictionary(
            dictionary.get("advanced"))\
                if dictionary.get("advanced") else None
        contact_details =\
            ContactDetails.from_dictionary(
            dictionary.get("contactDetails"))\
                if dictionary.get("contactDetails") else None
        data_to_sign =\
            DataToSign.from_dictionary(
            dictionary.get("dataToSign"))\
                if dictionary.get("dataToSign") else None
        description =\
            dictionary.get("description")\
            if dictionary.get("description")\
                else None
        document_id =\
            dictionary.get("documentId")\
            if dictionary.get("documentId")\
                else None
        external_id =\
            dictionary.get("externalId")\
            if dictionary.get("externalId")\
                else None
        signers = None
        if dictionary.get("signers") is not None:
            signers = [
                Signer.from_dictionary(x)
                    for x in dictionary.get("signers")
            ]
        status =\
            Status.from_dictionary(
            dictionary.get("status"))\
                if dictionary.get("status") else None
        title =\
            dictionary.get("title")\
            if dictionary.get("title")\
                else None

        # Clean out expected properties from dictionary
        additional_properties =\
            {k: v for k, v in dictionary.items() if k not in cls._names.values()}
        # Return an object of this model
        return cls(advanced,
                   contact_details,
                   data_to_sign,
                   description,
                   document_id,
                   external_id,
                   signers,
                   status,
                   title,
                   additional_properties)

    def __repr__(self):
        """Return a unambiguous string representation."""
        _document_id=self.document_id
        _signers=self.signers
        _status=self.status
        _title=self.title
        _description=self.description
        _external_id=self.external_id
        _data_to_sign=self.data_to_sign
        _contact_details=self.contact_details
        _advanced=self.advanced
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"document_id={_document_id!r}"
            f"signers={_signers!r}"
            f"status={_status!r}"
            f"title={_title!r}"
            f"description={_description!r}"
            f"external_id={_external_id!r}"
            f"data_to_sign={_data_to_sign!r}"
            f"contact_details={_contact_details!r}"
            f"advanced={_advanced!r}"
            f"additional_properties={_additional_properties!r}"
            f")"
        )

    def __str__(self):
        """Return a human-readable string representation."""
        _document_id=self.document_id
        _signers=self.signers
        _status=self.status
        _title=self.title
        _description=self.description
        _external_id=self.external_id
        _data_to_sign=self.data_to_sign
        _contact_details=self.contact_details
        _advanced=self.advanced
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"document_id={_document_id!s}"
            f"signers={_signers!s}"
            f"status={_status!s}"
            f"title={_title!s}"
            f"description={_description!s}"
            f"external_id={_external_id!s}"
            f"data_to_sign={_data_to_sign!s}"
            f"contact_details={_contact_details!s}"
            f"advanced={_advanced!s}"
            f"additional_properties={_additional_properties!s}"
            f")"
        )
