import jsonpickle
import logging

from goeapi.configuration import Environment
from goeapi.exceptions.api_exception import ApiException
from goeapi.exceptions.internal_server_message_general_exception import InternalServerMessageGeneralException
from goeapi.exceptions.message_exception import MessageException
from goeapi.goeapi_client import GoeapiClient
from goeapi.http.auth.oauth_2 import BearerAuthCredentials
from goeapi.logging.configuration.api_logging_configuration import LoggingConfiguration
from goeapi.logging.configuration.api_logging_configuration import RequestLoggingConfiguration
from goeapi.logging.configuration.api_logging_configuration import ResponseLoggingConfiguration
from goeapi.models.goal_profile_goe_for_taxes_attr import GoalProfileGoeForTaxesAttr
from goeapi.models.goe_for_taxes_input_model import GoeForTaxesInputModel
from goeapi.models.goe_to_account_attr import GoeToAccountAttr
from goeapi.models.goe_to_cashflow_details_2 import GoeToCashflowDetails2
from goeapi.models.goe_to_category import GoeToCategory
from goeapi.models.household_goe_for_taxes_obj_2 import HouseholdGoeForTaxesObj2
from goeapi.models.infusion_type_3 import InfusionType3
from goeapi.models.member_goe_for_taxes_obj import MemberGoeForTaxesObj
from goeapi.models.member_type import MemberType
from goeapi.models.reallocation_freq import ReallocationFreq
from goeapi.models.risk_profile_3 import RiskProfile3
from goeapi.models.tax_rates_dic_2 import TaxRatesDic2

client = GoeapiClient(
    bearer_auth_credentials=BearerAuthCredentials(
        access_token='AccessToken'
    ),
    environment=Environment.UAT,
    logging_configuration=LoggingConfiguration(
        log_level=logging.INFO,
        request_logging_config=RequestLoggingConfiguration(
            log_body=True
        ),
        response_logging_config=ResponseLoggingConfiguration(
            log_headers=True
        )
    )
)

goe_api = client.goe
body = GoeForTaxesInputModel(
    is_new_risk_profile=False,
    is_new_investment_tenure=False,
    is_new_goal_priority=False,
    is_new_goal=False,
    get_path=True,
    reallocation_freq=ReallocationFreq.YEARLY,
    current_portfolio_id=None,
    risk_profile=RiskProfile3.AGGRESSIVE,
    compute_social_security=False,
    use_social_security_for_goals=True,
    infusion_type=InfusionType3.YEARLY,
    cola_rate=0.03,
    tax_rates=TaxRatesDic2(
        ltcg_pre_retirement=0.15,
        ltcg_post_retirement=0.1,
        etr_pre_retirement=0.15,
        etr_post_retirement=0.2
    ),
    household=HouseholdGoeForTaxesObj2(
        household_id='1',
        member_list=[
            MemberGoeForTaxesObj(
                member_type=MemberType.PRIMARY,
                member_id='eff63fdb-1ed8-41be-a0f8-7788fdac728c',
                dob='02-1959',
                current_age=66,
                retirement_age=93,
                current_salary=400,
                social_security_start_age=65,
                existing_monthly_social_security_amount=10,
                additional_properties={
                    'lifeExpectancy': jsonpickle.decode('93')
                }
            )
        ],
        state_of_residence='KS'
    ),
    accounts=[
        GoeToAccountAttr(
            account_id='dbcd5e3d-55fb-45f6-a654-d720f056a071',
            account_type='IRA',
            taxability_type='D',
            member_i_ds=[
                'eff63fdb-1ed8-41be-a0f8-7788fdac728c'
            ],
            current_balance=2,
            current_holdings=[
                GoeToCategory(
                    category_name='CASH',
                    category_id='10',
                    category_price=1,
                    quantity=2,
                    cost_basis=2
                )
            ],
            cashflow_details=GoeToCashflowDetails2(
                start_date='02-05-2025',
                end_date='02-05-2051',
                cashflow_amt=[
                    2500,
                    2575,
                    2652,
                    2732,
                    2814,
                    2898,
                    2985,
                    3075,
                    3167,
                    3262,
                    3360,
                    3461,
                    3564,
                    3671,
                    3781,
                    3895,
                    4012,
                    4132,
                    4256,
                    4384,
                    4515,
                    4651,
                    4790,
                    4934,
                    5082,
                    5234,
                    5391
                ]
            ),
            additional_properties={
                'lockExpiry': jsonpickle.decode('0'),
                'meanReturn': jsonpickle.decode('0.03'),
                'standardDeviation': jsonpickle.decode('0.04')
            }
        )
    ],
    goal_profile_list=[
        GoalProfileGoeForTaxesAttr(
            goal_id='39623865346539642d366234362d343639362d393332332d356134356563653030336130',
            start_date='02-05-2052',
            end_date='02-05-2052',
            priority='Need',
            goal_purpose='non-education',
            goal_amt=[
                666
            ],
            scenario_type='retirement'
        )
    ],
    reallocate=False,
    is_near_term_volatility=False,
    curr_date='02-05-2025',
    cashflow_date='02-05-2025',
    loss_threshold=0,
    additional_properties={
        'targetPortfolio': jsonpickle.decode('{"meanReturn":0.03,"standardDeviation":0.04}')
    }
)

try:
    result = goe_api.goe_for_taxes(body)

    if result.is_success():
        print(result.body)
    elif result.is_error():
        print(result.errors)

except MessageException as e: 
    print(e)
except InternalServerMessageGeneralException as e: 
    print(e)
except ApiException as e: 
    print(e)

