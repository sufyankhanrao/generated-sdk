import logging

from goeapi.configuration import Environment
from goeapi.exceptions.api_exception import ApiException
from goeapi.exceptions.internal_server_message_1_exception import InternalServerMessage1Exception
from goeapi.exceptions.refresh_token_status_exception import RefreshTokenStatusException
from goeapi.goeapi_client import GoeapiClient
from goeapi.logging.configuration.api_logging_configuration import LoggingConfiguration
from goeapi.logging.configuration.api_logging_configuration import RequestLoggingConfiguration
from goeapi.logging.configuration.api_logging_configuration import ResponseLoggingConfiguration
from goeapi.models.refresh_token_input_model import RefreshTokenInputModel

client = GoeapiClient(
    environment=Environment.UAT,
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

auth_api = client.auth
body = RefreshTokenInputModel(
    refresh_token='HEpb6yNYH68XTFING3a_RkqLHOgFosQv5-7W0_So3VE'
)

try:
    result = auth_api.refresh_token(body)

    if result.is_success():
        print(result.body)
    elif result.is_error():
        print(result.errors)

except RefreshTokenStatusException as e: 
    print(e)
except InternalServerMessage1Exception as e: 
    print(e)
except ApiException as e: 
    print(e)

