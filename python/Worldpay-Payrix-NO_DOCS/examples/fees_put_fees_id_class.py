from payrix.configuration import Environment
from payrix.exceptions.api_exception import APIException
from payrix.exceptions.error_four_hundred_exception import ErrorFourHundredException
from payrix.http.auth.api_key import ApiKeyCredentials
from payrix.http.auth.session_key import SessionKeyCredentials
from payrix.http.auth.txn_session_key import TxnSessionKeyCredentials
from payrix.models.currency_enum import CurrencyEnum
from payrix.models.fee_collection_enum import FeeCollectionEnum
from payrix.models.fee_schedule_enum import FeeScheduleEnum
from payrix.models.fee_type_enum import FeeTypeEnum
from payrix.models.fee_um_enum import FeeUmEnum
from payrix.models.fees_put_request import FeesPutRequest
from payrix.models.frozen_enum import FrozenEnum
from payrix.models.inactive_enum import InactiveEnum
from payrix.models.txn_fee_enum import TxnFeeEnum
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

fees_controller = client.fees
id = 't1_fee_67b5422dda39a7c36059988'

body = FeesPutRequest(
    entity='t1_ent_00758e990d7437d51cdf1aa',
    forentity='t1_ent_0088c831a31ca8841c81111',
    org='t1_org_00b2ac11ed8bed97fb81111',
    mtype=FeeTypeEnum.FEE,
    name='Boarding Fee',
    description='Boarding Fee',
    schedule=FeeScheduleEnum.ENUM_5,
    schedule_factor=1,
    start=20160120,
    finish=21160120,
    collection=FeeCollectionEnum.TXNTAXID,
    collection_factor=2,
    collection_offset=5,
    collection_include_current=0,
    um=FeeUmEnum.ACTUAL,
    amount=5,
    maximum=30,
    currency=CurrencyEnum.USD,
    txn_fee=TxnFeeEnum.DISABLED,
    inactive=InactiveEnum.ACTIVE,
    frozen=FrozenEnum.NOTFROZEN
)

request_token = '20250423-yourmerchant-refunds-001'

try:
    result = fees_controller.put_fees_id(
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

