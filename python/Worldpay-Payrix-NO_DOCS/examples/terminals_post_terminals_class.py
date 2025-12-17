from payrix.configuration import Environment
from payrix.exceptions.api_exception import APIException
from payrix.exceptions.error_four_hundred_exception import ErrorFourHundredException
from payrix.http.auth.api_key import ApiKeyCredentials
from payrix.http.auth.session_key import SessionKeyCredentials
from payrix.http.auth.txn_session_key import TxnSessionKeyCredentials
from payrix.models.auto_close_enum import AutoCloseEnum
from payrix.models.capability_enum import CapabilityEnum
from payrix.models.cloud_enabled_enum import CloudEnabledEnum
from payrix.models.country_enum import CountryEnum
from payrix.models.terminal_environment_enum import TerminalEnvironmentEnum
from payrix.models.terminal_status_enum import TerminalStatusEnum
from payrix.models.terminal_type_enum import TerminalTypeEnum
from payrix.models.terminals_post_request import TerminalsPostRequest
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

terminals_controller = client.terminals
body = TerminalsPostRequest(
    merchant='t1_mer_67c127497499df129bfc68b',
    mtype=TerminalTypeEnum.PAXSP30CASIO,
    auto_close=AutoCloseEnum.ENUM_NONE,
    auto_close_time=2355,
    status=TerminalStatusEnum.ACTIVE,
    capability=CapabilityEnum.KEYED,
    environment=TerminalEnvironmentEnum.RETAIL,
    cloud_enabled=CloudEnabledEnum.CLOUDSERVICESDISABLED,
    serial='serial number',
    token='token',
    name='name of this terminal',
    description='description of the Terminal',
    address_1='first line of the address',
    address_2='second line of the address',
    city='city name',
    state='AB',
    zip='zip code',
    country=CountryEnum.CAN,
    phone='phone number',
    timezone=TimezoneEnum.EST
)

request_token = '20250423-yourmerchant-refunds-001'

try:
    result = terminals_controller.post_terminals(
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

