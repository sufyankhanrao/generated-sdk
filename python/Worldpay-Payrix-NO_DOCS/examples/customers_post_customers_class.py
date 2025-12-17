from payrix.configuration import Environment
from payrix.exceptions.api_exception import APIException
from payrix.exceptions.error_four_hundred_exception import ErrorFourHundredException
from payrix.http.auth.api_key import ApiKeyCredentials
from payrix.http.auth.session_key import SessionKeyCredentials
from payrix.http.auth.txn_session_key import TxnSessionKeyCredentials
from payrix.models.country_enum import CountryEnum
from payrix.models.customers_post_request import CustomersPostRequest
from payrix.models.frozen_enum import FrozenEnum
from payrix.models.inactive_enum import InactiveEnum
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

customers_controller = client.customers
body = CustomersPostRequest(
    login='t1_log_0089616d2294ec86ba6076c',
    frozen=FrozenEnum.NOTFROZEN,
    inactive=InactiveEnum.ACTIVE,
    merchant='t1_mer_00415e924c58c616f8a119b',
    entity='t1_ent_64415e922e9000ef8bf3c1d',
    first='John',
    middle='M',
    last='Doe',
    company='Doe Enterprises',
    email='somename@emaol.com',
    shipping_first='John',
    shipping_middle='M',
    shipping_last='Doe',
    shipping_company='Doe Shipping Co.',
    shipping_address_1='123 Main st.',
    shipping_address_2='Apt 4B',
    shipping_city='Shelbyville',
    shipping_state='TX',
    shipping_zip='75001',
    shipping_country=ShippingCountryEnum.USA,
    shipping_phone='+11234567845',
    shipping_fax='+11234567845',
    custom='Customer\'s custom data',
    address_1='456 Secondary Ave',
    address_2='Apt 4B',
    city='Shelbyville',
    state='TX',
    zip='75001',
    country=CountryEnum.USA,
    phone='+11324567845',
    fax='+11234567845'
)

request_token = '20250423-yourmerchant-refunds-001'

try:
    result = customers_controller.post_customers(
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

