from payrix.configuration import Environment
from payrix.exceptions.api_exception import APIException
from payrix.exceptions.error_four_hundred_exception import ErrorFourHundredException
from payrix.http.auth.api_key import ApiKeyCredentials
from payrix.http.auth.session_key import SessionKeyCredentials
from payrix.http.auth.txn_session_key import TxnSessionKeyCredentials
from payrix.models.advanced_billing_enum import AdvancedBillingEnum
from payrix.models.apple_pay_active_enum import ApplePayActiveEnum
from payrix.models.auto_boarded_enum import AutoBoardedEnum
from payrix.models.express_batch_close_method_enum import ExpressBatchCloseMethodEnum
from payrix.models.frozen_enum import FrozenEnum
from payrix.models.google_pay_active_enum import GooglePayActiveEnum
from payrix.models.inactive_enum import InactiveEnum
from payrix.models.incremental_auth_supported_enum import IncrementalAuthSupportedEnum
from payrix.models.letter_status_enum import LetterStatusEnum
from payrix.models.merchant_environment_enum import MerchantEnvironmentEnum
from payrix.models.merchant_location_type_enum import MerchantLocationTypeEnum
from payrix.models.merchant_status_enum import MerchantStatusEnum
from payrix.models.merchants_put_request import MerchantsPutRequest
from payrix.models.naics_enum import NaicsEnum
from payrix.models.new_enum import NewEnum
from payrix.models.omni_token_enabled_enum import OmniTokenEnabledEnum
from payrix.models.pass_token_enabled_enum import PassTokenEnabledEnum
from payrix.models.risk_level_enum import RiskLevelEnum
from payrix.models.saq_type_enum import SaqTypeEnum
from payrix.models.seasonal_enum import SeasonalEnum
from payrix.models.status_reason_enum import StatusReasonEnum
from payrix.models.tc_attestation_enum import TcAttestationEnum
from payrix.models.visa_disclosure_enum import VisaDisclosureEnum
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

merchants_controller = client.merchants
id = 'p1_mer_00c6b12d04ac280ed694323'

body = MerchantsPutRequest(
    total_approved_sales=0,
    entity='p1_ent_00c94cb712c4cb8ecbe4c88',
    dba='DISPOSAL LLC',
    new=NewEnum.NOTNEW,
    advanced_billing=AdvancedBillingEnum.DISABLED,
    seasonal=SeasonalEnum.YEARROUND,
    established=20210916,
    annual_cc_sales=2530,
    annual_cc_sale_volume=2530,
    annual_ach_sale_volume=2530,
    amex_volume=0,
    avg_ticket=56000,
    amex='American Express merchant identifier',
    discover='Discover merchant identifier',
    mcc='1799',
    visa_mvv='Merchant Verification Value',
    visa_disclosure=VisaDisclosureEnum.NOTACCEPTED,
    disclosure_ip='11.11.11.111',
    disclosure_date=20250307,
    environment=MerchantEnvironmentEnum.CARDPRESENT,
    status=MerchantStatusEnum.BOARDED,
    incremental_auth_supported=IncrementalAuthSupportedEnum.NOTSUPPORTED,
    auto_boarded=AutoBoardedEnum.AUTOBOARDED,
    status_reason=StatusReasonEnum.FRAUD,
    location_type=MerchantLocationTypeEnum.RETAILSTOREFRONT,
    percent_ecomm=70,
    percent_keyed=30,
    percent_business=0,
    total_volume=1000000,
    account_closure_reason_code='reason code',
    account_closure_reason_date=20250307,
    risk_level=RiskLevelEnum.RESTRICTED,
    credit_ratio=0,
    credit_timeliness=0,
    chargeback_ratio=0,
    ndx_days=1,
    ndx_percentage=0,
    saq_type=SaqTypeEnum.SAQA,
    saq_date=20250307,
    qsa='0',
    letter_status=LetterStatusEnum.OFF,
    letter_date=20250307,
    chargeback_notification_email='Notification Email',
    tc_attestation=TcAttestationEnum.NOTACCEPTED,
    apple_pay_active=ApplePayActiveEnum.INACTIVE,
    google_pay_active=GooglePayActiveEnum.ACTIVE,
    naics=NaicsEnum.AGRICULTURE,
    naics_description='other',
    tmx_session_id='007462d6-a1df-40f4-b998-35bfa5539562',
    pass_token_enabled=PassTokenEnabledEnum.DISABLED,
    express_batch_close_method=ExpressBatchCloseMethodEnum.TIMEINITIATED,
    express_batch_close_time='03:00:00',
    tin_status=0,
    omni_token_enabled=OmniTokenEnabledEnum.DISABLED,
    inactive=InactiveEnum.ACTIVE,
    frozen=FrozenEnum.NOTFROZEN
)

request_token = '20250423-yourmerchant-refunds-001'

try:
    result = merchants_controller.put_merchants_id(
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

