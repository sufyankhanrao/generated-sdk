from fortisapi.configuration import Environment
from fortisapi.exceptions.api_exception import APIException
from fortisapi.exceptions.response_401_token_exception import Response401tokenException
from fortisapi.exceptions.response_412_exception import Response412Exception
from fortisapi.fortisapi_client import FortisapiClient
from fortisapi.http.auth.developer_id import DeveloperIdCredentials
from fortisapi.http.auth.user_api_key import UserApiKeyCredentials
from fortisapi.http.auth.user_id import UserIdCredentials
from fortisapi.models.v_1_declined_recurring_transaction_payments_request import V1DeclinedRecurringTransactionPaymentsRequest

client = FortisapiClient(
    user_id_credentials=UserIdCredentials(
        user_id='user-id'
    ),
    user_api_key_credentials=UserApiKeyCredentials(
        user_api_key='user-api-key'
    ),
    developer_id_credentials=DeveloperIdCredentials(
        developer_id='developer-id'
    ),
    environment=Environment.SANDBOX
)

declined_recurring_transactions_controller = client.declined_recurring_transactions
body = V1DeclinedRecurringTransactionPaymentsRequest(
    declined_recurring_transaction_id='11e95f8ec39de8fbdb0a4f1a',
    account_number='5454545454545454',
    exp_date='0722',
    transaction_amount=0,
    account_holder_name='John Doe',
    description='Description',
    save_account_title='John Account',
    subtotal_amount=599,
    surcharge_amount=599
)

try:
    result = declined_recurring_transactions_controller.create_a_payment(body)

    if result.is_success():
        print(result.body)
    elif result.is_error():
        print(result.errors)

except Response401tokenException as e: 
    print(e)
except Response412Exception as e: 
    print(e)
except APIException as e: 
    print(e)

