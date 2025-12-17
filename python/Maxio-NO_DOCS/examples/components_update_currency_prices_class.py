from advancedbilling.advanced_billing_client import AdvancedBillingClient
from advancedbilling.configuration import Environment
from advancedbilling.exceptions.api_exception import APIException
from advancedbilling.exceptions.error_array_map_response_exception import ErrorArrayMapResponseException
from advancedbilling.http.auth.basic_auth import BasicAuthCredentials
from advancedbilling.models.update_currency_price import UpdateCurrencyPrice
from advancedbilling.models.update_currency_prices_request import UpdateCurrencyPricesRequest

client = AdvancedBillingClient(
    basic_auth_credentials=BasicAuthCredentials(
        username='BasicAuthUserName',
        password='BasicAuthPassword'
    ),
    environment=Environment.PRODUCTION,
    subdomain='subdomain',
    domain='chargify.com'
)

components_controller = client.components
price_point_id = 10

body = UpdateCurrencyPricesRequest(
    currency_prices=[
        UpdateCurrencyPrice(
            id=100,
            price=51
        ),
        UpdateCurrencyPrice(
            id=101,
            price=41
        )
    ]
)

try:
    result = components_controller.update_currency_prices(
        price_point_id,
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

