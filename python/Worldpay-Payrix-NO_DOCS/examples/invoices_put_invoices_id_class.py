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
from payrix.models.invoices_put_request import InvoicesPutRequest
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
id = 't1_inv_00b3a1f7e418cd6e378d410'

body = InvoicesPutRequest(
    login='t1_log_0092b50e1112b18e41d521e',
    merchant='t1_mer_008e7f511d5c5a2d2fade82',
    customer='t1_cus_00b39e97b2110ba9075dfda',
    subscription='t1_sbn_00fc6fxx7a871bbce685897',
    allowed_payment_methods='visa',
    title='Test Invoice Alert',
    message='Testing the invoice alerts',
    total=100,
    tax=1000,
    discount=1000,
    due_date=20250217,
    expiration_date=20250217,
    send_on=20250217,
    status=InvoiceStatusEnum.PAID,
    email_status=EmailStatusEnum.PENDING,
    emails='erik@test.com',
    mtype=InvoiceTypeEnum.ONEOFF,
    inactive=InactiveEnum.ACTIVE,
    frozen=FrozenEnum.NOTFROZEN
)

request_token = '20250423-yourmerchant-refunds-001'

try:
    result = invoices_controller.put_invoices_id(
        id,
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

