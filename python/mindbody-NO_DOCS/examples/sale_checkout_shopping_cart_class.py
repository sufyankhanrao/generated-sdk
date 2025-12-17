import dateutil.parser

from mindbodypublicapi.configuration import Environment
from mindbodypublicapi.exceptions.api_exception import APIException
from mindbodypublicapi.mindbodypublicapi_client import MindbodypublicapiClient
from mindbodypublicapi.models.checkout_appointment_booking_request import CheckoutAppointmentBookingRequest
from mindbodypublicapi.models.checkout_item import CheckoutItem
from mindbodypublicapi.models.checkout_item_wrapper import CheckoutItemWrapper
from mindbodypublicapi.models.checkout_payment_info import CheckoutPaymentInfo
from mindbodypublicapi.models.checkout_shopping_cart_request import CheckoutShoppingCartRequest
from mindbodypublicapi.models.resource_slim import ResourceSlim

client = MindbodypublicapiClient(
    environment=Environment.PRODUCTION
)

sale_controller = client.sale
version = '6'

request = CheckoutShoppingCartRequest(
    client_id='ClientId0',
    items=[
        CheckoutItemWrapper(
            item=CheckoutItem(
                mtype='Type2',
                metadata={
                    'key0': {"key1":"val1","key2":"val2"}
                }
            ),
            discount_amount=41.36,
            appointment_booking_requests=[
                CheckoutAppointmentBookingRequest(
                    staff_id=16,
                    location_id=66,
                    session_type_id=166,
                    resources=[
                        ResourceSlim(
                            id=216,
                            name='Name6'
                        ),
                        ResourceSlim(
                            id=216,
                            name='Name6'
                        ),
                        ResourceSlim(
                            id=216,
                            name='Name6'
                        )
                    ],
                    start_date_time=dateutil.parser.parse('2016-03-13T12:52:32.123Z')
                )
            ],
            enrollment_ids=[
                249,
                250
            ],
            class_ids=[
                153,
                154,
                155
            ]
        ),
        CheckoutItemWrapper(
            item=CheckoutItem(
                mtype='Type2',
                metadata={
                    'key0': {"key1":"val1","key2":"val2"}
                }
            ),
            discount_amount=41.36,
            appointment_booking_requests=[
                CheckoutAppointmentBookingRequest(
                    staff_id=16,
                    location_id=66,
                    session_type_id=166,
                    resources=[
                        ResourceSlim(
                            id=216,
                            name='Name6'
                        ),
                        ResourceSlim(
                            id=216,
                            name='Name6'
                        ),
                        ResourceSlim(
                            id=216,
                            name='Name6'
                        )
                    ],
                    start_date_time=dateutil.parser.parse('2016-03-13T12:52:32.123Z')
                )
            ],
            enrollment_ids=[
                249,
                250
            ],
            class_ids=[
                153,
                154,
                155
            ]
        ),
        CheckoutItemWrapper(
            item=CheckoutItem(
                mtype='Type2',
                metadata={
                    'key0': {"key1":"val1","key2":"val2"}
                }
            ),
            discount_amount=41.36,
            appointment_booking_requests=[
                CheckoutAppointmentBookingRequest(
                    staff_id=16,
                    location_id=66,
                    session_type_id=166,
                    resources=[
                        ResourceSlim(
                            id=216,
                            name='Name6'
                        ),
                        ResourceSlim(
                            id=216,
                            name='Name6'
                        ),
                        ResourceSlim(
                            id=216,
                            name='Name6'
                        )
                    ],
                    start_date_time=dateutil.parser.parse('2016-03-13T12:52:32.123Z')
                )
            ],
            enrollment_ids=[
                249,
                250
            ],
            class_ids=[
                153,
                154,
                155
            ]
        )
    ],
    payments=[
        CheckoutPaymentInfo(
            mtype='Type8',
            metadata={
                'key0': {"key1":"val1","key2":"val2"},
                'key1': {"key1":"val1","key2":"val2"}
            }
        ),
        CheckoutPaymentInfo(
            mtype='Type8',
            metadata={
                'key0': {"key1":"val1","key2":"val2"},
                'key1': {"key1":"val1","key2":"val2"}
            }
        ),
        CheckoutPaymentInfo(
            mtype='Type8',
            metadata={
                'key0': {"key1":"val1","key2":"val2"},
                'key1': {"key1":"val1","key2":"val2"}
            }
        )
    ],
    cart_id='CartId0',
    test=False,
    in_store=False,
    calculate_tax=False,
    promotion_code='PromotionCode2'
)

site_id = '-99'

authorization = 'authorization6'

try:
    result = sale_controller.checkout_shopping_cart(
        version,
        request,
        site_id,
        authorization=authorization
    )

    if result.is_success():
        print(result.body)
    elif result.is_error():
        print(result.errors)

except APIException as e: 
    print(e)

