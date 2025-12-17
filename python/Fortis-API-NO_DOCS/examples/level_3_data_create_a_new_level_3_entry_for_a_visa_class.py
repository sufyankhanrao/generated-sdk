from fortisapi.configuration import Environment
from fortisapi.exceptions.api_exception import APIException
from fortisapi.exceptions.response_401_token_exception import Response401tokenException
from fortisapi.exceptions.response_412_exception import Response412Exception
from fortisapi.fortisapi_client import FortisapiClient
from fortisapi.http.auth.developer_id import DeveloperIdCredentials
from fortisapi.http.auth.user_api_key import UserApiKeyCredentials
from fortisapi.http.auth.user_id import UserIdCredentials
from fortisapi.models.level_3_data_6 import Level3Data6
from fortisapi.models.line_item_6 import LineItem6
from fortisapi.models.tax_exempt_enum import TaxExemptEnum
from fortisapi.models.v_1_transactions_level_3_visa_request import V1TransactionsLevel3VisaRequest

client = FortisapiClient(
    user_id_credentials=UserIdCredentials(
        user_id='user-id'
    ),
    user_api_key_credentials=UserApiKeyCredentials(
        user_api_key='user-api-key'
    ),
    developer_id_credentials=DeveloperIdCredentials(
        developer_id='developer-id'
    ),
    environment=Environment.SANDBOX
)

level_3_data_controller = client.level_3_data
transaction_id = '11e95f8ec39de8fbdb0a4f1a'

body = V1TransactionsLevel3VisaRequest(
    level_3_data=Level3Data6(
        line_items=[
            LineItem6(
                description='cool drink',
                commodity_code='cc123456',
                product_code='fanta123456',
                unit_code='gll',
                unit_cost=3,
                discount_amount=0,
                other_tax_amount=0,
                quantity=12,
                tax_amount=4,
                tax_rate=0
            )
        ],
        destination_country_code='840',
        duty_amount=0,
        freight_amount=0,
        national_tax=2,
        sales_tax=200,
        shipfrom_zip_code='AZ1234',
        shipto_zip_code='FL1234',
        tax_amount=10,
        tax_exempt=TaxExemptEnum.ENUM_0,
        customer_vat_registration='12345678',
        merchant_vat_registration='123456',
        order_date='171006',
        summary_commodity_code='C1K2',
        tax_rate=0,
        unique_vat_ref_number='vat1234'
    )
)

try:
    result = level_3_data_controller.create_a_new_level_3_entry_for_a_visa(
        transaction_id,
        body
    )

    if result.is_success():
        print(result.body)
    elif result.is_error():
        print(result.errors)

except Response401tokenException as e: 
    print(e)
except Response412Exception as e: 
    print(e)
except APIException as e: 
    print(e)

