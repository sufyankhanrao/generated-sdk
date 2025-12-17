
from payrix.configuration import Environment
from payrix.exceptions.api_exception import APIException
from payrix.exceptions.error_four_hundred_exception import ErrorFourHundredException
from payrix.http.auth.api_key import ApiKeyCredentials
from payrix.http.auth.session_key import SessionKeyCredentials
from payrix.http.auth.txn_session_key import TxnSessionKeyCredentials
from payrix.models.citizenship_enum import CitizenshipEnum
from payrix.models.country_enum import CountryEnum
from payrix.models.frozen_enum import FrozenEnum
from payrix.models.gender_enum import GenderEnum
from payrix.models.inactive_enum import InactiveEnum
from payrix.models.mailing_country_enum import MailingCountryEnum
from payrix.models.members_post_request import MembersPostRequest
from payrix.models.members_primary_enum import MembersPrimaryEnum
from payrix.models.politically_exposed_enum import PoliticallyExposedEnum
from payrix.models.significant_responsibility_enum import SignificantResponsibilityEnum
from payrix.models.timezone_enum import TimezoneEnum
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

members_controller = client.members
body = MembersPostRequest(
    merchant='t1_mer_67d033698c234e74c399ddd',
    first='Chad',
    last='Foster',
    dob=20160120,
    email='Jerrod_Glover@hotmail.com',
    ownership=10000,
    primary=MembersPrimaryEnum.PRIMARYCONTACT,
    significant_responsibility=SignificantResponsibilityEnum.NOSIGNIFICANTRESPONSIBILITY,
    politically_exposed=PoliticallyExposedEnum.NOTPOLITICALLYEXPOSED,
    timezone=TimezoneEnum.EST,
    inactive=InactiveEnum.ACTIVE,
    frozen=FrozenEnum.NOTFROZEN,
    title='CEO',
    middle='middle name',
    ssn='1924',
    citizenship=CitizenshipEnum.MAR,
    gender=GenderEnum.MALE,
    dl='6679',
    dlstate='MD',
    credit_score=334,
    credit_score_date='2025-03-11 08:58:20',
    mailing_address_1='mailing first line of address',
    mailing_address_2='mailing second line of address',
    mailing_city='mailing name of the city',
    mailing_state='MD',
    mailing_country=MailingCountryEnum.MAR,
    mailing_postal_code='mailing postal code',
    address_1='first line of address',
    address_2='second line of address',
    city='name of city',
    state='MD',
    zip='ZIP code',
    country=CountryEnum.MAR,
    phone='5106406000',
    fax='5106406000'
)

request_token = '20250423-yourmerchant-refunds-001'

try:
    result = members_controller.post_members(
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

