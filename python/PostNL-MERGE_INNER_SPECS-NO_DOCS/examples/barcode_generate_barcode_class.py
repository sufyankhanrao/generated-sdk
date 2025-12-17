from postnlecommerce.configuration import Environment
from postnlecommerce.exceptions.api_exception import APIException
from postnlecommerce.exceptions.barcode_response_error_exception import BarcodeResponseErrorException
from postnlecommerce.exceptions.barcode_response_invalid_exception import BarcodeResponseInvalidException
from postnlecommerce.exceptions.method_not_allowed_only_get_post_exception import MethodNotAllowedOnlyGetPostException
from postnlecommerce.exceptions.too_many_requests_exception import TooManyRequestsException
from postnlecommerce.exceptions.unauthorized_exception import UnauthorizedException
from postnlecommerce.http.auth.custom_header_authentication import CustomHeaderAuthenticationCredentials
from postnlecommerce.models.type_enum import TypeEnum
from postnlecommerce.postnlecommerce_client import PostnlecommerceClient

client = PostnlecommerceClient(
    custom_header_authentication_credentials=CustomHeaderAuthenticationCredentials(
        apikey='apikey'
    ),
    environment=Environment.PRODUCTION_SERVER
)

barcode_controller = client.barcode
customer_code = 'DEVC'

customer_number = '11223344'

mtype = TypeEnum.ENUM_3S

try:
    result = barcode_controller.generate_barcode(
        customer_code,
        customer_number,
        mtype
    )

    if result.is_success():
        print(result.body)
    elif result.is_error():
        print(result.errors)

except BarcodeResponseInvalidException as e: 
    print(e)
except UnauthorizedException as e: 
    print(e)
except MethodNotAllowedOnlyGetPostException as e: 
    print(e)
except TooManyRequestsException as e: 
    print(e)
except BarcodeResponseErrorException as e: 
    print(e)
except APIException as e: 
    print(e)

