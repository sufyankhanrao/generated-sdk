from shelldatareportingapis.configuration import Environment
from shelldatareportingapis.exceptions.api_exception import APIException
from shelldatareportingapis.exceptions.error_object_exception import ErrorObjectException
from shelldatareportingapis.http.auth.bearer_token import BearerTokenCredentials
from shelldatareportingapis.models.o_auth_token import OAuthToken
from shelldatareportingapis.models.recent_transaction_req import RecentTransactionReq
from shelldatareportingapis.models.recent_transaction_request import RecentTransactionRequest
from shelldatareportingapis.shell_data_reporting_ap_is_client import ShellDataReportingApIsClient

client = ShellDataReportingApIsClient(
    bearer_token_credentials=BearerTokenCredentials(
        o_auth_client_id='OAuthClientId',
        o_auth_client_secret='OAuthClientSecret',
        o_auth_token=OAuthToken(
            access_token='AccessToken',
            token_type='SandboxToken',
            expires_in=3600,
            refresh_token='RefreshToken'
        )
    ),
    environment=Environment.SIT
)

transaction_controller = client.transaction
request_id = '2b0cbe11-f109-4c43-9201-49af0370df1c'

body = RecentTransactionRequest(
    page_size=1,
    page=1,
    filters=RecentTransactionReq(
        col_co_code=14,
        payer_number='GB00001232',
        account_number='GB00001233',
        product_code='22',
        purchased_in_country='GB',
        card_pan='700205******890645',
        from_date_time='2020-11-09 13:56:03.000',
        to_date_time='2020-12-09 13:56:03.000',
        transaction_status='APPROVED',
        fuel_only='False',
        product_group_name='Motor gasoline',
        vehicle_registration_number='YG67OUM',
        include_declines=True,
        card_issuer_name='Mathew',
        column_list='PayerNumber,AccountNumber,ProductName,FuelVolume,PAN'
    )
)

try:
    result = transaction_controller.recent_transactions_new(
        request_id,
        body=body
    )

    if result.is_success():
        print(result.body)
    elif result.is_error():
        print(result.errors)

except ErrorObjectException as e: 
    print(e)
except APIException as e: 
    print(e)

