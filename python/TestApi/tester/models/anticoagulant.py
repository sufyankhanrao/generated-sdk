"""tester.

This file was automatically generated for Stamplay by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

class Anticoagulant(object):
    """Implementation of the 'Anticoagulant' model.

    Attributes:
        name (str): The model property of type str.
        strength (str): The model property of type str.
        dose (str): The model property of type str.
        route (str): The model property of type str.
        sig (str): The model property of type str.
        pill_count (str): The model property of type str.
        refills (str): The model property of type str.
        additional_properties (Dict[str, object]): The additional properties
            for the model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "dose": "dose",
        "name": "name",
        "pill_count": "pillCount",
        "refills": "refills",
        "route": "route",
        "sig": "sig",
        "strength": "strength",
    }

    def __init__(self,
                 dose=None,
                 name=None,
                 pill_count=None,
                 refills=None,
                 route=None,
                 sig=None,
                 strength=None,
                 additional_properties=None):
        """Initialize a Anticoagulant instance."""
        # Initialize members of the class
        self.name = name
        self.strength = strength
        self.dose = dose
        self.route = route
        self.sig = sig
        self.pill_count = pill_count
        self.refills = refills

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
        dose = dictionary.get("dose") if dictionary.get("dose") else None
        name = dictionary.get("name") if dictionary.get("name") else None
        pill_count =\
            dictionary.get("pillCount")\
            if dictionary.get("pillCount") else None
        refills = dictionary.get("refills") if dictionary.get("refills") else None
        route = dictionary.get("route") if dictionary.get("route") else None
        sig = dictionary.get("sig") if dictionary.get("sig") else None
        strength =\
            dictionary.get("strength")\
            if dictionary.get("strength") else None
        # Clean out expected properties from dictionary
        additional_properties =\
            {k: v for k, v in dictionary.items() if k not in cls._names.values()}
        # Return an object of this model
        return cls(dose,
                   name,
                   pill_count,
                   refills,
                   route,
                   sig,
                   strength,
                   additional_properties)

    def __repr__(self):
        """Return a unambiguous string representation."""
        return (f"{self.__class__.__name__}("
                f"name={self.name!r}, "
                f"strength={self.strength!r}, "
                f"dose={self.dose!r}, "
                f"route={self.route!r}, "
                f"sig={self.sig!r}, "
                f"pill_count={self.pill_count!r}, "
                f"refills={self.refills!r}, "
                f"additional_properties={self.additional_properties!r})")

    def __str__(self):
        """Return a human-readable string representation."""
        return (f"{self.__class__.__name__}("
                f"name={self.name!s}, "
                f"strength={self.strength!s}, "
                f"dose={self.dose!s}, "
                f"route={self.route!s}, "
                f"sig={self.sig!s}, "
                f"pill_count={self.pill_count!s}, "
                f"refills={self.refills!s}, "
                f"additional_properties={self.additional_properties!s})")
