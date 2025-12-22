"""tester.

This file was automatically generated for Stamplay by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

from tester.models.job import Job


class AdditionalModelParameters(object):
    """Implementation of the 'AdditionalModelParameters' model.

    Attributes:
        name (str): The model property of type str.
        field (str): The model property of type str.
        address (str): The model property of type str.
        job (Job): The model property of type Job.
        additional_properties (Dict[str, object]): The additional properties for the
            model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "job": "Job",
        "address": "address",
        "field": "field",
        "name": "name",
    }

    def __init__(
        self,
        job=None,
        address=None,
        field=None,
        name=None,
        additional_properties=None):
        """Initialize a AdditionalModelParameters instance."""
        # Initialize members of the class
        self.name = name
        self.field = field
        self.address = address
        self.job = job

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
        job =\
            Job.from_dictionary(
            dictionary.get("Job"))\
                if dictionary.get("Job") else None
        address =\
            dictionary.get("address")\
            if dictionary.get("address")\
                else None
        field =\
            dictionary.get("field")\
            if dictionary.get("field")\
                else None
        name =\
            dictionary.get("name")\
            if dictionary.get("name")\
                else None

        # Clean out expected properties from dictionary
        additional_properties =\
            {k: v for k, v in dictionary.items() if k not in cls._names.values()}
        # Return an object of this model
        return cls(job,
                   address,
                   field,
                   name,
                   additional_properties)

    def __repr__(self):
        """Return a unambiguous string representation."""
        _name=self.name
        _field=self.field
        _address=self.address
        _job=self.job
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"name={_name!r}"
            f"field={_field!r}"
            f"address={_address!r}"
            f"job={_job!r}"
            f"additional_properties={_additional_properties!r}"
            f")"
        )

    def __str__(self):
        """Return a human-readable string representation."""
        _name=self.name
        _field=self.field
        _address=self.address
        _job=self.job
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"name={_name!s}"
            f"field={_field!s}"
            f"address={_address!s}"
            f"job={_job!s}"
            f"additional_properties={_additional_properties!s}"
            f")"
        )
