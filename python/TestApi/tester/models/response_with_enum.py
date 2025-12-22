"""tester.

This file was automatically generated for Stamplay by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

from tester.models.attributes import Attributes


class ResponseWithEnum(object):
    """Implementation of the 'response with Enum' model.

    Attributes:
        param_format (ParamFormatEnum): The model property of type ParamFormatEnum.
        optional (bool): The model property of type bool.
        mtype (TypeEnum): The model property of type TypeEnum.
        constant (bool): The model property of type bool.
        is_array (bool): The model property of type bool.
        is_stream (bool): The model property of type bool.
        is_attribute (bool): The model property of type bool.
        is_map (bool): The model property of type bool.
        attributes (Attributes): The model property of type Attributes.
        nullable (bool): The model property of type bool.
        id (str): The model property of type str.
        name (str): The model property of type str.
        description (str): The model property of type str.
        additional_properties (Dict[str, object]): The additional properties for the
            model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "attributes": "attributes",
        "constant": "constant",
        "description": "description",
        "id": "id",
        "is_array": "isArray",
        "is_attribute": "isAttribute",
        "is_map": "isMap",
        "is_stream": "isStream",
        "name": "name",
        "nullable": "nullable",
        "optional": "optional",
        "param_format": "paramFormat",
        "mtype": "type",
    }

    def __init__(
        self,
        attributes=None,
        constant=None,
        description=None,
        id=None,
        is_array=None,
        is_attribute=None,
        is_map=None,
        is_stream=None,
        name=None,
        nullable=None,
        optional=None,
        param_format=None,
        mtype=None,
        additional_properties=None):
        """Initialize a ResponseWithEnum instance."""
        # Initialize members of the class
        self.param_format = param_format
        self.optional = optional
        self.mtype = mtype
        self.constant = constant
        self.is_array = is_array
        self.is_stream = is_stream
        self.is_attribute = is_attribute
        self.is_map = is_map
        self.attributes = attributes
        self.nullable = nullable
        self.id = id
        self.name = name
        self.description = description

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
        attributes =\
            Attributes.from_dictionary(
            dictionary.get("attributes"))\
                if dictionary.get("attributes") else None
        constant =\
            dictionary.get("constant")\
            if "constant" in dictionary.keys()\
                else None
        description =\
            dictionary.get("description")\
            if dictionary.get("description")\
                else None
        id =\
            dictionary.get("id")\
            if dictionary.get("id")\
                else None
        is_array =\
            dictionary.get("isArray")\
            if "isArray" in dictionary.keys()\
                else None
        is_attribute =\
            dictionary.get("isAttribute")\
            if "isAttribute" in dictionary.keys()\
                else None
        is_map =\
            dictionary.get("isMap")\
            if "isMap" in dictionary.keys()\
                else None
        is_stream =\
            dictionary.get("isStream")\
            if "isStream" in dictionary.keys()\
                else None
        name =\
            dictionary.get("name")\
            if dictionary.get("name")\
                else None
        nullable =\
            dictionary.get("nullable")\
            if "nullable" in dictionary.keys()\
                else None
        optional =\
            dictionary.get("optional")\
            if "optional" in dictionary.keys()\
                else None
        param_format =\
            dictionary.get("paramFormat")\
            if dictionary.get("paramFormat")\
                else None
        mtype =\
            dictionary.get("type")\
            if dictionary.get("type")\
                else None

        # Clean out expected properties from dictionary
        additional_properties =\
            {k: v for k, v in dictionary.items() if k not in cls._names.values()}
        # Return an object of this model
        return cls(attributes,
                   constant,
                   description,
                   id,
                   is_array,
                   is_attribute,
                   is_map,
                   is_stream,
                   name,
                   nullable,
                   optional,
                   param_format,
                   mtype,
                   additional_properties)

    def __repr__(self):
        """Return a unambiguous string representation."""
        _param_format=self.param_format
        _optional=self.optional
        _mtype=self.mtype
        _constant=self.constant
        _is_array=self.is_array
        _is_stream=self.is_stream
        _is_attribute=self.is_attribute
        _is_map=self.is_map
        _attributes=self.attributes
        _nullable=self.nullable
        _id=self.id
        _name=self.name
        _description=self.description
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"param_format={_param_format!r}"
            f"optional={_optional!r}"
            f"mtype={_mtype!r}"
            f"constant={_constant!r}"
            f"is_array={_is_array!r}"
            f"is_stream={_is_stream!r}"
            f"is_attribute={_is_attribute!r}"
            f"is_map={_is_map!r}"
            f"attributes={_attributes!r}"
            f"nullable={_nullable!r}"
            f"id={_id!r}"
            f"name={_name!r}"
            f"description={_description!r}"
            f"additional_properties={_additional_properties!r}"
            f")"
        )

    def __str__(self):
        """Return a human-readable string representation."""
        _param_format=self.param_format
        _optional=self.optional
        _mtype=self.mtype
        _constant=self.constant
        _is_array=self.is_array
        _is_stream=self.is_stream
        _is_attribute=self.is_attribute
        _is_map=self.is_map
        _attributes=self.attributes
        _nullable=self.nullable
        _id=self.id
        _name=self.name
        _description=self.description
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"param_format={_param_format!s}"
            f"optional={_optional!s}"
            f"mtype={_mtype!s}"
            f"constant={_constant!s}"
            f"is_array={_is_array!s}"
            f"is_stream={_is_stream!s}"
            f"is_attribute={_is_attribute!s}"
            f"is_map={_is_map!s}"
            f"attributes={_attributes!s}"
            f"nullable={_nullable!s}"
            f"id={_id!s}"
            f"name={_name!s}"
            f"description={_description!s}"
            f"additional_properties={_additional_properties!s}"
            f")"
        )
