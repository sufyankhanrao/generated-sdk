from advancedbilling.advanced_billing_client import AdvancedBillingClient
from advancedbilling.configuration import Environment
from advancedbilling.exceptions.api_exception import APIException
from advancedbilling.exceptions.error_array_map_response_exception import ErrorArrayMapResponseException
from advancedbilling.http.auth.basic_auth import BasicAuthCredentials
from advancedbilling.models.create_offer import CreateOffer
from advancedbilling.models.create_offer_component import CreateOfferComponent
from advancedbilling.models.create_offer_request import CreateOfferRequest

client = AdvancedBillingClient(
    basic_auth_credentials=BasicAuthCredentials(
        username='BasicAuthUserName',
        password='BasicAuthPassword'
    ),
    environment=Environment.PRODUCTION,
    subdomain='subdomain',
    domain='chargify.com'
)

offers_controller = client.offers
body = CreateOfferRequest(
    offer=CreateOffer(
        name='Solo',
        handle='han_shot_first',
        product_id=31,
        description='A Star Wars Story',
        product_price_point_id=102,
        components=[
            CreateOfferComponent(
                component_id=24,
                starting_quantity=1
            )
        ],
        coupons=[
            'DEF456'
        ]
    )
)

try:
    result = offers_controller.create_offer(
        body=body
    )

    if result.is_success():
        print(result.body)
    elif result.is_error():
        print(result.errors)

except ErrorArrayMapResponseException as e: 
    print(e)
except APIException as e: 
    print(e)

