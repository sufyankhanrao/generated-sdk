# -*- coding: utf-8 -*-

"""
tester

This file was automatically generated for Stamplay by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from tester.models.redirect_settings import RedirectSettings
from tester.models.signature_type import SignatureType
from tester.models.ui import Ui


class Signer(object):

    """Implementation of the 'Signer' model.

    Attributes:
        id (str): The model property of type str.
        url (str): The model property of type str.
        links (List[str]): The model property of type List[str].
        external_signer_id (str): The model property of type str.
        redirect_settings (RedirectSettings): The model property of type
            RedirectSettings.
        signature_type (SignatureType): The model property of type
            SignatureType.
        ui (Ui): The model property of type Ui.
        tags (List[str]): The model property of type List[str].
        order (int): The model property of type int.
        required (bool): The model property of type bool.
        additional_properties (Dict[str, object]): The additional properties
            for the model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "external_signer_id": 'externalSignerId',
        "id": 'id',
        "links": 'links',
        "order": 'order',
        "redirect_settings": 'redirectSettings',
        "required": 'required',
        "signature_type": 'signatureType',
        "tags": 'tags',
        "ui": 'ui',
        "url": 'url'
    }

    def __init__(self,
                 external_signer_id=None,
                 id=None,
                 links=None,
                 order=None,
                 redirect_settings=None,
                 required=None,
                 signature_type=None,
                 tags=None,
                 ui=None,
                 url=None,
                 additional_properties=None):
        """Constructor for the Signer class"""

        # Initialize members of the class
        self.id = id 
        self.url = url 
        self.links = links 
        self.external_signer_id = external_signer_id 
        self.redirect_settings = redirect_settings 
        self.signature_type = signature_type 
        self.ui = ui 
        self.tags = tags 
        self.order = order 
        self.required = required 

        # Add additional model properties to the instance
        if additional_properties is None:
            additional_properties = {}
        self.additional_properties = additional_properties

    @classmethod
    def from_dictionary(cls,
                        dictionary):
        """Creates an instance of this model from a dictionary

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
        external_signer_id = dictionary.get("externalSignerId") if dictionary.get("externalSignerId") else None
        id = dictionary.get("id") if dictionary.get("id") else None
        links = dictionary.get("links") if dictionary.get("links") else None
        order = dictionary.get("order") if dictionary.get("order") else None
        redirect_settings = RedirectSettings.from_dictionary(dictionary.get('redirectSettings')) if dictionary.get('redirectSettings') else None
        required = dictionary.get("required") if "required" in dictionary.keys() else None
        signature_type = SignatureType.from_dictionary(dictionary.get('signatureType')) if dictionary.get('signatureType') else None
        tags = dictionary.get("tags") if dictionary.get("tags") else None
        ui = Ui.from_dictionary(dictionary.get('ui')) if dictionary.get('ui') else None
        url = dictionary.get("url") if dictionary.get("url") else None
        # Clean out expected properties from dictionary
        additional_properties = {k: v for k, v in dictionary.items() if k not in cls._names.values()}
        # Return an object of this model
        return cls(external_signer_id,
                   id,
                   links,
                   order,
                   redirect_settings,
                   required,
                   signature_type,
                   tags,
                   ui,
                   url,
                   additional_properties)

    def __repr__(self):
        return (f'{self.__class__.__name__}('
                f'id={self.id!r}, '
                f'url={self.url!r}, '
                f'links={self.links!r}, '
                f'external_signer_id={self.external_signer_id!r}, '
                f'redirect_settings={self.redirect_settings!r}, '
                f'signature_type={self.signature_type!r}, '
                f'ui={self.ui!r}, '
                f'tags={self.tags!r}, '
                f'order={self.order!r}, '
                f'required={self.required!r}, '
                f'additional_properties={self.additional_properties!r})')

    def __str__(self):
        return (f'{self.__class__.__name__}('
                f'id={self.id!s}, '
                f'url={self.url!s}, '
                f'links={self.links!s}, '
                f'external_signer_id={self.external_signer_id!s}, '
                f'redirect_settings={self.redirect_settings!s}, '
                f'signature_type={self.signature_type!s}, '
                f'ui={self.ui!s}, '
                f'tags={self.tags!s}, '
                f'order={self.order!s}, '
                f'required={self.required!s}, '
                f'additional_properties={self.additional_properties!s})')
