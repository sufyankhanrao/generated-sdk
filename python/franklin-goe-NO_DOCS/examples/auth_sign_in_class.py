import logging

from goeapi.configuration import Environment
from goeapi.exceptions.api_exception import ApiException
from goeapi.exceptions.internal_server_message_1_exception import InternalServerMessage1Exception
from goeapi.exceptions.validation_message_two_exception import ValidationMessageTwoException
from goeapi.goeapi_client import GoeapiClient
from goeapi.logging.configuration.api_logging_configuration import LoggingConfiguration
from goeapi.logging.configuration.api_logging_configuration import RequestLoggingConfiguration
from goeapi.logging.configuration.api_logging_configuration import ResponseLoggingConfiguration
from goeapi.models.sign_in_input_model import SignInInputModel

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
body = SignInInputModel(
    email='abc@abc.com',
    password='Gpattm@#124'
)

try:
    result = auth_api.sign_in(body)

    if result.is_success():
        print(result.body)
    elif result.is_error():
        print(result.errors)

except ValidationMessageTwoException as e: 
    print(e)
except InternalServerMessage1Exception as e: 
    print(e)
except ApiException as e: 
    print(e)

