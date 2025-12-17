from shelldigitalpayments.configuration import Environment
from shelldigitalpayments.exceptions.api_exception import APIException
from shelldigitalpayments.exceptions.payment_enablement_error_response_exception import PaymentEnablementErrorResponseException
from shelldigitalpayments.http.auth.o_auth_token_post import OAuthTokenPostCredentials
from shelldigitalpayments.models.collecting_company import CollectingCompany
from shelldigitalpayments.models.mobile_payment_registration_request import MobilePaymentRegistrationRequest
from shelldigitalpayments.shell_digital_payments_client import ShellDigitalPaymentsClient

client = ShellDigitalPaymentsClient(
    o_auth_token_post_credentials=OAuthTokenPostCredentials(
        x_apigee_authorization='X-Apigee-Authorization'
    ),
    environment=Environment.PRODUCTION
)

digital_payment_enablement_controller = client.digital_payment_enablement
body = MobilePaymentRegistrationRequest(
    reference_id='caa29807-6fa7-4801-87bb-dd975e2cbf41',
    pan='7077141290120180000',
    pan_expiry='2101',
    period=3,
    account_id='8682',
    payer_id='8682',
    col_co_id='32',
    collecting_companies=[
        CollectingCompany(
            col_co_id='32'
        )
    ]
)

try:
    result = digital_payment_enablement_controller.mpay_v_1_tokens_ref_put(body)

    if result.is_success():
        print(result.body)
    elif result.is_error():
        print(result.errors)

except PaymentEnablementErrorResponseException as e: 
    print(e)
except APIException as e: 
    print(e)

