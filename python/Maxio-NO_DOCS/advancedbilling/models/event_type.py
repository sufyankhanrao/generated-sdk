# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""


class EventType(object):

    """Implementation of the 'Event Type' enum.

    Attributes:
        ACCOUNT_TRANSACTION_CHANGED: The enum member of type str.
        BILLING_DATE_CHANGE: The enum member of type str.
        COMPONENT_ALLOCATION_CHANGE: The enum member of type str.
        CUSTOMER_UPDATE: The enum member of type str.
        CUSTOMER_CREATE: The enum member of type str.
        DUNNING_STEP_REACHED: The enum member of type str.
        EXPIRATION_DATE_CHANGE: The enum member of type str.
        EXPIRING_CARD: The enum member of type str.
        METERED_USAGE: The enum member of type str.
        PAYMENT_SUCCESS: The enum member of type str.
        PAYMENT_SUCCESS_RECREATED: The enum member of type str.
        PAYMENT_FAILURE: The enum member of type str.
        PAYMENT_FAILURE_RECREATED: The enum member of type str.
        REFUND_FAILURE: The enum member of type str.
        REFUND_SUCCESS: The enum member of type str.
        RENEWAL_SUCCESS: The enum member of type str.
        RENEWAL_SUCCESS_RECREATED: The enum member of type str.
        RENEWAL_FAILURE: The enum member of type str.
        SIGNUP_SUCCESS: The enum member of type str.
        SIGNUP_FAILURE: The enum member of type str.
        STATEMENT_CLOSED: The enum member of type str.
        STATEMENT_SETTLED: The enum member of type str.
        SUBSCRIPTION_BANK_ACCOUNT_UPDATE: The enum member of type str.
        SUBSCRIPTION_DELETION: The enum member of type str.
        SUBSCRIPTION_PAYPAL_ACCOUNT_UPDATE: The enum member of type str.
        SUBSCRIPTION_PRODUCT_CHANGE: The enum member of type str.
        SUBSCRIPTION_STATE_CHANGE: The enum member of type str.
        TRIAL_END_NOTICE: The enum member of type str.
        UPGRADE_DOWNGRADE_SUCCESS: The enum member of type str.
        UPGRADE_DOWNGRADE_FAILURE: The enum member of type str.
        UPCOMING_RENEWAL_NOTICE: The enum member of type str.
        CUSTOM_FIELD_VALUE_CHANGE: The enum member of type str.
        SUBSCRIPTION_PREPAYMENT_ACCOUNT_BALANCE_CHANGED: The enum member of
            type str.
        SUBSCRIPTION_SERVICE_CREDIT_ACCOUNT_BALANCE_CHANGED: The enum member
            of type str.
        additional_properties (Dict[str, object]): The additional properties
            for the model.

    """
    ACCOUNT_TRANSACTION_CHANGED = 'account_transaction_changed'

    BILLING_DATE_CHANGE = 'billing_date_change'

    COMPONENT_ALLOCATION_CHANGE = 'component_allocation_change'

    CUSTOMER_UPDATE = 'customer_update'

    CUSTOMER_CREATE = 'customer_create'

    DUNNING_STEP_REACHED = 'dunning_step_reached'

    EXPIRATION_DATE_CHANGE = 'expiration_date_change'

    EXPIRING_CARD = 'expiring_card'

    METERED_USAGE = 'metered_usage'

    PAYMENT_SUCCESS = 'payment_success'

    PAYMENT_SUCCESS_RECREATED = 'payment_success_recreated'

    PAYMENT_FAILURE = 'payment_failure'

    PAYMENT_FAILURE_RECREATED = 'payment_failure_recreated'

    REFUND_FAILURE = 'refund_failure'

    REFUND_SUCCESS = 'refund_success'

    RENEWAL_SUCCESS = 'renewal_success'

    RENEWAL_SUCCESS_RECREATED = 'renewal_success_recreated'

    RENEWAL_FAILURE = 'renewal_failure'

    SIGNUP_SUCCESS = 'signup_success'

    SIGNUP_FAILURE = 'signup_failure'

    STATEMENT_CLOSED = 'statement_closed'

    STATEMENT_SETTLED = 'statement_settled'

    SUBSCRIPTION_BANK_ACCOUNT_UPDATE = 'subscription_bank_account_update'

    SUBSCRIPTION_DELETION = 'subscription_deletion'

    SUBSCRIPTION_PAYPAL_ACCOUNT_UPDATE = 'subscription_paypal_account_update'

    SUBSCRIPTION_PRODUCT_CHANGE = 'subscription_product_change'

    SUBSCRIPTION_STATE_CHANGE = 'subscription_state_change'

    TRIAL_END_NOTICE = 'trial_end_notice'

    UPGRADE_DOWNGRADE_SUCCESS = 'upgrade_downgrade_success'

    UPGRADE_DOWNGRADE_FAILURE = 'upgrade_downgrade_failure'

    UPCOMING_RENEWAL_NOTICE = 'upcoming_renewal_notice'

    CUSTOM_FIELD_VALUE_CHANGE = 'custom_field_value_change'

    SUBSCRIPTION_PREPAYMENT_ACCOUNT_BALANCE_CHANGED = 'subscription_prepayment_account_balance_changed'

    SUBSCRIPTION_SERVICE_CREDIT_ACCOUNT_BALANCE_CHANGED = 'subscription_service_credit_account_balance_changed'

    @classmethod
    def from_value(cls, value, default=None):
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
