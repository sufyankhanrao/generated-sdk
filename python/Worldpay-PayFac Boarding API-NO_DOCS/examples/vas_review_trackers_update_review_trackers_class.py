from payfacsubmerchantprovisioningapi.configuration import Environment
from payfacsubmerchantprovisioningapi.exceptions.api_exception import APIException
from payfacsubmerchantprovisioningapi.exceptions.m_400_error_response_exception import M400ErrorResponseException
from payfacsubmerchantprovisioningapi.exceptions.m_401_error_response_exception import M401ErrorResponseException
from payfacsubmerchantprovisioningapi.exceptions.m_403_error_response_format_exception import M403ErrorResponseFormatException
from payfacsubmerchantprovisioningapi.exceptions.m_404_error_response_exception import M404ErrorResponseException
from payfacsubmerchantprovisioningapi.exceptions.m_500_error_response_exception import M500ErrorResponseException
from payfacsubmerchantprovisioningapi.http.auth.custom_header_authentication import CustomHeaderAuthenticationCredentials
from payfacsubmerchantprovisioningapi.models.review_trackersfor_update import ReviewTrackersforUpdate
from payfacsubmerchantprovisioningapi.payfacsubmerchantprovisioningapi_client import PayfacsubmerchantprovisioningapiClient

client = PayfacsubmerchantprovisioningapiClient(
    custom_header_authentication_credentials=CustomHeaderAuthenticationCredentials(
        authorization='Authorization'
    ),
    environment=Environment.PRODUCTION
)

vas_review_trackers_controller = client.vas_review_trackers
v_correlation_id = '0000139e-0000-0000-0000-000000000000'

id = 'id0'

body = ReviewTrackersforUpdate(
    opt_out_date='2006-12-22'
)

try:
    result = vas_review_trackers_controller.update_review_trackers(
        v_correlation_id,
        id,
        body=body
    )

    if result.is_success():
        print(result.body)
    elif result.is_error():
        print(result.errors)

except M400ErrorResponseException as e: 
    print(e)
except M401ErrorResponseException as e: 
    print(e)
except M403ErrorResponseFormatException as e: 
    print(e)
except M404ErrorResponseException as e: 
    print(e)
except M500ErrorResponseException as e: 
    print(e)
except APIException as e: 
    print(e)

