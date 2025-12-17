
from fortisapi.configuration import Environment
from fortisapi.exceptions.api_exception import APIException
from fortisapi.exceptions.response_401_token_exception import Response401tokenException
from fortisapi.exceptions.response_412_exception import Response412Exception
from fortisapi.fortisapi_client import FortisapiClient
from fortisapi.http.auth.developer_id import DeveloperIdCredentials
from fortisapi.http.auth.user_api_key import UserApiKeyCredentials
from fortisapi.http.auth.user_id import UserIdCredentials
from fortisapi.models.item_list_4 import ItemList4
from fortisapi.models.v_1_quick_invoices_request import V1QuickInvoicesRequest

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

quick_invoices_controller = client.quick_invoices
body = V1QuickInvoicesRequest(
    title='My terminal',
    due_date='2021-12-01',
    item_list=[
        ItemList4(
            name='Bread',
            amount=2015
        )
    ],
    location_id='11e95f8ec39de8fbdb0a4f1a',
    cc_product_transaction_id='11e95f8ec39de8fbdb0a4f1a',
    ach_product_transaction_id='11e95f8ec39de8fbdb0a4f1a',
    allow_overpayment=True,
    bank_funded_only_override=True,
    email='email@domain.com',
    contact_id='11e95f8ec39de8fbdb0a4f1a',
    contact_api_id='contact12345',
    quick_invoice_api_id='quickinvoice12345',
    customer_id='11e95f8ec39de8fbdb0a4f1a',
    expire_date='2021-12-01',
    allow_partial_pay=True,
    attach_files_to_email=True,
    send_email=True,
    invoice_number='invoice12345',
    item_header='Quick invoice header sample',
    item_footer='Thank you',
    amount_due=24536,
    notification_email='email@domain.com',
    status_id=1,
    status_code=1,
    note='some note',
    notification_days_before_due_date=3,
    notification_days_after_due_date=7,
    notification_on_due_date=True,
    send_text_to_pay=True,
    remaining_balance=24536,
    single_payment_min_amount=500,
    single_payment_max_amount=500000,
    cell_phone='3339998822'
)

try:
    result = quick_invoices_controller.create_a_new_quick_invoice(body)

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

