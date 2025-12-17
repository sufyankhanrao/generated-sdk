from postnlecommerce.configuration import Environment
from postnlecommerce.exceptions.api_exception import APIException
from postnlecommerce.exceptions.barcode_response_error_exception import BarcodeResponseErrorException
from postnlecommerce.exceptions.confirming_response_error_1_exception import ConfirmingResponseError1Exception
from postnlecommerce.exceptions.method_not_allowed_only_get_post_exception import MethodNotAllowedOnlyGetPostException
from postnlecommerce.http.auth.custom_header_authentication import CustomHeaderAuthenticationCredentials
from postnlecommerce.models.address_11 import Address11
from postnlecommerce.models.address_2 import Address2
from postnlecommerce.models.confirming_request import ConfirmingRequest
from postnlecommerce.models.contact import Contact
from postnlecommerce.models.customer import Customer
from postnlecommerce.models.dimension import Dimension
from postnlecommerce.models.message import Message
from postnlecommerce.models.shipment import Shipment
from postnlecommerce.postnlecommerce_client import PostnlecommerceClient

client = PostnlecommerceClient(
    custom_header_authentication_credentials=CustomHeaderAuthenticationCredentials(
        apikey='apikey'
    ),
    environment=Environment.PRODUCTION_SERVER
)

confirming_controller = client.confirming
body = ConfirmingRequest(
    customer=Customer(
        customer_code='DEVC',
        customer_number='11223344',
        address=Address2(
            address_type='02',
            city='Den Haag',
            countrycode='NL',
            company_name='PostNL',
            house_nr='3',
            street='Waldorpstraat',
            zipcode='2521CA'
        ),
        collection_location='123456',
        contact_person='Janssen',
        email='email@company.com',
        name='Janssen'
    ),
    message=Message(
        message_id='1',
        message_time_stamp='08-09-2022 12:00:00'
    ),
    shipments=[
        Shipment(
            addresses=[
                Address11(
                    address_type='01',
                    countrycode='NL',
                    city='Utrecht',
                    first_name='Peter',
                    house_nr='9',
                    house_nr_ext='a bis',
                    name='de Ruiter',
                    street='Bilderdijkstraat',
                    zipcode='3532VA'
                )
            ],
            barcode='3SDEVC748859096',
            dimension=Dimension(
                weight=2000
            ),
            product_code_delivery='3085',
            contacts=[
                Contact(
                    contact_type='01',
                    email='receiver@email.com',
                    sms_nr='+31612345678',
                    tel_nr='+31301234567'
                )
            ]
        )
    ]
)

try:
    result = confirming_controller.confirm_shipment(body)

    if result.is_success():
        print(result.body)
    elif result.is_error():
        print(result.errors)

except ConfirmingResponseError1Exception as e: 
    print(e)
except MethodNotAllowedOnlyGetPostException as e: 
    print(e)
except BarcodeResponseErrorException as e: 
    print(e)
except APIException as e: 
    print(e)

