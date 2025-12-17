import jsonpickle

from payrix.configuration import Environment
from payrix.exceptions.api_exception import APIException
from payrix.exceptions.error_four_hundred_exception import ErrorFourHundredException
from payrix.http.auth.api_key import ApiKeyCredentials
from payrix.http.auth.session_key import SessionKeyCredentials
from payrix.http.auth.txn_session_key import TxnSessionKeyCredentials
from payrix.models.allow_partial_enum import AllowPartialEnum
from payrix.models.cof_type_enum import CofTypeEnum
from payrix.models.copy_reason_enum import CopyReasonEnum
from payrix.models.country_enum import CountryEnum
from payrix.models.currency_conversion_enum import CurrencyConversionEnum
from payrix.models.currency_enum import CurrencyEnum
from payrix.models.cvv_status_enum import CvvStatusEnum
from payrix.models.debt_repayment_enum import DebtRepaymentEnum
from payrix.models.entry_mode_enum import EntryModeEnum
from payrix.models.funding_currency_enum import FundingCurrencyEnum
from payrix.models.mobile_enum import MobileEnum
from payrix.models.pin_entry_capability_enum import PinEntryCapabilityEnum
from payrix.models.pin_enum import PinEnum
from payrix.models.pinless_debit_conversion_enum import PinlessDebitConversionEnum
from payrix.models.signature_enum import SignatureEnum
from payrix.models.swiped_enum import SwipedEnum
from payrix.models.terminal_capability_enum import TerminalCapabilityEnum
from payrix.models.txn_origin_1_enum import TxnOrigin1Enum
from payrix.models.txn_payment_method_enum import TxnPaymentMethodEnum
from payrix.models.txn_type_enum import TxnTypeEnum
from payrix.models.txns_funding_enabled_enum import TxnsFundingEnabledEnum
from payrix.models.txns_payment import TxnsPayment
from payrix.models.txns_platform_enum import TxnsPlatformEnum
from payrix.models.txns_post_request import TxnsPostRequest
from payrix.models.unattended_enum import UnattendedEnum
from payrix.models.unauth_reason_enum import UnauthReasonEnum
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

transactions_txns_controller = client.transactions_txns
body = TxnsPostRequest(
    allow_partial=AllowPartialEnum.ALLOWED,
    authentication='Authentication Token',
    debt_repayment=DebtRepaymentEnum.ON,
    fortxn='t1_txn_67b5f9801e463c908f453oo',
    origin=TxnOrigin1Enum.APPLE,
    platform=TxnsPlatformEnum.VANTIV,
    mtype=TxnTypeEnum.CAPTURE,
    unauth_reason=UnauthReasonEnum.CUSTOMERCANCELLED,
    currency=CurrencyEnum.DOP,
    funding_currency=FundingCurrencyEnum.BRL,
    swiped=SwipedEnum.SWIPED,
    merchant='t1_mer_1344e1a5460f5cfdf21ce11',
    mid='11003321',
    pin=PinEnum.PIN,
    signature=SignatureEnum.CAPTURED,
    total=1010,
    unattended=UnattendedEnum.UNATTENDEDTERMINAL,
    payment=TxnsPayment(
        method=TxnPaymentMethodEnum.VISA,
        number='1111',
        routing='code',
        cvv=11,
        track=jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    ),
    batch='t1_bth_67b6129bcca1cbb7cdac000',
    authentication_id='Optional transaction ID',
    cof_type=CofTypeEnum.SINGLE,
    currency_conversion=CurrencyConversionEnum.CUSTOMERACCEPTED,
    expiration='0623',
    fromtxn='Reauthorize an expired Transaction',
    copy_reason=CopyReasonEnum.RESUBMISSION,
    mobile=MobileEnum.NONMOBILEPOS,
    pin_entry_capability=PinEntryCapabilityEnum.UNKNOWN,
    pinless_debit_conversion=PinlessDebitConversionEnum.OFF,
    processed_sequence=0,
    funded=623,
    returned='Returned Transaction',
    funding_enabled=TxnsFundingEnabledEnum.DISABLED,
    fbo='WORLDPAY_FBO1',
    request_sequence=1,
    statement='statement ID',
    token='31b0ac1d55c898a7b6758ed2209fce00',
    auth_token_customer='Customer Identifier',
    channel='LA',
    cashback=0,
    client_ip='216.80.4.000',
    company='Hotdog Water',
    cvv_status=CvvStatusEnum.NOTPRESENT,
    description='Neon Test',
    discount=0,
    duty=0,
    email='robert.johnson@example.com',
    entry_mode=EntryModeEnum.KEYED,
    fee=997,
    first='Robert',
    last='Johnson',
    middle='John',
    order='identifier',
    shipping=0,
    tax=0,
    surcharge=0,
    terminal='Terminal Identifier',
    terminal_capability=TerminalCapabilityEnum.KEYED,
    address_1='708 Kunde Mission',
    address_2='Apt 3g',
    city='New York',
    state='NY',
    zip='10001',
    country=CountryEnum.USA,
    phone='1111111111',
    tmx_session_id='Threatmetrix session ID',
    first_txn='t1_txn_67b6129bcca1cbb7cdac001'
)

request_token = '20250423-yourmerchant-refunds-001'

try:
    result = transactions_txns_controller.post_txns(
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

