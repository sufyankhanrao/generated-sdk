from payrix.configuration import Environment
from payrix.exceptions.api_exception import APIException
from payrix.exceptions.error_four_hundred_exception import ErrorFourHundredException
from payrix.http.auth.api_key import ApiKeyCredentials
from payrix.http.auth.session_key import SessionKeyCredentials
from payrix.http.auth.txn_session_key import TxnSessionKeyCredentials
from payrix.models.frozen_enum import FrozenEnum
from payrix.models.inactive_enum import InactiveEnum
from payrix.models.pinless_debit_conversions_put_request import PinlessDebitConversionsPutRequest
from payrix.models.platform_2_enum import Platform2Enum
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

pinless_debit_conversions_controller = client.pinless_debit_conversions
id = 't1_pdc_684c7ec770b6d462c4cd000'

body = PinlessDebitConversionsPutRequest(
    enablement_date='2023-06-01 01:00:00',
    org='t1_org_684c7ae33b2d4f98520a79a',
    division='t1_div_684c7ae33b2d4f98520a00b',
    partition='t1_ptn_666834d4d504f11234578f0',
    platform=Platform2Enum.VCORE,
    inactive=InactiveEnum.ACTIVE,
    frozen=FrozenEnum.NOTFROZEN,
    deleted='2023-06-01 01:00:00',
    deleter='t1_log_67a4e72ad2ccca060a2fcfb'
)

request_token = '20250423-yourmerchant-refunds-001'

try:
    result = pinless_debit_conversions_controller.put_pinless_debit_conversions_id(
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

