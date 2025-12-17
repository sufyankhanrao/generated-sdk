from payrix.configuration import Environment
from payrix.exceptions.api_exception import APIException
from payrix.exceptions.error_four_hundred_exception import ErrorFourHundredException
from payrix.http.auth.api_key import ApiKeyCredentials
from payrix.http.auth.session_key import SessionKeyCredentials
from payrix.http.auth.txn_session_key import TxnSessionKeyCredentials
from payrix.models.email_status_enum import EmailStatusEnum
from payrix.models.frozen_enum import FrozenEnum
from payrix.models.inactive_enum import InactiveEnum
from payrix.models.invoice_status_enum import InvoiceStatusEnum
from payrix.models.invoice_type_enum import InvoiceTypeEnum
from payrix.models.invoices_post_request import InvoicesPostRequest
from payrix.payrix_client import PayrixClient

client = PayrixClient(
    api_key_credentials=ApiKeyCredentials(
        apikey='APIKEY'
    ),
    session_key_credentials=SessionKeyCredentials(
        sessionkey='SESSIONKEY'
    ),
    txn_session_key_credentials=TxnSessionKeyCredentials(
        txnsessionkey='TXNSESSIONKEY'
    ),
    environment=Environment.QA
)

invoices_controller = client.invoices
body = InvoicesPostRequest(
    login='t1_log_0092b50e1112b18e41d521e',
    merchant='t1_mer_008e7f511d5c5a2d2fade82',
    subscription='t1_sbn_00fc6fxx7a871bbce685897',
    number='9999888888',
    status=InvoiceStatusEnum.PAID,
    email_status=EmailStatusEnum.PENDING,
    mtype=InvoiceTypeEnum.ONEOFF,
    frozen=FrozenEnum.NOTFROZEN,
    inactive=InactiveEnum.ACTIVE,
    customer='t1_cus_00b39e97b2110ba9075dfda',
    allowed_payment_methods='visa',
    title='Test Invoice Alert',
    message='Testing invoice alerts',
    total=100,
    tax=1000,
    discount=1000,
    due_date=20250217,
    expiration_date=20250217,
    send_on=20250217,
    emails='erik@test.com'
)

request_token = '20250423-yourmerchant-refunds-001'

try:
    result = invoices_controller.post_invoices(
        body,
        request_token=request_token
    )

    if result.is_success():
        print(result.body)
    elif result.is_error():
        print(result.errors)

except ErrorFourHundredException as e: 
    print(e)
except APIException as e: 
    print(e)

