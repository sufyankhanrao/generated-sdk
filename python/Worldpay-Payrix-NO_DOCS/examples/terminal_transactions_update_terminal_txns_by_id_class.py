from payrix.configuration import Environment
from payrix.exceptions.api_exception import APIException
from payrix.exceptions.error_four_hundred_exception import ErrorFourHundredException
from payrix.http.auth.api_key import ApiKeyCredentials
from payrix.http.auth.session_key import SessionKeyCredentials
from payrix.http.auth.txn_session_key import TxnSessionKeyCredentials
from payrix.models.bin_type_enum import BinTypeEnum
from payrix.models.emv_enum import EmvEnum
from payrix.models.entry_mode_enum import EntryModeEnum
from payrix.models.frozen_enum import FrozenEnum
from payrix.models.hsa_fsa_card_indicator_enum import HsaFsaCardIndicatorEnum
from payrix.models.inactive_enum import InactiveEnum
from payrix.models.reserved_1_enum import Reserved1Enum
from payrix.models.signature_enum import SignatureEnum
from payrix.models.swiped_enum import SwipedEnum
from payrix.models.terminal_txn_payment_method_enum import TerminalTxnPaymentMethodEnum
from payrix.models.terminal_txn_status_enum import TerminalTxnStatusEnum
from payrix.models.terminal_txns_payment import TerminalTxnsPayment
from payrix.models.terminal_txns_put_request import TerminalTxnsPutRequest
from payrix.models.unattended_enum import UnattendedEnum
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

terminal_transactions_controller = client.terminal_transactions
id = 't1_ttx_67c76e07ebc6fbbbd476ee0'

body = TerminalTxnsPutRequest(
    bin_type=BinTypeEnum.DEBIT,
    expiration='1123',
    payment=TerminalTxnsPayment(
        method=TerminalTxnPaymentMethodEnum.AMEX,
        number='2222',
        routing='1',
        expiration='0623',
        cvv=123,
        track='Track 1'
    ),
    trace_number=853202,
    txn='related txn',
    token='124f2d0efab0bcda46f2118d688bbf97',
    payment_number=7,
    payment_method=TerminalTxnPaymentMethodEnum.VISA,
    tip=0,
    originating_app='originatingApp',
    oemt_txn_ref_number='TxnRefNumber',
    pos_application_id='15668',
    unattended=UnattendedEnum.ATTENDEDTERMINAL,
    pos_application_name='XML Test Example',
    pos_application_version='1.00',
    customer_reference_number='123456',
    gateway_transaction_id='486689252',
    customer_ticket_number='123456',
    client_ip='Client IP address',
    description='Transaction1',
    swiped=SwipedEnum.SWIPED,
    emv=EmvEnum.DIPPED,
    entry_mode=EntryModeEnum.KEYED,
    first='John',
    last='Doe',
    middle='M',
    order='orderId',
    reserved=Reserved1Enum.ENUM_NONE,
    signature=SignatureEnum.CAPTURED,
    total=8000,
    status=TerminalTxnStatusEnum.CAPTURED,
    card_network_transaction_id='250630144026744',
    omnitoken='4445223322990007',
    convenience_fee=0,
    surcharge=0,
    soft_pos_device_type_indicator='device type indicator',
    soft_pos_id='software POS ID',
    hsa_fsa_card_indicator=HsaFsaCardIndicatorEnum.NOTHSAFSA,
    gateway_terminal_id='12',
    descriptor='billing Descriptor',
    card_network_bank_net_reference_number='cardNetworkBankNetReferenceNumber',
    card_network_bank_net_settlement_date='1123',
    inactive=InactiveEnum.ACTIVE,
    frozen=FrozenEnum.NOTFROZEN
)

request_token = '20250423-yourmerchant-refunds-001'

try:
    result = terminal_transactions_controller.update_terminal_txns_by_id(
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

