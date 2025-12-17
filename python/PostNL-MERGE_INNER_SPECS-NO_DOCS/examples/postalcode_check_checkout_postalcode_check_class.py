from postnlecommerce.configuration import Environment
from postnlecommerce.exceptions.api_exception import APIException
from postnlecommerce.exceptions.barcode_response_error_exception import BarcodeResponseErrorException
from postnlecommerce.exceptions.barcode_response_invalid_exception import BarcodeResponseInvalidException
from postnlecommerce.exceptions.method_not_allowed_only_get_post_exception import MethodNotAllowedOnlyGetPostException
from postnlecommerce.http.auth.custom_header_authentication import CustomHeaderAuthenticationCredentials
from postnlecommerce.postnlecommerce_client import PostnlecommerceClient

client = PostnlecommerceClient(
    custom_header_authentication_credentials=CustomHeaderAuthenticationCredentials(
        apikey='apikey'
    ),
    environment=Environment.PRODUCTION_SERVER
)

postalcode_check_controller = client.postalcode_check
postalcode = '3571ZZ'

housenumber = '74'

housenumberaddition = 'bis'

try:
    result = postalcode_check_controller.checkout_postalcode_check(
        postalcode,
        housenumber,
        housenumberaddition=housenumberaddition
    )

    if result.is_success():
        print(result.body)
    elif result.is_error():
        print(result.errors)

except BarcodeResponseInvalidException as e: 
    print(e)
except MethodNotAllowedOnlyGetPostException as e: 
    print(e)
except BarcodeResponseErrorException as e: 
    print(e)
except APIException as e: 
    print(e)

