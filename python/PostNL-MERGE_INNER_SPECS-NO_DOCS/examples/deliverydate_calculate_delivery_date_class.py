from postnlecommerce.configuration import Environment
from postnlecommerce.exceptions.api_exception import APIException
from postnlecommerce.exceptions.barcode_response_error_exception import BarcodeResponseErrorException
from postnlecommerce.exceptions.deliverydate_response_invalid_exception import DeliverydateResponseInvalidException
from postnlecommerce.exceptions.method_not_allowed_only_get_post_exception import MethodNotAllowedOnlyGetPostException
from postnlecommerce.http.auth.custom_header_authentication import CustomHeaderAuthenticationCredentials
from postnlecommerce.models.countrycode_enum import CountrycodeEnum
from postnlecommerce.models.option_3_enum import Option3Enum
from postnlecommerce.postnlecommerce_client import PostnlecommerceClient

client = PostnlecommerceClient(
    custom_header_authentication_credentials=CustomHeaderAuthenticationCredentials(
        apikey='apikey'
    ),
    environment=Environment.PRODUCTION_SERVER
)

deliverydate_controller = client.deliverydate
shipping_date = '29-05-2022 14:00:00'

shipping_duration = 1

cut_off_time = '17:00:00'

postal_code = '2132WT'

country_code = CountrycodeEnum.NL

options = [
    Option3Enum.SUNDAY,
    Option3Enum.TODAY,
    Option3Enum.AFTERNOON
]

origin_country_code = CountrycodeEnum.NL

city = 'Hoofddorp'

street = 'Siriusdreef'

house_number = 42

house_nr_ext = 'A'

try:
    result = deliverydate_controller.calculate_delivery_date(
        shipping_date,
        shipping_duration,
        cut_off_time,
        postal_code,
        country_code,
        options,
        origin_country_code=origin_country_code,
        city=city,
        street=street,
        house_number=house_number,
        house_nr_ext=house_nr_ext
    )

    if result.is_success():
        print(result.body)
    elif result.is_error():
        print(result.errors)

except DeliverydateResponseInvalidException as e: 
    print(e)
except MethodNotAllowedOnlyGetPostException as e: 
    print(e)
except BarcodeResponseErrorException as e: 
    print(e)
except APIException as e: 
    print(e)

