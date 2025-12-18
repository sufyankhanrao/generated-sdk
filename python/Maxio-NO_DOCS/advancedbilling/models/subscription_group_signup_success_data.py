# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.api_helper import APIHelper


class SubscriptionGroupSignupSuccessData(object):

    """Implementation of the 'Subscription Group Signup Success Data' model.

    Attributes:
        uid (str): The model property of type str.
        scheme (int): The model property of type int.
        customer_id (int): The model property of type int.
        payment_profile_id (int): The model property of type int.
        subscription_ids (List[int]): The model property of type List[int].
        primary_subscription_id (int): The model property of type int.
        next_assessment_at (datetime): The model property of type datetime.
        state (str): The model property of type str.
        cancel_at_end_of_period (bool): The model property of type bool.
        additional_properties (Dict[str, object]): The additional properties
            for the model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "uid": 'uid',
        "scheme": 'scheme',
        "customer_id": 'customer_id',
        "payment_profile_id": 'payment_profile_id',
        "subscription_ids": 'subscription_ids',
        "primary_subscription_id": 'primary_subscription_id',
        "next_assessment_at": 'next_assessment_at',
        "state": 'state',
        "cancel_at_end_of_period": 'cancel_at_end_of_period'
    }

    def __init__(self,
                 uid=None,
                 scheme=None,
                 customer_id=None,
                 payment_profile_id=None,
                 subscription_ids=None,
                 primary_subscription_id=None,
                 next_assessment_at=None,
                 state=None,
                 cancel_at_end_of_period=None,
                 additional_properties=None):
        """Constructor for the SubscriptionGroupSignupSuccessData class"""

        # Initialize members of the class
        self.uid = uid 
        self.scheme = scheme 
        self.customer_id = customer_id 
        self.payment_profile_id = payment_profile_id 
        self.subscription_ids = subscription_ids 
        self.primary_subscription_id = primary_subscription_id 
        self.next_assessment_at = APIHelper.apply_datetime_converter(next_assessment_at, APIHelper.RFC3339DateTime) if next_assessment_at else None 
        self.state = state 
        self.cancel_at_end_of_period = cancel_at_end_of_period 

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
        uid = dictionary.get("uid") if dictionary.get("uid") else None
        scheme = dictionary.get("scheme") if dictionary.get("scheme") else None
        customer_id = dictionary.get("customer_id") if dictionary.get("customer_id") else None
        payment_profile_id = dictionary.get("payment_profile_id") if dictionary.get("payment_profile_id") else None
        subscription_ids = dictionary.get("subscription_ids") if dictionary.get("subscription_ids") else None
        primary_subscription_id = dictionary.get("primary_subscription_id") if dictionary.get("primary_subscription_id") else None
        next_assessment_at = APIHelper.RFC3339DateTime.from_value(dictionary.get("next_assessment_at")).datetime if dictionary.get("next_assessment_at") else None
        state = dictionary.get("state") if dictionary.get("state") else None
        cancel_at_end_of_period = dictionary.get("cancel_at_end_of_period") if "cancel_at_end_of_period" in dictionary.keys() else None
        # Clean out expected properties from dictionary
        additional_properties = {k: v for k, v in dictionary.items() if k not in cls._names.values()}
        # Return an object of this model
        return cls(uid,
                   scheme,
                   customer_id,
                   payment_profile_id,
                   subscription_ids,
                   primary_subscription_id,
                   next_assessment_at,
                   state,
                   cancel_at_end_of_period,
                   additional_properties)

    @classmethod
    def validate(cls, dictionary):
        """Validates dictionary against class required properties

        Args:
            dictionary (dictionary): A dictionary representation of the object
            as obtained from the deserialization of the server's response. The
            keys MUST match property names in the API description.

        Returns:
            boolean : if dictionary is valid contains required properties.

        """

        if isinstance(dictionary, cls):
            return APIHelper.is_valid_type(value=dictionary.uid,
                                           type_callable=lambda value: isinstance(value, str)) \
                and APIHelper.is_valid_type(value=dictionary.scheme,
                                            type_callable=lambda value: isinstance(value, int)) \
                and APIHelper.is_valid_type(value=dictionary.customer_id,
                                            type_callable=lambda value: isinstance(value, int)) \
                and APIHelper.is_valid_type(value=dictionary.payment_profile_id,
                                            type_callable=lambda value: isinstance(value, int)) \
                and APIHelper.is_valid_type(value=dictionary.subscription_ids,
                                            type_callable=lambda value: isinstance(value, int)) \
                and APIHelper.is_valid_type(value=dictionary.primary_subscription_id,
                                            type_callable=lambda value: isinstance(value, int)) \
                and APIHelper.is_valid_type(value=dictionary.next_assessment_at,
                                            type_callable=lambda value: isinstance(value, APIHelper.RFC3339DateTime)) \
                and APIHelper.is_valid_type(value=dictionary.state,
                                            type_callable=lambda value: isinstance(value, str)) \
                and APIHelper.is_valid_type(value=dictionary.cancel_at_end_of_period,
                                            type_callable=lambda value: isinstance(value, bool))

        if not isinstance(dictionary, dict):
            return False

        return APIHelper.is_valid_type(value=dictionary.get('uid'),
                                       type_callable=lambda value: isinstance(value, str)) \
            and APIHelper.is_valid_type(value=dictionary.get('scheme'),
                                        type_callable=lambda value: isinstance(value, int)) \
            and APIHelper.is_valid_type(value=dictionary.get('customer_id'),
                                        type_callable=lambda value: isinstance(value, int)) \
            and APIHelper.is_valid_type(value=dictionary.get('payment_profile_id'),
                                        type_callable=lambda value: isinstance(value, int)) \
            and APIHelper.is_valid_type(value=dictionary.get('subscription_ids'),
                                        type_callable=lambda value: isinstance(value, int)) \
            and APIHelper.is_valid_type(value=dictionary.get('primary_subscription_id'),
                                        type_callable=lambda value: isinstance(value, int)) \
            and APIHelper.is_valid_type(value=dictionary.get('next_assessment_at'),
                                        type_callable=lambda value: isinstance(value, str)) \
            and APIHelper.is_valid_type(value=dictionary.get('state'),
                                        type_callable=lambda value: isinstance(value, str)) \
            and APIHelper.is_valid_type(value=dictionary.get('cancel_at_end_of_period'),
                                        type_callable=lambda value: isinstance(value, bool))

    def __repr__(self):
        return (f'{self.__class__.__name__}('
                f'uid={self.uid!r}, '
                f'scheme={self.scheme!r}, '
                f'customer_id={self.customer_id!r}, '
                f'payment_profile_id={self.payment_profile_id!r}, '
                f'subscription_ids={self.subscription_ids!r}, '
                f'primary_subscription_id={self.primary_subscription_id!r}, '
                f'next_assessment_at={self.next_assessment_at!r}, '
                f'state={self.state!r}, '
                f'cancel_at_end_of_period={self.cancel_at_end_of_period!r}, '
                f'additional_properties={self.additional_properties!r})')

    def __str__(self):
        return (f'{self.__class__.__name__}('
                f'uid={self.uid!s}, '
                f'scheme={self.scheme!s}, '
                f'customer_id={self.customer_id!s}, '
                f'payment_profile_id={self.payment_profile_id!s}, '
                f'subscription_ids={self.subscription_ids!s}, '
                f'primary_subscription_id={self.primary_subscription_id!s}, '
                f'next_assessment_at={self.next_assessment_at!s}, '
                f'state={self.state!s}, '
                f'cancel_at_end_of_period={self.cancel_at_end_of_period!s}, '
                f'additional_properties={self.additional_properties!s})')
