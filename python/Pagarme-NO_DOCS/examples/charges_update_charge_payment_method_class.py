
from pagarmeapisdk.configuration import Environment
from pagarmeapisdk.exceptions.api_exception import APIException
from pagarmeapisdk.exceptions.error_exception import ErrorException
from pagarmeapisdk.http.auth.basic_auth import BasicAuthCredentials
from pagarmeapisdk.models.create_address_request import CreateAddressRequest
from pagarmeapisdk.models.create_bank_transfer_payment_request import CreateBankTransferPaymentRequest
from pagarmeapisdk.models.create_boleto_payment_request import CreateBoletoPaymentRequest
from pagarmeapisdk.models.create_cash_payment_request import CreateCashPaymentRequest
from pagarmeapisdk.models.create_credit_card_payment_request import CreateCreditCardPaymentRequest
from pagarmeapisdk.models.create_debit_card_payment_request import CreateDebitCardPaymentRequest
from pagarmeapisdk.models.create_private_label_payment_request import CreatePrivateLabelPaymentRequest
from pagarmeapisdk.models.create_voucher_payment_request import CreateVoucherPaymentRequest
from pagarmeapisdk.models.update_charge_payment_method_request import UpdateChargePaymentMethodRequest
from pagarmeapisdk.pagarmeapisdk_client import PagarmeapisdkClient

client = PagarmeapisdkClient(
    service_referer_name='ServiceRefererName',
    basic_auth_credentials=BasicAuthCredentials(
        username='BasicAuthUserName',
        password='BasicAuthPassword'
    ),
    environment=Environment.PRODUCTION
)

charges_controller = client.charges
charge_id = 'charge_id8'

request = UpdateChargePaymentMethodRequest(
    update_subscription=False,
    payment_method='payment_method4',
    credit_card=CreateCreditCardPaymentRequest(
        installments=1,
        capture=True,
        recurrency_cycle='"first" or "subsequent"'
    ),
    debit_card=CreateDebitCardPaymentRequest(),
    boleto=CreateBoletoPaymentRequest(
        retries=226,
        instructions='instructions2',
        billing_address=CreateAddressRequest(
            street='street8',
            number='number4',
            zip_code='zip_code2',
            neighborhood='neighborhood4',
            city='city2',
            state='state6',
            country='country2',
            complement='complement6',
            line_1='line_18',
            line_2='line_26'
        ),
        document_number='document_number6',
        statement_descriptor='statement_descriptor0'
    ),
    voucher=CreateVoucherPaymentRequest(
        recurrency_cycle='"first" or "subsequent"'
    ),
    cash=CreateCashPaymentRequest(
        description='description0',
        confirm=False
    ),
    bank_transfer=CreateBankTransferPaymentRequest(
        bank='bank0',
        retries=236
    ),
    private_label=CreatePrivateLabelPaymentRequest(
        installments=1,
        capture=True,
        recurrency_cycle='"first" or "subsequent"'
    )
)

try:
    result = charges_controller.update_charge_payment_method(
        charge_id,
        request
    )

    if result.is_success():
        print(result.body)
    elif result.is_error():
        print(result.errors)

except ErrorException as e: 
    print(e)
except APIException as e: 
    print(e)

