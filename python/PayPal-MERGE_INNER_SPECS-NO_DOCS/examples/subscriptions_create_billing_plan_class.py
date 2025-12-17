import logging

from paypalserversdk.configuration import Environment
from paypalserversdk.exceptions.api_exception import ApiException
from paypalserversdk.exceptions.subscription_error_exception import SubscriptionErrorException
from paypalserversdk.http.auth.o_auth_2 import ClientCredentialsAuthCredentials
from paypalserversdk.logging.configuration.api_logging_configuration import LoggingConfiguration
from paypalserversdk.logging.configuration.api_logging_configuration import RequestLoggingConfiguration
from paypalserversdk.logging.configuration.api_logging_configuration import ResponseLoggingConfiguration
from paypalserversdk.models.frequency import Frequency
from paypalserversdk.models.interval_unit import IntervalUnit
from paypalserversdk.models.payment_preferences import PaymentPreferences
from paypalserversdk.models.plan_request import PlanRequest
from paypalserversdk.models.plan_request_status import PlanRequestStatus
from paypalserversdk.models.setup_fee_failure_action import SetupFeeFailureAction
from paypalserversdk.models.subscription_billing_cycle import SubscriptionBillingCycle
from paypalserversdk.models.tenure_type import TenureType
from paypalserversdk.paypal_serversdk_client import PaypalServersdkClient

client = PaypalServersdkClient(
    client_credentials_auth_credentials=ClientCredentialsAuthCredentials(
        o_auth_client_id='OAuthClientId',
        o_auth_client_secret='OAuthClientSecret'
    ),
    environment=Environment.SANDBOX,
    logging_configuration=LoggingConfiguration(
        log_level=logging.INFO,
        request_logging_config=RequestLoggingConfiguration(
            log_body=True
        ),
        response_logging_config=ResponseLoggingConfiguration(
            log_headers=True
        )
    )
)

subscriptions_controller = client.subscriptions
collect = {
    'prefer': 'return=minimal',
    'body': PlanRequest(
        product_id='product_id2',
        name='name6',
        billing_cycles=[
            SubscriptionBillingCycle(
                frequency=Frequency(
                    interval_unit=IntervalUnit.DAY,
                    interval_count=1
                ),
                tenure_type=TenureType.REGULAR,
                sequence=8,
                total_cycles=1
            )
        ],
        payment_preferences=PaymentPreferences(
            auto_bill_outstanding=True,
            setup_fee_failure_action=SetupFeeFailureAction.CANCEL,
            payment_failure_threshold=0
        ),
        status=PlanRequestStatus.ACTIVE,
        quantity_supported=False
    )
}
try:
    result = subscriptions_controller.create_billing_plan(collect)

    if result.is_success():
        print(result.body)
    elif result.is_error():
        print(result.errors)

except SubscriptionErrorException as e: 
    print(e)
except ApiException as e: 
    print(e)

