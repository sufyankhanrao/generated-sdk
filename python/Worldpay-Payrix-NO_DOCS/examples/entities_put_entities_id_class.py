from payrix.configuration import Environment
from payrix.exceptions.api_exception import APIException
from payrix.exceptions.error_four_hundred_exception import ErrorFourHundredException
from payrix.http.auth.api_key import ApiKeyCredentials
from payrix.http.auth.session_key import SessionKeyCredentials
from payrix.http.auth.txn_session_key import TxnSessionKeyCredentials
from payrix.models.ein_type_enum import EinTypeEnum
from payrix.models.entities_public_enum import EntitiesPublicEnum
from payrix.models.entities_put_request import EntitiesPutRequest
from payrix.models.entity_country_enum import EntityCountryEnum
from payrix.models.entity_type_enum import EntityTypeEnum
from payrix.models.frozen_enum import FrozenEnum
from payrix.models.global_business_type_enum import GlobalBusinessTypeEnum
from payrix.models.inactive_enum import InactiveEnum
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

entities_controller = client.entities
id = 't1_ent_6733015a977c2cdd6277d89'

body = EntitiesPutRequest(
    client_ip='152.58.83.44',
    login='t1_log_6733015a79f48410904564b',
    mtype=EntityTypeEnum.GOV,
    name='Splash LLC',
    display_name='John',
    address_1='1234 Rivver Lane',
    address_2='San house Fremont',
    city='Frisco',
    state='TX',
    zip='75034',
    country=EntityCountryEnum.USA,
    timezone=TimezoneEnum.CST,
    phone='995685662566',
    customer_phone='995685662566',
    fax='995685662566',
    email='rawatankit0911@gmail.com',
    website='http://payrix.com',
    ein_type=EinTypeEnum.SSN,
    irs_filing_name='Integration Test 2025-02-21T09:12:15.332',
    ein='678912345',
    locations=1,
    public=EntitiesPublicEnum.PUBLICENTITY,
    tc_version='1.0',
    tc_accept_date='202204281403',
    tc_accept_ip='162.250.123.158',
    custom='voluptatibus et accusamus',
    payout_secondary_descriptor='Apex Leadership',
    industry='Residential Painting',
    global_business_type=GlobalBusinessTypeEnum.SSN,
    global_business_id='678912345',
    frozen=FrozenEnum.NOTFROZEN,
    inactive=InactiveEnum.ACTIVE
)

request_token = '20250423-yourmerchant-refunds-001'

try:
    result = entities_controller.put_entities_id(
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

