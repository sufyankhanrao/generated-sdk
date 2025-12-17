from foxitesigntest.configuration import Environment
from foxitesigntest.exceptions.api_exception import APIException
from foxitesigntest.foxitesigntest_client import FoxitesigntestClient
from foxitesigntest.http.auth.o_auth_2 import BearerAuthCredentials
from foxitesigntest.models.email_group_identifiers import EmailGroupIdentifiers

client = FoxitesigntestClient(
    bearer_auth_credentials=BearerAuthCredentials(
        access_token='AccessToken'
    ),
    environment=Environment.US_SERVER
)

parties_api_controller = client.parties_api
body = EmailGroupIdentifiers(
    email_group_names=[
        'Email_Group_1',
        'Email_Group_2'
    ]
)

try:
    result = parties_api_controller.get_email_group_details(body)

    if result.is_success():
        print(result.body)
    elif result.is_error():
        print(result.errors)

except APIException as e: 
    print(e)

