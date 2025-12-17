from verizon.configuration import Environment
from verizon.exceptions.api_exception import APIException
from verizon.exceptions.security_result_exception import SecurityResultException
from verizon.http.auth.thingspace_oauth import ThingspaceOauthCredentials
from verizon.http.auth.vz_m2m_token import VZM2mTokenCredentials
from verizon.models.assign_license_request import AssignLicenseRequest
from verizon.models.license_device_id import LicenseDeviceId
from verizon.models.license_device_list import LicenseDeviceList
from verizon.models.oauth_scope_thingspace_oauth_enum import OauthScopeThingspaceOauthEnum
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

sim_secure_for_io_t_licenses_controller = client.sim_secure_for_io_t_licenses
body = AssignLicenseRequest(
    account_name='0000123456-00001',
    devices=[
        LicenseDeviceList(
            device_ids=[
                LicenseDeviceId(
                    id='864508030109877',
                    kind='IMEI'
                )
            ]
        )
    ],
    sku_number='SIMSec-IoT-Lt'
)

try:
    result = sim_secure_for_io_t_licenses_controller.assign_license_to_devices(body)

    if result.is_success():
        print(result.body)
    elif result.is_error():
        print(result.errors)

except SecurityResultException as e: 
    print(e)
except APIException as e: 
    print(e)

