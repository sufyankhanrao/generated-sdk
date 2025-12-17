from payrix.configuration import Environment
from payrix.exceptions.api_exception import APIException
from payrix.exceptions.error_four_hundred_exception import ErrorFourHundredException
from payrix.http.auth.api_key import ApiKeyCredentials
from payrix.http.auth.session_key import SessionKeyCredentials
from payrix.http.auth.txn_session_key import TxnSessionKeyCredentials
from payrix.models.mappings_put_request import MappingsPutRequest
from payrix.payrix_client import PayrixClient

client = PayrixClient(
    api_key_credentials=ApiKeyCredentials(
        apikey='APIKEY'
    ),
    session_key_credentials=SessionKeyCredentials(
        sessionkey='SESSIONKEY'
    ),
    txn_session_key_credentials=TxnSessionKeyCredentials(
        txnsessionkey='TXNSESSIONKEY'
    ),
    environment=Environment.QA
)

mappings_controller = client.mappings
id = 't1_map_63d6a1df609e000f10b00d0'

body = MappingsPutRequest(
    login='t1_log_63d25f51ea7ddb271d78304',
    name='Test1',
    description='Test1',
    input='{\\"mappingsCreate\\":{\\"requests\\":[{\\"name\\":{\\"__path__\\":\\"mappings2Create;mappings2Request;name\\"}}]}}',
    output='{\\"mappings2CreateResponse\\":{\\"mappings2Responses\\":[{\\"name\\":{\\"__path__\\":\\"mappingsCreateResponse;requests;[];name\\"}}]}}',
    namespace='XML namespace of input and output'
)

request_token = '20250423-yourmerchant-refunds-001'

try:
    result = mappings_controller.put_mappings_id(
        id,
        body,
        request_token=request_token
    )

    if result.is_success():
        print(result.body)
    elif result.is_error():
        print(result.errors)

except ErrorFourHundredException as e: 
    print(e)
except APIException as e: 
    print(e)

