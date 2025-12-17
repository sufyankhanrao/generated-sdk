import jsonpickle

from foxitesigntest.configuration import Environment
from foxitesigntest.exceptions.api_exception import APIException
from foxitesigntest.foxitesigntest_client import FoxitesigntestClient
from foxitesigntest.http.auth.o_auth_2 import BearerAuthCredentials

client = FoxitesigntestClient(
    bearer_auth_credentials=BearerAuthCredentials(
        access_token='AccessToken'
    ),
    environment=Environment.US_SERVER
)

parties_api_controller = client.parties_api
body = jsonpickle.decode('{"emailGroupName":"Email_Group_Name","emailGroupDescription":"Email_Group_Description","allowAdvancedEmailValidation":true,"parties":[{"firstName":"Sandra","lastName":"Smith","emailId":"san_smith@esigngenie.com"},{"firstName":"Hannah","lastName":"Pitt","emailId":"pitthannah@esigngenie.com"}]}')

try:
    result = parties_api_controller.create_email_group(body)

    if result.is_success():
        print(result.body)
    elif result.is_error():
        print(result.errors)

except APIException as e: 
    print(e)

