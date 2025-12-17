from payrix.configuration import Environment
from payrix.exceptions.api_exception import APIException
from payrix.exceptions.error_four_hundred_exception import ErrorFourHundredException
from payrix.http.auth.api_key import ApiKeyCredentials
from payrix.http.auth.session_key import SessionKeyCredentials
from payrix.http.auth.txn_session_key import TxnSessionKeyCredentials
from payrix.models.invoice_result_post_request import InvoiceResultPostRequest
from payrix.models.invoice_result_status_enum import InvoiceResultStatusEnum
from payrix.models.shipping_country_enum import ShippingCountryEnum
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

invoice_results_controller = client.invoice_results
body = InvoiceResultPostRequest(
    invoice='t1_inv_00b62cb82db90057aae4157',
    txn='p1_txn_67b7c41d9d166b99ac02b36',
    status=InvoiceResultStatusEnum.SUCCESS,
    message='Invoice Paid',
    shipping_first='John',
    shipping_middle='M',
    shipping_last='Doe',
    shipping_company='Doe Shippin Co.',
    shipping_address_1='123 Mai st.',
    shipping_address_2='Suite 10',
    shipping_city='Springfield',
    shipping_state='TX',
    shipping_zip='62701',
    shipping_country=ShippingCountryEnum.USA,
    shipping_phone='+1123456784',
    shipping_fax='+1123456784',
    authorization='Test Authorization with a field name = :field: and a replace text = :replace:',
    authorization_data='{"field":"field", "replace":"replace"}',
    signature='/9j/4AAQSkZJRgABAQAAAQABAAD/2wBDAAYEBQYFBAYGBQYHBwYIChAKCgkJChQODwwQFxQYGBcUFhYaHSUfGhsjHBYWICwgIyYnKSop'
)

request_token = '20250423-yourmerchant-refunds-001'

try:
    result = invoice_results_controller.post_invoice_results(
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

