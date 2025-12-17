"""advanced_billing.

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""


class CurrentVault(object):
    """Implementation of the 'Current Vault' enum.

    The vault that stores the payment profile with the provided `vault_token`.
    Use `bogus` for testing.

    Attributes:
        ADYEN: The enum member of type str.
        AUTHORIZENET: The enum member of type str.
        AVALARA: The enum member of type str.
        BEANSTREAM: The enum member of type str.
        BLUE_SNAP: The enum member of type str.
        BOGUS: The enum member of type str.
        BRAINTREE_BLUE: The enum member of type str.
        CHECKOUT: The enum member of type str.
        CYBERSOURCE: The enum member of type str.
        ELAVON: The enum member of type str.
        EWAY: The enum member of type str.
        EWAY_RAPID_STD: The enum member of type str.
        FIRSTDATA: The enum member of type str.
        FORTE: The enum member of type str.
        GOCARDLESS: The enum member of type str.
        LITLE: The enum member of type str.
        MAXIO_PAYMENTS: The enum member of type str.
        MODUSLINK: The enum member of type str.
        MONERIS: The enum member of type str.
        NMI: The enum member of type str.
        ORBITAL: The enum member of type str.
        PAYMENT_EXPRESS: The enum member of type str.
        PIN: The enum member of type str.
        SQUARE: The enum member of type str.
        STRIPE_CONNECT: The enum member of type str.
        TRUST_COMMERCE: The enum member of type str.
        UNIPAAS: The enum member of type str.
        additional_properties (Dict[str, object]): The additional properties
            for the model.

    """

    _all_values = ["adyen", "authorizenet", "avalara", "beanstream", "blue_snap", "bogus", "braintree_blue", "checkout", "cybersource", "elavon", "eway", "eway_rapid_std", "firstdata", "forte", "gocardless", "litle", "maxio_payments", "moduslink", "moneris", "nmi", "orbital", "payment_express", "pin", "square", "stripe_connect", "trust_commerce", "unipaas"]
    ADYEN = "adyen"

    AUTHORIZENET = "authorizenet"

    AVALARA = "avalara"

    BEANSTREAM = "beanstream"

    BLUE_SNAP = "blue_snap"

    BOGUS = "bogus"

    BRAINTREE_BLUE = "braintree_blue"

    CHECKOUT = "checkout"

    CYBERSOURCE = "cybersource"

    ELAVON = "elavon"

    EWAY = "eway"

    EWAY_RAPID_STD = "eway_rapid_std"

    FIRSTDATA = "firstdata"

    FORTE = "forte"

    GOCARDLESS = "gocardless"

    LITLE = "litle"

    MAXIO_PAYMENTS = "maxio_payments"

    MODUSLINK = "moduslink"

    MONERIS = "moneris"

    NMI = "nmi"

    ORBITAL = "orbital"

    PAYMENT_EXPRESS = "payment_express"

    PIN = "pin"

    SQUARE = "square"

    STRIPE_CONNECT = "stripe_connect"

    TRUST_COMMERCE = "trust_commerce"

    UNIPAAS = "unipaas"

    @classmethod
    def validate(cls, value):
        """Validate value contains in enum

        Args:
            value: the value to be validated

        Returns:
            boolean : if value is valid enum values.

        """
        return value in cls._all_values

    @classmethod
    def from_value(cls, value, default=None):
        """Return the matching enum value for the given input."""
        if value is None:
            return default

        # If numeric and matches directly
        if isinstance(value, int):
            for name, val in cls.__dict__.items():
                if not name.startswith("_") and val == value:
                    return val

        # If string, perform case-insensitive match
        if isinstance(value, str):
            value_lower = value.lower()
            for name, val in cls.__dict__.items():
                if not name.startswith("_") and (
                    name.lower() == value_lower or str(val).lower() == value_lower
                ):
                    return val

        # Fallback to default
        return default
