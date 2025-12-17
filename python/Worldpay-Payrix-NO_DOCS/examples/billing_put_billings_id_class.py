from payrix.configuration import Environment
from payrix.exceptions.api_exception import APIException
from payrix.exceptions.error_four_hundred_exception import ErrorFourHundredException
from payrix.http.auth.api_key import ApiKeyCredentials
from payrix.http.auth.session_key import SessionKeyCredentials
from payrix.http.auth.txn_session_key import TxnSessionKeyCredentials
from payrix.models.billing_collection_enum import BillingCollectionEnum
from payrix.models.billing_schedule_enum import BillingScheduleEnum
from payrix.models.billings_put_request import BillingsPutRequest
from payrix.models.collection_factor_enum import CollectionFactorEnum
from payrix.models.collection_include_current_enum import CollectionIncludeCurrentEnum
from payrix.models.currency_enum import CurrencyEnum
from payrix.models.frozen_enum import FrozenEnum
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

billing_controller = client.billing
id = 't1_bil_67dbdc94ee1b1a43e6ab400'

body = BillingsPutRequest(
    login='t1_log_5cd987a73478a6179b95008',
    entity='identifier',
    forentity='t1_ent_67dbdc7bb6b1dd5dbf396e0',
    org='t1_org_5b0e08025ec790d3f9b8c00',
    division='t1_div_67c56806728fbbf0bae0b00',
    partition='t1_ptn_666834d4d504f21414970z0',
    description='Monthly Billing',
    schedule=BillingScheduleEnum.MONTHS,
    schedule_factor=1,
    start=20250401,
    finish=20250401,
    collection=BillingCollectionEnum.ENTITY,
    collection_factor=CollectionFactorEnum.MONTHS,
    collection_offset=1,
    collection_include_current=CollectionIncludeCurrentEnum.EXCLUDECURRENTPERIOD,
    currency=CurrencyEnum.USD,
    inactive=InactiveEnum.ACTIVE,
    frozen=FrozenEnum.NOTFROZEN
)

request_token = '20250423-yourmerchant-refunds-001'

try:
    result = billing_controller.put_billings_id(
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

