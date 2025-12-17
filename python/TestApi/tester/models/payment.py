"""tester.

This file was automatically generated for Stamplay by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

class Payment(object):
    """Implementation of the 'Payment' model.

    Attributes:
        payment_type (str): The model property of type str.
        additional_properties (Dict[str, object]): The additional properties
            for the model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "payment_type": "paymentType",
    }

    _optionals = [
        "payment_type",
    ]

    def __init__(self,
                 payment_type="Payment",
                 additional_properties=None):
        """Initialize a Payment instance."""
        # Initialize members of the class
        self.payment_type = payment_type

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

        discriminators = {
            "CARD": PaymentCard.from_dictionary,
            "CASH": PaymentCash.from_dictionary,
        }
        unboxer = discriminators.get(dictionary.get("paymentType"))

        # Delegate unboxing to another function if a discriminator
        # value for a child class is present.
        if unboxer:
            return unboxer(dictionary)

        # Extract variables from the dictionary
        payment_type =\
            dictionary.get("paymentType")\
            if dictionary.get("paymentType") else "Payment"
        # Clean out expected properties from dictionary
        additional_properties =\
            {k: v for k, v in dictionary.items() if k not in cls._names.values()}
        # Return an object of this model
        return cls(payment_type,
                   additional_properties)

    def __repr__(self):
        """Return a unambiguous string representation."""
        return (f"{self.__class__.__name__}("
                f"payment_type={(self.payment_type
                     if hasattr(self, 'payment_type') else None)!r}, "
                f"additional_properties={self.additional_properties!r})")

    def __str__(self):
        """Return a human-readable string representation."""
        return (f"{self.__class__.__name__}("
                f"payment_type={(self.payment_type
                     if hasattr(self, 'payment_type') else None)!s}, "
                f"additional_properties={self.additional_properties!s})")

class PaymentCard(Payment):
    """Implementation of the 'PaymentCard' model.
    NOTE: This class inherits from 'Payment'.

    Attributes:
        swiped (bool): The model property of type bool.
        additional_properties (Dict[str, object]): The additional properties
            for the model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "swiped": "swiped",
        "payment_type": "paymentType",
    }

    def __init__(self,
                 swiped=None,
                 payment_type="CARD",
                 additional_properties=None):
        """Initialize a PaymentCard instance."""
        # Initialize members of the class
        self.swiped = swiped

        # Call the constructor for the base class
        super(PaymentCard, self).__init__(payment_type,
                                          additional_properties)

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
        swiped =\
            dictionary.get("swiped")\
            if "swiped" in dictionary.keys() else None
        payment_type =\
            dictionary.get("paymentType")\
            if dictionary.get("paymentType") else "CARD"
        # Clean out expected properties from dictionary
        additional_properties =\
            {k: v for k, v in dictionary.items() if k not in cls._names.values()}
        # Return an object of this model
        return cls(swiped,
                   payment_type,
                   additional_properties)

    def __repr__(self):
        """Return a unambiguous string representation."""
        base_repr = super().__repr__()
        return (f"{self.__class__.__name__}("
                f"{base_repr[base_repr.find('(') + 1:-1]}, "
                f"swiped={self.swiped!r})")

    def __str__(self):
        """Return a human-readable string representation."""
        base_str = super().__str__()
        return (f"{self.__class__.__name__}("
                f"{base_str[base_str.find('(') + 1:-1]}, "
                f"swiped={self.swiped!s})")

class PaymentCash(Payment):
    """Implementation of the 'PaymentCash' model.
    NOTE: This class inherits from 'Payment'.

    Attributes:
        received (bool): The model property of type bool.
        additional_properties (Dict[str, object]): The additional properties
            for the model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "received": "received",
        "payment_type": "paymentType",
    }

    def __init__(self,
                 received=None,
                 payment_type="CASH",
                 additional_properties=None):
        """Initialize a PaymentCash instance."""
        # Initialize members of the class
        self.received = received

        # Call the constructor for the base class
        super(PaymentCash, self).__init__(payment_type,
                                          additional_properties)

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
        received =\
            dictionary.get("received")\
            if "received" in dictionary.keys() else None
        payment_type =\
            dictionary.get("paymentType")\
            if dictionary.get("paymentType") else "CASH"
        # Clean out expected properties from dictionary
        additional_properties =\
            {k: v for k, v in dictionary.items() if k not in cls._names.values()}
        # Return an object of this model
        return cls(received,
                   payment_type,
                   additional_properties)

    def __repr__(self):
        """Return a unambiguous string representation."""
        base_repr = super().__repr__()
        return (f"{self.__class__.__name__}("
                f"{base_repr[base_repr.find('(') + 1:-1]}, "
                f"received={self.received!r})")

    def __str__(self):
        """Return a human-readable string representation."""
        base_str = super().__str__()
        return (f"{self.__class__.__name__}("
                f"{base_str[base_str.find('(') + 1:-1]}, "
                f"received={self.received!s})")
