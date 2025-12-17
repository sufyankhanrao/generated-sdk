from fortisapi.configuration import Environment
from fortisapi.exceptions.api_exception import APIException
from fortisapi.exceptions.response_401_token_exception import Response401tokenException
from fortisapi.exceptions.response_412_exception import Response412Exception
from fortisapi.fortisapi_client import FortisapiClient
from fortisapi.http.auth.developer_id import DeveloperIdCredentials
from fortisapi.http.auth.user_api_key import UserApiKeyCredentials
from fortisapi.http.auth.user_id import UserIdCredentials
from fortisapi.models.debit_credit_enum import DebitCreditEnum
from fortisapi.models.level_3_data_5 import Level3Data5
from fortisapi.models.line_item_5 import LineItem5
from fortisapi.models.tax_exempt_enum import TaxExemptEnum
from fortisapi.models.v_1_transactions_level_3_master_card_request import V1TransactionsLevel3MasterCardRequest

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

body = V1TransactionsLevel3MasterCardRequest(
    level_3_data=Level3Data5(
        line_items=[
            LineItem5(
                description='cool drink',
                product_code='coke12345678',
                unit_code='gll',
                unit_cost=10,
                alternate_tax_id='1234',
                debit_credit=DebitCreditEnum.C,
                discount_amount=10,
                discount_rate=11,
                quantity=5,
                tax_amount=3,
                tax_rate=0,
                tax_type_applied='22',
                tax_type_id='11'
            )
        ],
        destination_country_code='840',
        duty_amount=0,
        freight_amount=0,
        national_tax=2,
        sales_tax=200,
        shipfrom_zip_code='AZ12345',
        shipto_zip_code='MI48335',
        tax_amount=0,
        tax_exempt=TaxExemptEnum.ENUM_0
    )
)

try:
    result = level_3_data_controller.create_a_new_level_3_entry_for_a_master_card(
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

