from fortisapi.configuration import Environment
from fortisapi.exceptions.api_exception import APIException
from fortisapi.exceptions.response_401_token_exception import Response401tokenException
from fortisapi.exceptions.response_412_exception import Response412Exception
from fortisapi.fortisapi_client import FortisapiClient
from fortisapi.http.auth.developer_id import DeveloperIdCredentials
from fortisapi.http.auth.user_api_key import UserApiKeyCredentials
from fortisapi.http.auth.user_id import UserIdCredentials
from fortisapi.models.iias_ind_enum import IiasIndEnum
from fortisapi.models.v_1_transactions_refund_request import V1TransactionsRefundRequest

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

transactions_updates_controller = client.transactions_updates
transaction_id = '11e95f8ec39de8fbdb0a4f1a'

body = V1TransactionsRefundRequest(
    transaction_amount=1,
    checkin_date='2021-12-01',
    checkout_date='2021-12-01',
    clerk_number='AE1234',
    contact_id='11e95f8ec39de8fbdb0a4f1a',
    custom_data={"data1":"custom1","data2":"custom2"},
    customer_id='customerid',
    description='some description',
    iias_ind=IiasIndEnum.ENUM_1,
    image_front='U29tZVN0cmluZ09idmlvdXNseU5vdEJhc2U2NEVuY29kZWQ=',
    image_back='U29tZVN0cmluZ09idmlvdXNseU5vdEJhc2U2NEVuY29kZWQ=',
    installment=True,
    installment_number=1,
    installment_count=1,
    location_api_id='location-api-id-florida-2',
    location_id='11e95f8ec39de8fbdb0a4f1a',
    product_transaction_id='11e95f8ec39de8fbdb0a4f1a',
    advance_deposit=False,
    no_show=False,
    notification_email_address='johnsmith@smiths.com',
    order_number='433659378839',
    po_number='555555553123',
    quick_invoice_id='11e95f8ec39de8fbdb0a4f1a',
    recurring=False,
    recurring_number=1,
    room_num='303',
    room_rate=95,
    save_account=False,
    save_account_title='John Account',
    subtotal_amount=599,
    surcharge_amount=100,
    tax=0,
    tip_amount=0,
    secondary_amount=0,
    transaction_api_id='transaction-payment-abcd123',
    transaction_c_1='custom-data-1',
    transaction_c_2='custom-data-2',
    transaction_c_3='custom-data-3',
    bank_funded_only_override=False,
    allow_partial_authorization_override=False,
    auto_decline_cvv_override=False,
    auto_decline_street_override=False,
    auto_decline_zip_override=False
)

try:
    result = transactions_updates_controller.refund_transaction(
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

