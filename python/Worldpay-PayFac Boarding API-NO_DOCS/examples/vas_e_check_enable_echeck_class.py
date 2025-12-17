
from payfacsubmerchantprovisioningapi.configuration import Environment
from payfacsubmerchantprovisioningapi.exceptions.api_exception import APIException
from payfacsubmerchantprovisioningapi.exceptions.m_400_error_response_exception import M400ErrorResponseException
from payfacsubmerchantprovisioningapi.exceptions.m_401_error_response_exception import M401ErrorResponseException
from payfacsubmerchantprovisioningapi.exceptions.m_403_error_response_format_exception import M403ErrorResponseFormatException
from payfacsubmerchantprovisioningapi.exceptions.m_404_error_response_exception import M404ErrorResponseException
from payfacsubmerchantprovisioningapi.exceptions.m_412_error_response_exception import M412ErrorResponseException
from payfacsubmerchantprovisioningapi.exceptions.m_500_error_response_exception import M500ErrorResponseException
from payfacsubmerchantprovisioningapi.http.auth.custom_header_authentication import CustomHeaderAuthenticationCredentials
from payfacsubmerchantprovisioningapi.models.echeck import Echeck
from payfacsubmerchantprovisioningapi.models.echeck_transaction_thresholds import EcheckTransactionThresholds
from payfacsubmerchantprovisioningapi.models.echeck_transaction_thresholds_per_customer import EcheckTransactionThresholdsPerCustomer
from payfacsubmerchantprovisioningapi.payfacsubmerchantprovisioningapi_client import PayfacsubmerchantprovisioningapiClient

client = PayfacsubmerchantprovisioningapiClient(
    custom_header_authentication_credentials=CustomHeaderAuthenticationCredentials(
        authorization='Authorization'
    ),
    environment=Environment.PRODUCTION
)

vas_e_check_controller = client.vas_e_check
v_correlation_id = '0000139e-0000-0000-0000-000000000000'

id = 'id0'

body = Echeck(
    enable_echeck=False,
    transaction_thresholds=EcheckTransactionThresholds(
        single_transaction_amount=156,
        daily_transaction_count=110,
        daily_transaction_amount=16,
        monthly_transaction_count=58,
        monthly_transaction_amount=224,
        per_customer=EcheckTransactionThresholdsPerCustomer(
            daily_transaction_count=132,
            daily_transaction_amount=6,
            daily_transaction_decline_count=248
        )
    )
)

try:
    result = vas_e_check_controller.enable_echeck(
        v_correlation_id,
        id,
        body
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
except M412ErrorResponseException as e: 
    print(e)
except M500ErrorResponseException as e: 
    print(e)
except APIException as e: 
    print(e)

