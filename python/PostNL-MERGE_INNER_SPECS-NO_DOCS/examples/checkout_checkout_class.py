from postnlecommerce.configuration import Environment
from postnlecommerce.exceptions.api_exception import APIException
from postnlecommerce.exceptions.barcode_response_error_exception import BarcodeResponseErrorException
from postnlecommerce.exceptions.checkout_response_invalid_exception import CheckoutResponseInvalidException
from postnlecommerce.exceptions.method_not_allowed_only_get_post_exception import MethodNotAllowedOnlyGetPostException
from postnlecommerce.http.auth.custom_header_authentication import CustomHeaderAuthenticationCredentials
from postnlecommerce.models.address import Address
from postnlecommerce.models.address_type_enum import AddressTypeEnum
from postnlecommerce.models.checkout_request import CheckoutRequest
from postnlecommerce.models.countrycode_enum import CountrycodeEnum
from postnlecommerce.models.cut_off_time import CutOffTime
from postnlecommerce.models.day_enum import DayEnum
from postnlecommerce.models.option_enum import OptionEnum
from postnlecommerce.models.type_1_enum import Type1Enum
from postnlecommerce.postnlecommerce_client import PostnlecommerceClient

client = PostnlecommerceClient(
    custom_header_authentication_credentials=CustomHeaderAuthenticationCredentials(
        apikey='apikey'
    ),
    environment=Environment.PRODUCTION_SERVER
)

checkout_controller = client.checkout
body = CheckoutRequest(
    order_date='24-02-2021 12:00:00',
    cut_off_times=[
        CutOffTime(
            day=DayEnum.ENUM_00,
            available=True,
            mtype=Type1Enum.REGULAR,
            time='20:00:00'
        ),
        CutOffTime(
            day=DayEnum.ENUM_00,
            available=True,
            mtype=Type1Enum.TODAY,
            time='12:00:00'
        )
    ],
    options=[
        OptionEnum.DAYTIME,
        OptionEnum.EVENING,
        OptionEnum.TODAY,
        OptionEnum.SUNDAY,
        OptionEnum.PICKUP
    ],
    locations=2,
    days=3,
    addresses=[
        Address(
            address_type=AddressTypeEnum.ENUM_01,
            house_nr=74,
            zipcode='3571ZZ',
            countrycode=CountrycodeEnum.NL,
            street='Molengraaffplantsoen',
            city='Utrecht'
        )
    ],
    shipping_duration=1,
    holiday_sorting=True
)

try:
    result = checkout_controller.checkout(body)

    if result.is_success():
        print(result.body)
    elif result.is_error():
        print(result.errors)

except CheckoutResponseInvalidException as e: 
    print(e)
except MethodNotAllowedOnlyGetPostException as e: 
    print(e)
except BarcodeResponseErrorException as e: 
    print(e)
except APIException as e: 
    print(e)

