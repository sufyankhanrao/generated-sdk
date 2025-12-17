from pagarmeapisdk.configuration import Environment
from pagarmeapisdk.exceptions.api_exception import APIException
from pagarmeapisdk.exceptions.error_exception import ErrorException
from pagarmeapisdk.http.auth.basic_auth import BasicAuthCredentials
from pagarmeapisdk.models.create_bank_account_request import CreateBankAccountRequest
from pagarmeapisdk.models.create_recipient_request import CreateRecipientRequest
from pagarmeapisdk.pagarmeapisdk_client import PagarmeapisdkClient

client = PagarmeapisdkClient(
    service_referer_name='ServiceRefererName',
    basic_auth_credentials=BasicAuthCredentials(
        username='BasicAuthUserName',
        password='BasicAuthPassword'
    ),
    environment=Environment.PRODUCTION
)

recipients_controller = client.recipients
request = CreateRecipientRequest(
    default_bank_account=CreateBankAccountRequest(
        holder_name='holder_name4',
        holder_type='holder_type0',
        holder_document='holder_document2',
        bank='bank6',
        branch_number='branch_number4',
        account_number='account_number8',
        account_check_digit='account_check_digit4',
        mtype='type2',
        metadata={
            'key0': 'metadata5',
            'key1': 'metadata4',
            'key2': 'metadata3'
        }
    ),
    metadata={
        'key0': 'metadata3'
    },
    code='code4',
    payment_mode='bank_transfer'
)

try:
    result = recipients_controller.create_recipient(request)

    if result.is_success():
        print(result.body)
    elif result.is_error():
        print(result.errors)

except ErrorException as e: 
    print(e)
except APIException as e: 
    print(e)

