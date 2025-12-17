from verizon.configuration import Environment
from verizon.exceptions.api_exception import APIException
from verizon.exceptions.device_diagnostics_result_exception import DeviceDiagnosticsResultException
from verizon.http.auth.thingspace_oauth import ThingspaceOauthCredentials
from verizon.http.auth.vz_m2m_token import VZM2mTokenCredentials
from verizon.models.attribute_identifier_enum import AttributeIdentifierEnum
from verizon.models.device import Device
from verizon.models.numerical_data import NumericalData
from verizon.models.numerical_data_unit_enum import NumericalDataUnitEnum
from verizon.models.oauth_scope_thingspace_oauth_enum import OauthScopeThingspaceOauthEnum
from verizon.models.observation_request import ObservationRequest
from verizon.models.observation_request_attribute import ObservationRequestAttribute
from verizon.verizon_client import VerizonClient

client = VerizonClient(
    thingspace_oauth_credentials=ThingspaceOauthCredentials(
        oauth_client_id='OAuthClientId',
        oauth_client_secret='OAuthClientSecret',
        oauth_scopes=[
            OauthScopeThingspaceOauthEnum.DISCOVERYREAD,
            OauthScopeThingspaceOauthEnum.SERVICEPROFILEREAD
        ]
    ),
    vz_m2m_token_credentials=VZM2mTokenCredentials(
        vz_m2m_token='VZ-M2M-Token'
    ),
    environment=Environment.PRODUCTION
)

diagnostics_observations_controller = client.diagnostics_observations
body = ObservationRequest(
    account_name='TestQAAccount',
    devices=[
        Device(
            id='864508030026238',
            kind='IMEI'
        )
    ],
    attributes=[
        ObservationRequestAttribute(
            name=AttributeIdentifierEnum.RADIO_SIGNAL_STRENGTH
        ),
        ObservationRequestAttribute(
            name=AttributeIdentifierEnum.LINK_QUALITY
        ),
        ObservationRequestAttribute(
            name=AttributeIdentifierEnum.NETWORK_BEARER
        ),
        ObservationRequestAttribute(
            name=AttributeIdentifierEnum.CELL_ID
        )
    ],
    frequency=NumericalData(
        value=15,
        unit=NumericalDataUnitEnum.SECOND
    ),
    duration=NumericalData(
        value=15,
        unit=NumericalDataUnitEnum.SECOND
    )
)

try:
    result = diagnostics_observations_controller.start_diagnostics_observation(body)

    if result.is_success():
        print(result.body)
    elif result.is_error():
        print(result.errors)

except DeviceDiagnosticsResultException as e: 
    print(e)
except APIException as e: 
    print(e)

