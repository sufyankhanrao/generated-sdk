from payrix.configuration import Environment
from payrix.exceptions.api_exception import APIException
from payrix.exceptions.error_four_hundred_exception import ErrorFourHundredException
from payrix.http.auth.api_key import ApiKeyCredentials
from payrix.http.auth.session_key import SessionKeyCredentials
from payrix.http.auth.txn_session_key import TxnSessionKeyCredentials
from payrix.models.chargeback_message_post_request import ChargebackMessagePostRequest
from payrix.models.chargeback_message_status_enum import ChargebackMessageStatusEnum
from payrix.models.chargeback_message_type_enum import ChargebackMessageTypeEnum
from payrix.models.currency_enum import CurrencyEnum
from payrix.models.frozen_enum import FrozenEnum
from payrix.models.imported_enum import ImportedEnum
from payrix.models.inactive_enum import InactiveEnum
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

chargeback_messages_controller = client.chargeback_messages
body = ChargebackMessagePostRequest(
    chargeback='t1_chb_2c2443d86f1c94d3846f85b',
    mtype=ChargebackMessageTypeEnum.RESPOND,
    status=ChargebackMessageStatusEnum.PROCESSED,
    imported=ImportedEnum.IMPORTED,
    inactive=InactiveEnum.ACTIVE,
    frozen=FrozenEnum.NOTFROZEN,
    date='20190908',
    from_queue='specifies queue',
    to_queue='specifies queue',
    contact='identifier of Contact',
    amount=1,
    currency=CurrencyEnum.USD,
    note='Charge Merchant'
)

request_token = '20250423-yourmerchant-refunds-001'

try:
    result = chargeback_messages_controller.post_chargeback_messages(
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

