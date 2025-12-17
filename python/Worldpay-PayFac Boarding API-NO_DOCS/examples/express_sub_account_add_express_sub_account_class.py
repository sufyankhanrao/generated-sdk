from payfacsubmerchantprovisioningapi.configuration import Environment
from payfacsubmerchantprovisioningapi.exceptions.api_exception import APIException
from payfacsubmerchantprovisioningapi.exceptions.m_400_error_response_exception import M400ErrorResponseException
from payfacsubmerchantprovisioningapi.exceptions.m_401_error_response_exception import M401ErrorResponseException
from payfacsubmerchantprovisioningapi.exceptions.m_403_error_response_exception import M403ErrorResponseException
from payfacsubmerchantprovisioningapi.exceptions.m_404_error_response_exception import M404ErrorResponseException
from payfacsubmerchantprovisioningapi.exceptions.m_500_error_response_exception import M500ErrorResponseException
from payfacsubmerchantprovisioningapi.http.auth.custom_header_authentication import CustomHeaderAuthenticationCredentials
from payfacsubmerchantprovisioningapi.models.batch_close_method_enum import BatchCloseMethodEnum
from payfacsubmerchantprovisioningapi.models.check_for_duplicate_transactions_enum import CheckForDuplicateTransactionsEnum
from payfacsubmerchantprovisioningapi.models.enable_commercial_card_bin_query_enum import EnableCommercialCardBINQueryEnum
from payfacsubmerchantprovisioningapi.models.express_sub_account import ExpressSubAccount
from payfacsubmerchantprovisioningapi.payfacsubmerchantprovisioningapi_client import PayfacsubmerchantprovisioningapiClient

client = PayfacsubmerchantprovisioningapiClient(
    custom_header_authentication_credentials=CustomHeaderAuthenticationCredentials(
        authorization='Authorization'
    ),
    environment=Environment.PRODUCTION
)

express_sub_account_controller = client.express_sub_account
v_correlation_id = '0000139e-0000-0000-0000-000000000000'

id = 'id0'

body = ExpressSubAccount(
    express_gateway_id=123456,
    batch_close_method=BatchCloseMethodEnum.TIMEINITIATED,
    batch_close_time='20:00:00',
    check_for_duplicate_transactions=CheckForDuplicateTransactionsEnum.YES,
    enable_commercial_card_bin_query=EnableCommercialCardBINQueryEnum.NO
)

try:
    result = express_sub_account_controller.add_express_sub_account(
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
except M403ErrorResponseException as e: 
    print(e)
except M404ErrorResponseException as e: 
    print(e)
except M500ErrorResponseException as e: 
    print(e)
except APIException as e: 
    print(e)

