from foxitesigntest.configuration import Environment
from foxitesigntest.exceptions.api_exception import APIException
from foxitesigntest.foxitesigntest_client import FoxitesigntestClient
from foxitesigntest.models.account_creation_company_object import AccountCreationCompanyObject
from foxitesigntest.models.account_creation_object import AccountCreationObject
from foxitesigntest.models.account_creation_user_object import AccountCreationUserObject
from foxitesigntest.models.plan_names_enum import PlanNamesEnum

client = FoxitesigntestClient(
    environment=Environment.US_SERVER
)

accounts_api_controller = client.accounts_api
account_creationobject = AccountCreationObject(
    client_id='123456789012345678901234567890',
    client_secret='123456789012345678901234567890',
    company=AccountCreationCompanyObject(
        company_name='Wayne Tech',
        company_address='LA, US'
    ),
    user=AccountCreationUserObject(
        first_name='Bruce',
        last_name='Wayne',
        email_id='esigndemo@foxitsoftware.com',
        login_password='Welcome@123!'
    ),
    plan_name=PlanNamesEnum.PROFESSIONAL,
    account_type='partner-pay',
    partner_code='WAYNE_TECH'
)

try:
    result = accounts_api_controller.create_new_account(account_creationobject)

    if result.is_success():
        print(result.body)
    elif result.is_error():
        print(result.errors)

except APIException as e: 
    print(e)

