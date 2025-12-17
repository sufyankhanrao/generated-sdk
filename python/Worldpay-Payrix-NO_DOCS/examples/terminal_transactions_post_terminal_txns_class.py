from payrix.configuration import Environment
from payrix.exceptions.api_exception import APIException
from payrix.exceptions.error_four_hundred_exception import ErrorFourHundredException
from payrix.http.auth.api_key import ApiKeyCredentials
from payrix.http.auth.session_key import SessionKeyCredentials
from payrix.http.auth.txn_session_key import TxnSessionKeyCredentials
from payrix.models.bin_type_enum import BinTypeEnum
from payrix.models.country_enum import CountryEnum
from payrix.models.currency_enum import CurrencyEnum
from payrix.models.cvv_status_enum import CvvStatusEnum
from payrix.models.entry_mode_enum import EntryModeEnum
from payrix.models.frozen_enum import FrozenEnum
from payrix.models.funding_currency_enum import FundingCurrencyEnum
from payrix.models.inactive_enum import InactiveEnum
from payrix.models.pin_enum import PinEnum
from payrix.models.platform_1_enum import Platform1Enum
from payrix.models.pos_enum import PosEnum
from payrix.models.receipt_enum import ReceiptEnum
from payrix.models.signature_enum import SignatureEnum
from payrix.models.swiped_enum import SwipedEnum
from payrix.models.terminal_capability_enum import TerminalCapabilityEnum
from payrix.models.terminal_txn_origin_enum import TerminalTxnOriginEnum
from payrix.models.terminal_txn_payment_method_enum import TerminalTxnPaymentMethodEnum
from payrix.models.terminal_txn_status_enum import TerminalTxnStatusEnum
from payrix.models.terminal_txn_type_enum import TerminalTxnTypeEnum
from payrix.models.terminal_txns_payment import TerminalTxnsPayment
from payrix.models.terminal_txns_post_request import TerminalTxnsPostRequest
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
body = TerminalTxnsPostRequest(
    bin_type=BinTypeEnum.DEBIT,
    origin=TerminalTxnOriginEnum.TERMINAL,
    pos=PosEnum.POSACTIVATION,
    mtype=TerminalTxnTypeEnum.SALE,
    currency=CurrencyEnum.USD,
    funding_currency=FundingCurrencyEnum.USD,
    swiped=SwipedEnum.SWIPED,
    merchant='t1_mer_64415e89a919c1566a2b49b',
    mid='4445061378323',
    pin=PinEnum.NOPIN,
    reserved=0,
    signature=SignatureEnum.NOTCAPTURED,
    total=8000,
    status=TerminalTxnStatusEnum.APPROVED,
    inactive=InactiveEnum.ACTIVE,
    frozen=FrozenEnum.NOTFROZEN,
    expiration='1023',
    forterminal_txn='forterminalTxn',
    payment=TerminalTxnsPayment(
        method=TerminalTxnPaymentMethodEnum.AMEX,
        number='1234',
        routing='123456789',
        expiration='1023',
        cvv=123,
        track='Track1'
    ),
    platform=Platform1Enum.VCORE,
    receipt=ReceiptEnum.NORECEIPT,
    tid='Terminal ID',
    trace_number=853202,
    txn='related txn',
    token='124f2d0efab0bcda46f2118d688bbf97',
    payment_number=7,
    payment_method=TerminalTxnPaymentMethodEnum.VISA,
    tip=0,
    originating_app='originatingApp',
    oemt_txn_ref_number='TxnRefNumber',
    pos_application_id='15668',
    pos_application_name='XML Test Example',
    pos_application_version='1.00',
    customer_reference_number='123456',
    gateway_transaction_id='486689252',
    customer_ticket_number='123456',
    auth_code='authorization code',
    auth_date=20160120,
    cashback=0,
    client_ip='Client IP address',
    company='company1',
    cvv_status=CvvStatusEnum.NOTPRESENT,
    description='description1',
    discount=0,
    duty=0,
    email='john.johnson@example.com',
    entry_mode=EntryModeEnum.KEYED,
    fee=0,
    first='John',
    last='Doe',
    middle='M',
    order='orderId',
    shipping=0,
    tax=0,
    terminal='identifier of terminal',
    terminal_capability=TerminalCapabilityEnum.KEYED,
    unattended=UnattendedEnum.ATTENDEDTERMINAL,
    address_1='address1',
    address_2='address2',
    city='city1',
    state='AB',
    zip='ZIP code',
    country=CountryEnum.CAN,
    phone='9999888888'
)

request_token = '20250423-yourmerchant-refunds-001'

try:
    result = terminal_transactions_controller.post_terminal_txns(
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

