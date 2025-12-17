from greenbyteapi.configuration import Environment
from greenbyteapi.exceptions.api_exception import APIException
from greenbyteapi.exceptions.problem_details_exception import ProblemDetailsException
from greenbyteapi.greenbyteapi_client import GreenbyteapiClient
from greenbyteapi.http.auth.custom_header_authentication import CustomHeaderAuthenticationCredentials

client = GreenbyteapiClient(
    custom_header_authentication_credentials=CustomHeaderAuthenticationCredentials(
        x_api_key='X-Api-Key'
    ),
    environment=Environment.PRODUCTION,
    customer='intro'
)

plan_controller = client.plan
try:
    result = plan_controller.list_organizations()

    if result.is_success():
        print(result.body)
    elif result.is_error():
        print(result.errors)

except ProblemDetailsException as e: 
    print(e)
except APIException as e: 
    print(e)

