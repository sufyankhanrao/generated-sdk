from payrix.configuration import Environment
from payrix.exceptions.api_exception import APIException
from payrix.exceptions.error_four_hundred_exception import ErrorFourHundredException
from payrix.http.auth.api_key import ApiKeyCredentials
from payrix.http.auth.session_key import SessionKeyCredentials
from payrix.http.auth.txn_session_key import TxnSessionKeyCredentials
from payrix.models.frozen_enum import FrozenEnum
from payrix.models.inactive_enum import InactiveEnum
from payrix.models.orgs_vas_efe_products_post_request import OrgsVASEfeProductsPostRequest
from payrix.models.platform_enum import PlatformEnum
from payrix.models.product_3_enum import Product3Enum
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

orgs_vas_efe_products_controller = client.orgs_vas_efe_products
body = OrgsVASEfeProductsPostRequest(
    org='t1_org_6862c1211b366bbfe87657c',
    product=Product3Enum.MERCHANTWORKINGCAPITAL,
    contract_type='{"residualFeeType": "rev_share"}',
    platform=PlatformEnum.PARAFIN,
    inactive=InactiveEnum.ACTIVE,
    frozen=FrozenEnum.NOTFROZEN
)

request_token = '20250423-yourmerchant-refunds-001'

try:
    result = orgs_vas_efe_products_controller.post_orgs_vas_efe_products(
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

