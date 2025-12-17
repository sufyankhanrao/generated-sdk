from payrix.configuration import Environment
from payrix.exceptions.api_exception import APIException
from payrix.exceptions.error_four_hundred_exception import ErrorFourHundredException
from payrix.http.auth.api_key import ApiKeyCredentials
from payrix.http.auth.session_key import SessionKeyCredentials
from payrix.http.auth.txn_session_key import TxnSessionKeyCredentials
from payrix.models.contacts_post_request import ContactsPostRequest
from payrix.models.country_enum import CountryEnum
from payrix.models.frozen_enum import FrozenEnum
from payrix.models.inactive_enum import InactiveEnum
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

contacts_controller = client.contacts
body = ContactsPostRequest(
    entity='t1_ent_665e13ff8b2e613134b9273',
    first='first name',
    last='last name',
    email='fewafehwuohfewafewafewa@payrjfhuiweafewa.com',
    frozen=FrozenEnum.NOTFROZEN,
    inactive=InactiveEnum.ACTIVE,
    middle='middle name',
    description='description of Contact',
    address_1='first line of the address',
    address_2='second line of the address',
    city='Anchorage',
    state='AK',
    zip='99501',
    country=CountryEnum.USA,
    phone='1234567890',
    fax='1234567890'
)

request_token = '20250423-yourmerchant-refunds-001'

try:
    result = contacts_controller.post_contacts(
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

