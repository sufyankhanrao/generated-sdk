from payrix.configuration import Environment
from payrix.exceptions.api_exception import APIException
from payrix.exceptions.error_four_hundred_exception import ErrorFourHundredException
from payrix.http.auth.api_key import ApiKeyCredentials
from payrix.http.auth.session_key import SessionKeyCredentials
from payrix.http.auth.txn_session_key import TxnSessionKeyCredentials
from payrix.models.credential_integration_enum import CredentialIntegrationEnum
from payrix.models.credential_type_enum import CredentialTypeEnum
from payrix.models.credentials_post_request import CredentialsPostRequest
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

credentials_controller = client.credentials
body = CredentialsPostRequest(
    entity='t1_ent_67e152cfd598c814ed8f2e0',
    username='JDoe123',
    integration=CredentialIntegrationEnum.VANTIV,
    mtype=CredentialTypeEnum.TRANSACTION,
    inactive=InactiveEnum.ACTIVE,
    frozen=FrozenEnum.NOTFROZEN,
    name='name of Credential resource',
    description='description of Credential resource',
    password='password',
    connect_username='username connecting to integration',
    connect_password='password',
    secret='secret resource identifier'
)

request_token = '20250423-yourmerchant-refunds-001'

try:
    result = credentials_controller.post_credentials(
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

