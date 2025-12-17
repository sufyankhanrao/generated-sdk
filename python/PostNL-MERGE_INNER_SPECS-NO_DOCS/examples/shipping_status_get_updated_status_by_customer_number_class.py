from postnlecommerce.configuration import Environment
from postnlecommerce.exceptions.api_exception import APIException
from postnlecommerce.exceptions.barcode_response_error_exception import BarcodeResponseErrorException
from postnlecommerce.exceptions.method_not_allowed_only_get_post_exception import MethodNotAllowedOnlyGetPostException
from postnlecommerce.http.auth.custom_header_authentication import CustomHeaderAuthenticationCredentials
from postnlecommerce.postnlecommerce_client import PostnlecommerceClient

client = PostnlecommerceClient(
    custom_header_authentication_credentials=CustomHeaderAuthenticationCredentials(
        apikey='apikey'
    ),
    environment=Environment.PRODUCTION_SERVER
)

shipping_status_controller = client.shipping_status
customernumber = '11223344'

period = [
    '2022-11-07T12:00:00.000',
    '2022-11-07T12:05:00.000'
]

try:
    result = shipping_status_controller.get_updated_status_by_customer_number(
        customernumber,
        period=period
    )

    if result.is_success():
        print(result.body)
    elif result.is_error():
        print(result.errors)

except BarcodeResponseErrorException as e: 
    print(e)
except MethodNotAllowedOnlyGetPostException as e: 
    print(e)
except APIException as e: 
    print(e)

