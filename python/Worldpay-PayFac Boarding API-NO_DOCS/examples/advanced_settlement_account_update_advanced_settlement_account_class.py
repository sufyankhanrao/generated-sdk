from payfacsubmerchantprovisioningapi.configuration import Environment
from payfacsubmerchantprovisioningapi.exceptions.api_exception import APIException
from payfacsubmerchantprovisioningapi.exceptions.m_400_error_response_exception import M400ErrorResponseException
from payfacsubmerchantprovisioningapi.exceptions.m_401_error_response_exception import M401ErrorResponseException
from payfacsubmerchantprovisioningapi.exceptions.m_403_error_response_exception import M403ErrorResponseException
from payfacsubmerchantprovisioningapi.exceptions.m_404_error_response_exception import M404ErrorResponseException
from payfacsubmerchantprovisioningapi.exceptions.m_500_error_response_exception import M500ErrorResponseException
from payfacsubmerchantprovisioningapi.models.advanced_settlement_account import AdvancedSettlementAccount
from payfacsubmerchantprovisioningapi.models.bank_account import BankAccount
from payfacsubmerchantprovisioningapi.models.dda_type_enum import DdaTypeEnum
from payfacsubmerchantprovisioningapi.models.one_ach_for_all_categories_enum import OneACHForAllCategoriesEnum
from payfacsubmerchantprovisioningapi.models.one_ach_for_credit_and_debit_enum import OneACHForCreditAndDebitEnum
from payfacsubmerchantprovisioningapi.models.settlement_category_enum import SettlementCategoryEnum
from payfacsubmerchantprovisioningapi.payfacsubmerchantprovisioningapi_client import PayfacsubmerchantprovisioningapiClient

client = PayfacsubmerchantprovisioningapiClient(
    environment=Environment.PRODUCTION
)

advanced_settlement_account_controller = client.advanced_settlement_account
v_correlation_id = '0000139e-0000-0000-0000-000000000000'

account_number = 'accountNumber2'

id = 'id0'

body = AdvancedSettlementAccount(
    bank_account=BankAccount(
        dda_type=DdaTypeEnum.CHECKING,
        account_number='12345678910',
        routing_number='123456789'
    ),
    settlement_categories=[
        SettlementCategoryEnum.DEBITDEPOSITS,
        SettlementCategoryEnum.CREDITCONVENIENCEFEES
    ],
    one_ach_for_all_categories=OneACHForAllCategoriesEnum.NO,
    one_ach_for_credit_and_debit=OneACHForCreditAndDebitEnum.NO
)

try:
    result = advanced_settlement_account_controller.update_advanced_settlement_account(
        v_correlation_id,
        account_number,
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

