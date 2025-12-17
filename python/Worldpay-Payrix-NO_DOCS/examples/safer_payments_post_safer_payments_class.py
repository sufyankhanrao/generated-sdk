from payrix.configuration import Environment
from payrix.exceptions.api_exception import APIException
from payrix.exceptions.error_four_hundred_exception import ErrorFourHundredException
from payrix.http.auth.api_key import ApiKeyCredentials
from payrix.http.auth.session_key import SessionKeyCredentials
from payrix.http.auth.txn_session_key import TxnSessionKeyCredentials
from payrix.models.frozen_enum import FrozenEnum
from payrix.models.inactive_enum import InactiveEnum
from payrix.models.safer_payment_pci_non_validation_fee_enabled_enum import SaferPaymentPciNonValidationFeeEnabledEnum
from payrix.models.safer_payment_program_enum import SaferPaymentProgramEnum
from payrix.models.safer_payment_status_enum import SaferPaymentStatusEnum
from payrix.models.safer_payments_post_request import SaferPaymentsPostRequest
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

safer_payments_controller = client.safer_payments
body = SaferPaymentsPostRequest(
    entity='t1_ent_65de12aabb1f58e2a3441f7',
    status=SaferPaymentStatusEnum.COMPLIANCE,
    enablement_date='2024-02-27 11:54:19',
    pci_non_validation_fee_enabled=SaferPaymentPciNonValidationFeeEnabledEnum.ENUM_0,
    org='t1_org_00b2ac11ed8bed97fb80000',
    division='t1_div_67c56806728fbbf0bae0b00',
    partition='t1_ptn_666834d4d504f21414978z5',
    program=SaferPaymentProgramEnum.BASIC,
    deleted='2024-02-27 11:54:19',
    deleter='',
    inactive=InactiveEnum.ACTIVE,
    frozen=FrozenEnum.NOTFROZEN
)

try:
    result = safer_payments_controller.post_safer_payments(body)

    if result.is_success():
        print(result.body)
    elif result.is_error():
        print(result.errors)

except ErrorFourHundredException as e: 
    print(e)
except APIException as e: 
    print(e)

