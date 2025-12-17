from postnlecommerce.configuration import Environment
from postnlecommerce.exceptions.api_exception import APIException
from postnlecommerce.exceptions.barcode_response_error_exception import BarcodeResponseErrorException
from postnlecommerce.exceptions.method_not_allowed_only_get_post_exception import MethodNotAllowedOnlyGetPostException
from postnlecommerce.exceptions.timeframe_response_invalid_exception import TimeframeResponseInvalidException
from postnlecommerce.http.auth.custom_header_authentication import CustomHeaderAuthenticationCredentials
from postnlecommerce.models.countrycode_enum import CountrycodeEnum
from postnlecommerce.models.options_2_enum import Options2Enum
from postnlecommerce.postnlecommerce_client import PostnlecommerceClient

client = PostnlecommerceClient(
    custom_header_authentication_credentials=CustomHeaderAuthenticationCredentials(
        apikey='apikey'
    ),
    environment=Environment.PRODUCTION_SERVER
)

timeframes_controller = client.timeframes
allow_sunday_sorting = False

start_date = '30-06-2022'

end_date = '02-07-2022'

country_code = CountrycodeEnum.NL

postal_code = '2132WT'

house_number = 42

options = [
    Options2Enum.DAYTIME,
    Options2Enum.EVENING,
    Options2Enum.SUNDAY
]

house_nr_ext = 'A'

city = 'Hoofddorp'

street = 'Siriusdreef'

try:
    result = timeframes_controller.retrieve_delivery_timeframes(
        allow_sunday_sorting,
        start_date,
        end_date,
        country_code,
        postal_code,
        house_number,
        options,
        house_nr_ext=house_nr_ext,
        city=city,
        street=street
    )

    if result.is_success():
        print(result.body)
    elif result.is_error():
        print(result.errors)

except TimeframeResponseInvalidException as e: 
    print(e)
except MethodNotAllowedOnlyGetPostException as e: 
    print(e)
except BarcodeResponseErrorException as e: 
    print(e)
except APIException as e: 
    print(e)

