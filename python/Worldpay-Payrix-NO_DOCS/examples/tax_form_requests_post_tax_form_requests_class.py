from payrix.configuration import Environment
from payrix.exceptions.api_exception import APIException
from payrix.exceptions.error_four_hundred_exception import ErrorFourHundredException
from payrix.http.auth.api_key import ApiKeyCredentials
from payrix.http.auth.session_key import SessionKeyCredentials
from payrix.http.auth.txn_session_key import TxnSessionKeyCredentials
from payrix.models.tax_form_requests_post_request import TaxFormRequestsPostRequest
from payrix.models.type_enum import TypeEnum
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

tax_form_requests_controller = client.tax_form_requests
body = TaxFormRequestsPostRequest(
    merchant='t1_mer_6705400c6dbd095b4cb0000',
    mtype=TypeEnum.ENUM_1099K,
    tax_year=2024,
    response_code=500
)

request_token = '20250423-yourmerchant-refunds-001'

try:
    result = tax_form_requests_controller.post_tax_form_requests(
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

