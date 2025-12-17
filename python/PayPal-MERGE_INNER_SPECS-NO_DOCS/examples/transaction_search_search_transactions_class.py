import logging

from paypalserversdk.configuration import Environment
from paypalserversdk.exceptions.api_exception import ApiException
from paypalserversdk.exceptions.search_error_exception import SearchErrorException
from paypalserversdk.http.auth.o_auth_2 import ClientCredentialsAuthCredentials
from paypalserversdk.logging.configuration.api_logging_configuration import LoggingConfiguration
from paypalserversdk.logging.configuration.api_logging_configuration import RequestLoggingConfiguration
from paypalserversdk.logging.configuration.api_logging_configuration import ResponseLoggingConfiguration
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

transaction_search_controller = client.transaction_search
collect = {
    'start_date': 'start_date6',
    'end_date': 'end_date0',
    'fields': 'transaction_info',
    'balance_affecting_records_only': 'Y',
    'page_size': 100,
    'page': 1
}
try:
    result = transaction_search_controller.search_transactions(collect)

    if result.is_success():
        print(result.body)
    elif result.is_error():
        print(result.errors)

except SearchErrorException as e: 
    print(e)
except ApiException as e: 
    print(e)

