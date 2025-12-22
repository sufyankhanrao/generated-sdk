from multiauthjwtandcustomheader.configuration import Environment
from multiauthjwtandcustomheader.exceptions.api_exception import APIException
from multiauthjwtandcustomheader.http.auth.http_bearer import HttpBearerCredentials
from multiauthjwtandcustomheader.http.auth.http_header import HttpHeaderCredentials
from multiauthjwtandcustomheader.models.suite_code_enum import SuiteCodeEnum
from multiauthjwtandcustomheader.multiauthjwtandcustomheader_client import MultiauthjwtandcustomheaderClient

client = MultiauthjwtandcustomheaderClient(
    http_bearer_credentials=HttpBearerCredentials(
        access_token='AccessToken'
    ),
    http_header_credentials=HttpHeaderCredentials(
        token='token',
        api_key='api-key'
    ),
    environment=Environment.TESTING,
    port='80',
    suites=SuiteCodeEnum.HEARTS
)

client_controller = client.client
try:
    result = client_controller.get_o_auth_2_test()
    print(result)
except APIException as e: 
    print(e)

