from mindbodypublicapi.configuration import Environment
from mindbodypublicapi.exceptions.api_exception import APIException
from mindbodypublicapi.mindbodypublicapi_client import MindbodypublicapiClient
from mindbodypublicapi.models.issue_request import IssueRequest

client = MindbodypublicapiClient(
    environment=Environment.PRODUCTION
)

user_token_controller = client.user_token
version = '6'

request = IssueRequest(
    username='Username4',
    password='Password6'
)

site_id = '-99'

try:
    result = user_token_controller.issue_token(
        version,
        request,
        site_id
    )

    if result.is_success():
        print(result.body)
    elif result.is_error():
        print(result.errors)

except APIException as e: 
    print(e)

