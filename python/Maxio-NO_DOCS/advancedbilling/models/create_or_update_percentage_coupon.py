"""advanced_billing.

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

from advancedbilling.api_helper import APIHelper


class CreateOrUpdatePercentageCoupon(object):
    """Implementation of the 'Create or Update Percentage Coupon' model.

    Attributes:
        name (str): the name of the coupon
        code (str): may contain uppercase alphanumeric characters and these
            special characters (which allow for email addresses to be used):
            “%”, “@”, “+”, “-”, “_”, and “.”
        description (str): The model property of type str.
        percentage (str | float): The model property of type str | float.
        allow_negative_balance (bool): The model property of type bool.
        recurring (bool): The model property of type bool.
        end_date (datetime): The model property of type datetime.
        product_family_id (str): The model property of type str.
        stackable (bool): The model property of type bool.
        compounding_strategy (CompoundingStrategy): The model property of type
            CompoundingStrategy.
        exclude_mid_period_allocations (bool): The model property of type bool.
        apply_on_cancel_at_end_of_period (bool): The model property of type
            bool.
        apply_on_subscription_expiration (bool): The model property of type
            bool.
        additional_properties (Dict[str, object]): The additional properties
            for the model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "name": "name",
        "code": "code",
        "percentage": "percentage",
        "description": "description",
        "allow_negative_balance": "allow_negative_balance",
        "recurring": "recurring",
        "end_date": "end_date",
        "product_family_id": "product_family_id",
        "stackable": "stackable",
        "compounding_strategy": "compounding_strategy",
        "exclude_mid_period_allocations": "exclude_mid_period_allocations",
        "apply_on_cancel_at_end_of_period": "apply_on_cancel_at_end_of_period",
        "apply_on_subscription_expiration": "apply_on_subscription_expiration",
    }

    _optionals = [
        "description",
        "allow_negative_balance",
        "recurring",
        "end_date",
        "product_family_id",
        "stackable",
        "compounding_strategy",
        "exclude_mid_period_allocations",
        "apply_on_cancel_at_end_of_period",
        "apply_on_subscription_expiration",
    ]

    def __init__(self,
                 name=None,
                 code=None,
                 percentage=None,
                 description=APIHelper.SKIP,
                 allow_negative_balance=APIHelper.SKIP,
                 recurring=APIHelper.SKIP,
                 end_date=APIHelper.SKIP,
                 product_family_id=APIHelper.SKIP,
                 stackable=APIHelper.SKIP,
                 compounding_strategy=APIHelper.SKIP,
                 exclude_mid_period_allocations=APIHelper.SKIP,
                 apply_on_cancel_at_end_of_period=APIHelper.SKIP,
                 apply_on_subscription_expiration=APIHelper.SKIP,
                 additional_properties=None):
        """Initialize a CreateOrUpdatePercentageCoupon instance."""
        # Initialize members of the class
        self.name = name
        self.code = code
        if description is not APIHelper.SKIP:
            self.description = description
        self.percentage = percentage
        if allow_negative_balance is not APIHelper.SKIP:
            self.allow_negative_balance = allow_negative_balance
        if recurring is not APIHelper.SKIP:
            self.recurring = recurring
        if end_date is not APIHelper.SKIP:
            self.end_date =\
                 APIHelper.apply_datetime_converter(
                end_date, APIHelper.RFC3339DateTime) if end_date else None
        if product_family_id is not APIHelper.SKIP:
            self.product_family_id = product_family_id
        if stackable is not APIHelper.SKIP:
            self.stackable = stackable
        if compounding_strategy is not APIHelper.SKIP:
            self.compounding_strategy = compounding_strategy
        if exclude_mid_period_allocations is not APIHelper.SKIP:
            self.exclude_mid_period_allocations = exclude_mid_period_allocations
        if apply_on_cancel_at_end_of_period is not APIHelper.SKIP:
            self.apply_on_cancel_at_end_of_period = apply_on_cancel_at_end_of_period
        if apply_on_subscription_expiration is not APIHelper.SKIP:
            self.apply_on_subscription_expiration = apply_on_subscription_expiration

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
        from advancedbilling.utilities.union_type_lookup import (
            UnionTypeLookUp,
        )

        if not isinstance(dictionary, dict) or dictionary is None:
            return None

        # Extract variables from the dictionary
        name = dictionary.get("name") if dictionary.get("name") else None
        code = dictionary.get("code") if dictionary.get("code") else None
        percentage = APIHelper.deserialize_union_type(UnionTypeLookUp.get("CreateOrUpdatePercentageCouponPercentage"), dictionary.get("percentage"), False) if dictionary.get("percentage") is not None else None
        description =\
            dictionary.get("description")\
            if dictionary.get("description") else APIHelper.SKIP
        allow_negative_balance =\
            dictionary.get("allow_negative_balance")\
            if "allow_negative_balance" in dictionary.keys() else APIHelper.SKIP
        recurring =\
            dictionary.get("recurring")\
            if "recurring" in dictionary.keys() else APIHelper.SKIP
        end_date = APIHelper.RFC3339DateTime.from_value(
            dictionary.get("end_date")).datetime\
            if dictionary.get("end_date") else APIHelper.SKIP
        product_family_id =\
            dictionary.get("product_family_id")\
            if dictionary.get("product_family_id") else APIHelper.SKIP
        stackable =\
            dictionary.get("stackable")\
            if "stackable" in dictionary.keys() else APIHelper.SKIP
        compounding_strategy =\
            dictionary.get("compounding_strategy")\
            if dictionary.get("compounding_strategy") else APIHelper.SKIP
        exclude_mid_period_allocations =\
            dictionary.get("exclude_mid_period_allocations")\
            if "exclude_mid_period_allocations" in dictionary.keys() else APIHelper.SKIP
        apply_on_cancel_at_end_of_period =\
            dictionary.get("apply_on_cancel_at_end_of_period")\
            if "apply_on_cancel_at_end_of_period" in dictionary.keys() else APIHelper.SKIP
        apply_on_subscription_expiration =\
            dictionary.get("apply_on_subscription_expiration")\
            if "apply_on_subscription_expiration" in dictionary.keys() else APIHelper.SKIP
        # Clean out expected properties from dictionary
        additional_properties =\
            {k: v for k, v in dictionary.items() if k not in cls._names.values()}
        # Return an object of this model
        return cls(name,
                   code,
                   percentage,
                   description,
                   allow_negative_balance,
                   recurring,
                   end_date,
                   product_family_id,
                   stackable,
                   compounding_strategy,
                   exclude_mid_period_allocations,
                   apply_on_cancel_at_end_of_period,
                   apply_on_subscription_expiration,
                   additional_properties)

    @classmethod
    def validate(cls, dictionary):
        """Validate dictionary against class required properties

        Args:
            dictionary (dictionary): A dictionary representation of the object
            as obtained from the deserialization of the server's response. The
            keys MUST match property names in the API description.

        Returns:
            boolean : if dictionary is valid contains required properties.

        """
        from advancedbilling.utilities.union_type_lookup import (
            UnionTypeLookUp,
        )

        if isinstance(dictionary, cls):
            return APIHelper.is_valid_type(
                value=dictionary.name,
                type_callable=lambda value: isinstance(value, str)) \
                and APIHelper.is_valid_type(
                value=dictionary.code,
                type_callable=lambda value: isinstance(value, str)) \
                and UnionTypeLookUp.get("CreateOrUpdatePercentageCouponPercentage").validate(dictionary.percentage).is_valid

        if not isinstance(dictionary, dict):
            return False

        return APIHelper.is_valid_type(
            value=dictionary.get("name"),
            type_callable=lambda value: isinstance(value, str)) \
            and APIHelper.is_valid_type(
            value=dictionary.get("code"),
            type_callable=lambda value: isinstance(value, str)) \
            and UnionTypeLookUp.get("CreateOrUpdatePercentageCouponPercentage").validate(dictionary.get("percentage")).is_valid

    def __repr__(self):
        """Return a unambiguous string representation."""
        return (f"{self.__class__.__name__}("
                f"name={self.name!r}, "
                f"code={self.code!r}, "
                f"description={(self.description
                     if hasattr(self, 'description') else None)!r}, "
                f"percentage={self.percentage!r}, "
                f"allow_negative_balance={(self.allow_negative_balance
                     if hasattr(self, 'allow_negative_balance') else None)!r}, "
                f"recurring={(self.recurring
                     if hasattr(self, 'recurring') else None)!r}, "
                f"end_date={(self.end_date
                     if hasattr(self, 'end_date') else None)!r}, "
                f"product_family_id={(self.product_family_id
                     if hasattr(self, 'product_family_id') else None)!r}, "
                f"stackable={(self.stackable
                     if hasattr(self, 'stackable') else None)!r}, "
                f"compounding_strategy={(self.compounding_strategy
                     if hasattr(self, 'compounding_strategy') else None)!r}, "
                f"exclude_mid_period_allocations={(self.exclude_mid_period_allocations
                     if hasattr(self, 'exclude_mid_period_allocations') else None)!r}, "
                f"apply_on_cancel_at_end_of_period={(self.apply_on_cancel_at_end_of_period
                     if hasattr(self, 'apply_on_cancel_at_end_of_period') else None)!r}, "
                f"apply_on_subscription_expiration={(self.apply_on_subscription_expiration
                     if hasattr(self, 'apply_on_subscription_expiration') else None)!r}, "
                f"additional_properties={self.additional_properties!r})")

    def __str__(self):
        """Return a human-readable string representation."""
        return (f"{self.__class__.__name__}("
                f"name={self.name!s}, "
                f"code={self.code!s}, "
                f"description={(self.description
                     if hasattr(self, 'description') else None)!s}, "
                f"percentage={self.percentage!s}, "
                f"allow_negative_balance={(self.allow_negative_balance
                     if hasattr(self, 'allow_negative_balance') else None)!s}, "
                f"recurring={(self.recurring
                     if hasattr(self, 'recurring') else None)!s}, "
                f"end_date={(self.end_date
                     if hasattr(self, 'end_date') else None)!s}, "
                f"product_family_id={(self.product_family_id
                     if hasattr(self, 'product_family_id') else None)!s}, "
                f"stackable={(self.stackable
                     if hasattr(self, 'stackable') else None)!s}, "
                f"compounding_strategy={(self.compounding_strategy
                     if hasattr(self, 'compounding_strategy') else None)!s}, "
                f"exclude_mid_period_allocations={(self.exclude_mid_period_allocations
                     if hasattr(self, 'exclude_mid_period_allocations') else None)!s}, "
                f"apply_on_cancel_at_end_of_period={(self.apply_on_cancel_at_end_of_period
                     if hasattr(self, 'apply_on_cancel_at_end_of_period') else None)!s}, "
                f"apply_on_subscription_expiration={(self.apply_on_subscription_expiration
                     if hasattr(self, 'apply_on_subscription_expiration') else None)!s}, "
                f"additional_properties={self.additional_properties!s})")
