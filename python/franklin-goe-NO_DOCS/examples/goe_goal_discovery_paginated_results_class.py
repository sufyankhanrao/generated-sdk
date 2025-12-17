import logging

from goeapi.configuration import Environment
from goeapi.exceptions.api_exception import ApiException
from goeapi.exceptions.internal_server_message_exception import InternalServerMessageException
from goeapi.exceptions.validation_message_one_exception import ValidationMessageOneException
from goeapi.goeapi_client import GoeapiClient
from goeapi.http.auth.oauth_2 import BearerAuthCredentials
from goeapi.logging.configuration.api_logging_configuration import LoggingConfiguration
from goeapi.logging.configuration.api_logging_configuration import RequestLoggingConfiguration
from goeapi.logging.configuration.api_logging_configuration import ResponseLoggingConfiguration

client = GoeapiClient(
    bearer_auth_credentials=BearerAuthCredentials(
        access_token='AccessToken'
    ),
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

goe_api = client.goe
request_id = 'requestId2'

page_index = 500

try:
    result = goe_api.goal_discovery_paginated_results(
        request_id,
        page_index=page_index
    )

    if result.is_success():
        print(result.body)
    elif result.is_error():
        print(result.errors)

except ValidationMessageOneException as e: 
    print(e)
except InternalServerMessageException as e: 
    print(e)
except ApiException as e: 
    print(e)

