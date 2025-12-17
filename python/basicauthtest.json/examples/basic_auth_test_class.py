import logging

from batester.batester_client import BatesterClient
from batester.configuration import Environment
from batester.exceptions.api_exception import APIException
from batester.http.auth.basic_auth import BasicAuthCredentials
from batester.logging.configuration.api_logging_configuration import LoggingConfiguration
from batester.logging.configuration.api_logging_configuration import RequestLoggingConfiguration
from batester.logging.configuration.api_logging_configuration import ResponseLoggingConfiguration
from batester.models.suite_code_enum import SuiteCodeEnum

client = BatesterClient(
    basic_auth_credentials=BasicAuthCredentials(
        username='BasicAuthUserName',
        password='BasicAuthPassword'
    ),
    environment=Environment.TESTING,
    port='80',
    suites=SuiteCodeEnum.HEARTS,
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

client_controller = client.client
try:
    result = client_controller.get_basic_auth_test()

    if result.is_success():
        print(result.body)
    elif result.is_error():
        print(result.errors)

except APIException as e: 
    print(e)

