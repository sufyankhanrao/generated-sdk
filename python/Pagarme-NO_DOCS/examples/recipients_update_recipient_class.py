from pagarmeapisdk.configuration import Environment
from pagarmeapisdk.exceptions.api_exception import APIException
from pagarmeapisdk.exceptions.error_exception import ErrorException
from pagarmeapisdk.http.auth.basic_auth import BasicAuthCredentials
from pagarmeapisdk.models.update_recipient_request import UpdateRecipientRequest
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

request = UpdateRecipientRequest(
    name='name6',
    email='email0',
    description='description6',
    mtype='type4',
    status='status8',
    metadata={
        'key0': 'metadata3'
    }
)

try:
    result = recipients_controller.update_recipient(
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

