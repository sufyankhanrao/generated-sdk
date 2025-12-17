from payrix.configuration import Environment
from payrix.exceptions.api_exception import APIException
from payrix.exceptions.error_four_hundred_exception import ErrorFourHundredException
from payrix.http.auth.api_key import ApiKeyCredentials
from payrix.http.auth.session_key import SessionKeyCredentials
from payrix.http.auth.txn_session_key import TxnSessionKeyCredentials
from payrix.models.contacts_put_request import ContactsPutRequest
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
id = 't1_con_665f696f0d66c3281d00000'

body = ContactsPutRequest(
    entity='t1_ent_665e13ff8b2e613134b9273',
    first='first name',
    middle='middle name',
    last='last name',
    description='description of Contact',
    email='fewafehwuohfewafewafewa@payrjfhuiweafewa.com',
    address_1='first line of the address',
    address_2='second line of the address',
    city='Anchorage',
    state='AK',
    zip='99501',
    country=CountryEnum.USA,
    phone='1234567890',
    fax='1234567890',
    frozen=FrozenEnum.NOTFROZEN,
    inactive=InactiveEnum.ACTIVE
)

request_token = '20250423-yourmerchant-refunds-001'

try:
    result = contacts_controller.put_contacts_id(
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

