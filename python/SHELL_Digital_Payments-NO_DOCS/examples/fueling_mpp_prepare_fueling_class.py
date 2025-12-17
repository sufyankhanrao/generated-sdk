from shelldigitalpayments.configuration import Environment
from shelldigitalpayments.exceptions.api_exception import APIException
from shelldigitalpayments.http.auth.mpp_token import MppTokenCredentials
from shelldigitalpayments.http.auth.o_auth_token_post import OAuthTokenPostCredentials
from shelldigitalpayments.models.loyalty_details import LoyaltyDetails
from shelldigitalpayments.models.payment_details_items import PaymentDetailsItems
from shelldigitalpayments.models.payment_properties import PaymentProperties
from shelldigitalpayments.models.prepare_fueling_request import PrepareFuelingRequest
from shelldigitalpayments.shell_digital_payments_client import ShellDigitalPaymentsClient

client = ShellDigitalPaymentsClient(
    mpp_token_credentials=MppTokenCredentials(
        authorization='Authorization'
    ),
    o_auth_token_post_credentials=OAuthTokenPostCredentials(
        x_apigee_authorization='X-Apigee-Authorization'
    ),
    environment=Environment.PRODUCTION
)

fueling_controller = client.fueling
site_country = 'NL'

currency = 'EUR'

body = PrepareFuelingRequest(
    latitude=12.92452,
    longitude=77.68862,
    station_id='9955',
    pump_id='1',
    source_application='PARTNER_APP_EXAMPLE',
    payment_details=[
        PaymentDetailsItems(
            payment_method_id='euroShell',
            payment_properties=PaymentProperties(
                card_identifier='98e4ffd3-4146-4e94-8445-e02f4ce87a77'
            )
        )
    ],
    loyalty_details=[
        LoyaltyDetails(
            loyalty_id='70043201060148830',
            loyalty_type='Shell'
        )
    ]
)

try:
    result = fueling_controller.mpp_prepare_fueling(
        site_country,
        currency,
        body
    )

    if result.is_success():
        print(result.body)
    elif result.is_error():
        print(result.errors)

except APIException as e: 
    print(e)

