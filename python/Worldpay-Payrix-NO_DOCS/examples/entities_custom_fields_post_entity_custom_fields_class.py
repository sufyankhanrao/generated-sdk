from payrix.configuration import Environment
from payrix.exceptions.api_exception import APIException
from payrix.exceptions.error_four_hundred_exception import ErrorFourHundredException
from payrix.http.auth.api_key import ApiKeyCredentials
from payrix.http.auth.session_key import SessionKeyCredentials
from payrix.http.auth.txn_session_key import TxnSessionKeyCredentials
from payrix.models.entity_custom_fields_post_request import EntityCustomFieldsPostRequest
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

entities_custom_fields_controller = client.entities_custom_fields
body = EntityCustomFieldsPostRequest(
    entity='t1_ent_67d3ab7bc0ef1d4284d4578',
    key='companyId',
    value='70bbd35e-8500-f011-90cb-6045bdc7c168'
)

request_token = '20250423-yourmerchant-refunds-001'

try:
    result = entities_custom_fields_controller.post_entity_custom_fields(
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

