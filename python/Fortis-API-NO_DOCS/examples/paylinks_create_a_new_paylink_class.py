from fortisapi.configuration import Environment
from fortisapi.exceptions.api_exception import APIException
from fortisapi.exceptions.response_401_token_exception import Response401tokenException
from fortisapi.exceptions.response_412_exception import Response412Exception
from fortisapi.fortisapi_client import FortisapiClient
from fortisapi.http.auth.developer_id import DeveloperIdCredentials
from fortisapi.http.auth.user_api_key import UserApiKeyCredentials
from fortisapi.http.auth.user_id import UserIdCredentials
from fortisapi.models.delivery_method_enum import DeliveryMethodEnum
from fortisapi.models.v_1_paylinks_request import V1PaylinksRequest

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

paylinks_controller = client.paylinks
body = V1PaylinksRequest(
    amount_due=1,
    location_id='11e95f8ec39de8fbdb0a4f1a',
    cc_product_transaction_id='11e95f8ec39de8fbdb0a4f1a',
    email='email@domain.com',
    contact_id='11e95f8ec39de8fbdb0a4f1a',
    ach_product_transaction_id='11e95f8ec39de8fbdb0a4f1a',
    expire_date='2021-12-01',
    display_product_transaction_receipt_details=True,
    display_billing_fields=True,
    delivery_method=DeliveryMethodEnum.ENUM_0,
    cell_phone='3339998822',
    description='Description',
    store_token=False,
    store_token_title='John Account',
    bank_funded_only_override=False
)

try:
    result = paylinks_controller.create_a_new_paylink(body)

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

