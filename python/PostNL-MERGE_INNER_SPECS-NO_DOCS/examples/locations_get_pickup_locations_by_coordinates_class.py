from postnlecommerce.configuration import Environment
from postnlecommerce.exceptions.api_exception import APIException
from postnlecommerce.exceptions.barcode_response_error_exception import BarcodeResponseErrorException
from postnlecommerce.exceptions.locations_response_invalid_exception import LocationsResponseInvalidException
from postnlecommerce.exceptions.method_not_allowed_only_get_post_exception import MethodNotAllowedOnlyGetPostException
from postnlecommerce.http.auth.custom_header_authentication import CustomHeaderAuthenticationCredentials
from postnlecommerce.models.countrycode_enum import CountrycodeEnum
from postnlecommerce.postnlecommerce_client import PostnlecommerceClient

client = PostnlecommerceClient(
    custom_header_authentication_credentials=CustomHeaderAuthenticationCredentials(
        apikey='apikey'
    ),
    environment=Environment.PRODUCTION_SERVER
)

locations_controller = client.locations
latitude = 52.2864669620795

longitude = 4.68239055845954

country_code = CountrycodeEnum.NL

delivery_date = '24-12-2022'

opening_time = '09:00:00'

try:
    result = locations_controller.get_pickup_locations_by_coordinates(
        latitude,
        longitude,
        country_code,
        delivery_date=delivery_date,
        opening_time=opening_time
    )

    if result.is_success():
        print(result.body)
    elif result.is_error():
        print(result.errors)

except LocationsResponseInvalidException as e: 
    print(e)
except MethodNotAllowedOnlyGetPostException as e: 
    print(e)
except BarcodeResponseErrorException as e: 
    print(e)
except APIException as e: 
    print(e)

