from payrix.configuration import Environment
from payrix.exceptions.api_exception import APIException
from payrix.exceptions.error_four_hundred_exception import ErrorFourHundredException
from payrix.http.auth.api_key import ApiKeyCredentials
from payrix.http.auth.session_key import SessionKeyCredentials
from payrix.http.auth.txn_session_key import TxnSessionKeyCredentials
from payrix.models.embedded_finance_post_request import EmbeddedFinancePostRequest
from payrix.models.frozen_enum import FrozenEnum
from payrix.models.inactive_enum import InactiveEnum
from payrix.models.platform_enum import PlatformEnum
from payrix.models.product_enum import ProductEnum
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

embedded_finance_controller = client.embedded_finance
body = EmbeddedFinancePostRequest(
    enablement_date='2023-06-01 01:00:00',
    product=ProductEnum.MERCHANTWORKINGCAPITAL,
    platform=PlatformEnum.PARAFIN,
    entity='t1_ent_685d27bc1611a5c48c0000f',
    org='t1_org_685d27bd878c0a8cf00ad0c',
    division='t1_div_67b51635da21f7399ce2af1',
    partition='t1_ptn_666834d4d504f11234578f0',
    inactive=InactiveEnum.ACTIVE,
    frozen=FrozenEnum.NOTFROZEN
)

request_token = '20250423-yourmerchant-refunds-001'

try:
    result = embedded_finance_controller.post_embedded_finance(
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

