from postnlecommerce.configuration import Environment
from postnlecommerce.exceptions.api_exception import APIException
from postnlecommerce.exceptions.barcode_response_error_exception import BarcodeResponseErrorException
from postnlecommerce.exceptions.labelling_response_invalid_exception import LabellingResponseInvalidException
from postnlecommerce.exceptions.method_not_allowed_only_get_post_exception import MethodNotAllowedOnlyGetPostException
from postnlecommerce.http.auth.custom_header_authentication import CustomHeaderAuthenticationCredentials
from postnlecommerce.models.address_11 import Address11
from postnlecommerce.models.address_2 import Address2
from postnlecommerce.models.contact import Contact
from postnlecommerce.models.customer_1 import Customer1
from postnlecommerce.models.dimension import Dimension
from postnlecommerce.models.labelling_request import LabellingRequest
from postnlecommerce.models.message_1 import Message1
from postnlecommerce.models.shipment_1 import Shipment1
from postnlecommerce.postnlecommerce_client import PostnlecommerceClient

client = PostnlecommerceClient(
    custom_header_authentication_credentials=CustomHeaderAuthenticationCredentials(
        apikey='apikey'
    ),
    environment=Environment.PRODUCTION_SERVER
)

labelling_controller = client.labelling
body = LabellingRequest(
    customer=Customer1(
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
    message=Message1(
        message_id='1',
        message_time_stamp='08-09-2022 12:00:00',
        printertype='GraphicFile|PDF'
    ),
    shipments=[
        Shipment1(
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
    result = labelling_controller.generate_label(body)

    if result.is_success():
        print(result.body)
    elif result.is_error():
        print(result.errors)

except LabellingResponseInvalidException as e: 
    print(e)
except MethodNotAllowedOnlyGetPostException as e: 
    print(e)
except BarcodeResponseErrorException as e: 
    print(e)
except APIException as e: 
    print(e)

