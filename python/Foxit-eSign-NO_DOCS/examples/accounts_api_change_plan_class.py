from foxitesigntest.configuration import Environment
from foxitesigntest.exceptions.api_exception import APIException
from foxitesigntest.foxitesigntest_client import FoxitesigntestClient
from foxitesigntest.http.auth.o_auth_2 import BearerAuthCredentials
from foxitesigntest.models.plan_names_enum import PlanNamesEnum

client = FoxitesigntestClient(
    bearer_auth_credentials=BearerAuthCredentials(
        access_token='AccessToken'
    ),
    environment=Environment.US_SERVER
)

accounts_api_controller = client.accounts_api
new_number_of_licenses = '20'

new_plan = PlanNamesEnum.BUSINESS_PREMIUM

try:
    result = accounts_api_controller.change_plan(
        new_number_of_licenses,
        new_plan
    )

    if result.is_success():
        print(result.body)
    elif result.is_error():
        print(result.errors)

except APIException as e: 
    print(e)

