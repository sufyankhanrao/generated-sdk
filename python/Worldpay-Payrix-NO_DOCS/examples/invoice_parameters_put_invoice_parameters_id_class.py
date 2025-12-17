from payrix.configuration import Environment
from payrix.exceptions.api_exception import APIException
from payrix.exceptions.error_four_hundred_exception import ErrorFourHundredException
from payrix.http.auth.api_key import ApiKeyCredentials
from payrix.http.auth.session_key import SessionKeyCredentials
from payrix.http.auth.txn_session_key import TxnSessionKeyCredentials
from payrix.models.frozen_enum import FrozenEnum
from payrix.models.inactive_enum import InactiveEnum
from payrix.models.invoice_parameter_locked_enum import InvoiceParameterLockedEnum
from payrix.models.invoice_parameter_type_enum import InvoiceParameterTypeEnum
from payrix.models.invoice_parameters_put_request import InvoiceParametersPutRequest
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

invoice_parameters_controller = client.invoice_parameters
id = 't1_inp_67e46c1f4245ca0a6398000'

body = InvoiceParametersPutRequest(
    login='t1_log_67c272f9078d060d291fdez',
    entity='t1_ent_67c272f920c1724d2709c0b',
    division='t1_div_67c56806728fbbf0bae0b00',
    org='t1_org_67b736ad7d05922340000cf',
    partition='t1_ptn_666834d4d504f11234578f0',
    locked=InvoiceParameterLockedEnum.NOTLOCKED,
    mtype=InvoiceParameterTypeEnum.APIKEY,
    value='ecfb12e30dcfc1421a2e6c18345cb0a6',
    inactive=InactiveEnum.ACTIVE,
    frozen=FrozenEnum.NOTFROZEN
)

request_token = '20250423-yourmerchant-refunds-001'

try:
    result = invoice_parameters_controller.put_invoice_parameters_id(
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

