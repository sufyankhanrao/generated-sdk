from payrix.configuration import Environment
from payrix.exceptions.api_exception import APIException
from payrix.exceptions.error_four_hundred_exception import ErrorFourHundredException
from payrix.http.auth.api_key import ApiKeyCredentials
from payrix.http.auth.session_key import SessionKeyCredentials
from payrix.http.auth.txn_session_key import TxnSessionKeyCredentials
from payrix.models.frozen_enum import FrozenEnum
from payrix.models.inactive_enum import InactiveEnum
from payrix.models.orgs_vas_safer_payments_default_program_enum import OrgsVASSaferPaymentsDefaultProgramEnum
from payrix.models.orgs_vas_safer_payments_put_request import OrgsVASSaferPaymentsPutRequest
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

orgs_vas_safer_payments_controller = client.orgs_vas_safer_payments
id = 't1_ovs_67ffd50aa5b2855bcd59e00'

body = OrgsVASSaferPaymentsPutRequest(
    org='t1_org_680bfd2cea2729081810000',
    default_program=OrgsVASSaferPaymentsDefaultProgramEnum.BASIC,
    inactive=InactiveEnum.ACTIVE,
    frozen=FrozenEnum.NOTFROZEN
)

try:
    result = orgs_vas_safer_payments_controller.put_orgs_vas_safer_payments_id(
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

