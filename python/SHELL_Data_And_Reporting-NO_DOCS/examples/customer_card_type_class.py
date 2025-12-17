from shelldatareportingapis.configuration import Environment
from shelldatareportingapis.exceptions.api_exception import APIException
from shelldatareportingapis.exceptions.default_error_exception import DefaultErrorException
from shelldatareportingapis.exceptions.error_user_access_error_1_exception import ErrorUserAccessError1Exception
from shelldatareportingapis.http.auth.basic_auth import BasicAuthCredentials
from shelldatareportingapis.models.card_type_request import CardTypeRequest
from shelldatareportingapis.shell_data_reporting_ap_is_client import ShellDataReportingApIsClient

client = ShellDataReportingApIsClient(
    basic_auth_credentials=BasicAuthCredentials(
        username='Username',
        password='Password'
    ),
    environment=Environment.SIT
)

customer_controller = client.customer
apikey = 'apikey6'

request_id = '2b0cbe11-f109-4c43-9201-49af0370df1c'

body = CardTypeRequest(
    col_co_id=14,
    col_co_code=14,
    payer_id=2343,
    payer_number='GB000000124',
    account_id=343,
    account_number='GB000000124',
    include_usage_restrictions=True,
    include_purchase_categories=True
)

try:
    result = customer_controller.card_type(
        apikey,
        request_id,
        body=body
    )

    if result.is_success():
        print(result.body)
    elif result.is_error():
        print(result.errors)

except DefaultErrorException as e: 
    print(e)
except ErrorUserAccessError1Exception as e: 
    print(e)
except APIException as e: 
    print(e)

