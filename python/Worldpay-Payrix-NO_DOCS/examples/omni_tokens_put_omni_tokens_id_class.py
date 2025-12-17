from payrix.configuration import Environment
from payrix.exceptions.api_exception import APIException
from payrix.exceptions.error_four_hundred_exception import ErrorFourHundredException
from payrix.http.auth.api_key import ApiKeyCredentials
from payrix.http.auth.session_key import SessionKeyCredentials
from payrix.http.auth.txn_session_key import TxnSessionKeyCredentials
from payrix.models.frozen_enum import FrozenEnum
from payrix.models.inactive_enum import InactiveEnum
from payrix.models.omni_tokens_put_request import OmniTokensPutRequest
from payrix.models.platform_1_enum import Platform1Enum
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

omni_tokens_controller = client.omni_tokens
id = 't1_otk_6809db98230a5b02b08f00z'

body = OmniTokensPutRequest(
    enablement_date='2025-04-24 02:35:04',
    org='t1_org_5b0e08025ec790d3f9b8c00',
    division='t1_div_67c56806728fbbf0bae0b00',
    partition='t1_ptn_666834d4d504f21414978z0',
    entity='t1_ent_6809db6dd78923dadbfd904',
    platform=Platform1Enum.VCORE,
    inactive=InactiveEnum.ACTIVE,
    frozen=FrozenEnum.NOTFROZEN,
    deleted='2025-04-24 02:35:04',
    deleter=''
)

try:
    result = omni_tokens_controller.put_omni_tokens_id(
        id,
        body
    )

    if result.is_success():
        print(result.body)
    elif result.is_error():
        print(result.errors)

except ErrorFourHundredException as e: 
    print(e)
except APIException as e: 
    print(e)

