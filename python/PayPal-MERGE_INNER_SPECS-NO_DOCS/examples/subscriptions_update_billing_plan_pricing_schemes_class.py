import logging

from paypalserversdk.configuration import Environment
from paypalserversdk.exceptions.api_exception import ApiException
from paypalserversdk.exceptions.subscription_error_exception import SubscriptionErrorException
from paypalserversdk.http.auth.o_auth_2 import ClientCredentialsAuthCredentials
from paypalserversdk.logging.configuration.api_logging_configuration import LoggingConfiguration
from paypalserversdk.logging.configuration.api_logging_configuration import RequestLoggingConfiguration
from paypalserversdk.logging.configuration.api_logging_configuration import ResponseLoggingConfiguration
from paypalserversdk.models.subscription_pricing_scheme import SubscriptionPricingScheme
from paypalserversdk.models.update_pricing_scheme import UpdatePricingScheme
from paypalserversdk.models.update_pricing_schemes_request import UpdatePricingSchemesRequest
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
    'id': 'id0',
    'body': UpdatePricingSchemesRequest(
        pricing_schemes=[
            UpdatePricingScheme(
                billing_cycle_sequence=34,
                pricing_scheme=SubscriptionPricingScheme()
            )
        ]
    )
}
try:
    result = subscriptions_controller.update_billing_plan_pricing_schemes(collect)

    if result.is_success():
        print(result.body)
    elif result.is_error():
        print(result.errors)

except SubscriptionErrorException as e: 
    print(e)
except ApiException as e: 
    print(e)

