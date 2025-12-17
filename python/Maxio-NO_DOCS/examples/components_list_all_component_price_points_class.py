import dateutil.parser

from advancedbilling.advanced_billing_client import AdvancedBillingClient
from advancedbilling.configuration import Environment
from advancedbilling.exceptions.api_exception import APIException
from advancedbilling.exceptions.error_list_response_exception import ErrorListResponseException
from advancedbilling.http.auth.basic_auth import BasicAuthCredentials
from advancedbilling.models.list_components_price_points_include import ListComponentsPricePointsInclude
from advancedbilling.models.list_price_points_filter import ListPricePointsFilter
from advancedbilling.models.price_point_type import PricePointType

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
collect = {
    'include': ListComponentsPricePointsInclude.CURRENCY_PRICES,
    'page': 2,
    'per_page': 50,
    'filter': ListPricePointsFilter(
        start_date=dateutil.parser.parse('2011-12-17').date(),
        end_date=dateutil.parser.parse('2011-12-15').date(),
        start_datetime=dateutil.parser.parse('2011-12-19T10:15:30+01:00'),
        end_datetime=dateutil.parser.parse('2019-06-07T17:20:06Z'),
        mtype=[
            PricePointType.CATALOG,
            PricePointType.DEFAULT,
            PricePointType.CUSTOM
        ],
        ids=[
            1,
            2,
            3
        ]
    )
}
try:
    result = components_controller.list_all_component_price_points(collect)

    if result.is_success():
        print(result.body)
    elif result.is_error():
        print(result.errors)

except ErrorListResponseException as e: 
    print(e)
except APIException as e: 
    print(e)

