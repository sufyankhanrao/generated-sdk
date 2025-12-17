from pagarmeapisdk.configuration import Environment
from pagarmeapisdk.exceptions.api_exception import APIException
from pagarmeapisdk.exceptions.error_exception import ErrorException
from pagarmeapisdk.http.auth.basic_auth import BasicAuthCredentials
from pagarmeapisdk.models.create_bank_account_request import CreateBankAccountRequest
from pagarmeapisdk.models.update_recipient_bank_account_request import UpdateRecipientBankAccountRequest
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
recipient_id = 'recipient_id0'

request = UpdateRecipientBankAccountRequest(
    bank_account=CreateBankAccountRequest(
        holder_name='holder_name0',
        holder_type='holder_type6',
        holder_document='holder_document8',
        bank='bank2',
        branch_number='branch_number0',
        account_number='account_number4',
        account_check_digit='account_check_digit0',
        mtype='type6',
        metadata={
            'key0': 'metadata1',
            'key1': 'metadata0'
        }
    ),
    payment_mode='bank_transfer'
)

try:
    result = recipients_controller.update_recipient_default_bank_account(
        recipient_id,
        request
    )

    if result.is_success():
        print(result.body)
    elif result.is_error():
        print(result.errors)

except ErrorException as e: 
    print(e)
except APIException as e: 
    print(e)

