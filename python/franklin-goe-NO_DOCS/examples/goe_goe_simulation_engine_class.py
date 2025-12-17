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
from goeapi.models.account import Account
from goeapi.models.cashflow_details_2 import CashflowDetails2
from goeapi.models.category import Category
from goeapi.models.goal_profile_simulation_engine import GoalProfileSimulationEngine
from goeapi.models.goe_simulation_engine_input_model import GoeSimulationEngineInputModel
from goeapi.models.household_2 import Household2
from goeapi.models.infusion_type_3 import InfusionType3
from goeapi.models.member import Member
from goeapi.models.member_type_1 import MemberType1
from goeapi.models.reallocation_freq import ReallocationFreq
from goeapi.models.risk_profile_4 import RiskProfile4
from goeapi.models.tax_rates_2 import TaxRates2

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
body = GoeSimulationEngineInputModel(
    reallocation_freq=ReallocationFreq.YEARLY,
    current_portfolio_id=None,
    risk_profile=RiskProfile4.AGGRESSIVE,
    compute_social_security=True,
    use_social_security_for_goals=True,
    is_new_risk_profile=True,
    infusion_type=InfusionType3.YEARLY,
    cola_rate=0.02,
    tax_rates=TaxRates2(
        ltcg_pre_retirement=0.15,
        ltcg_post_retirement=0.15,
        etr_pre_retirement=0.15,
        etr_post_retirement=0.15
    ),
    household=Household2(
        household_id='house_1',
        member_list=[
            Member(
                member_type=MemberType1.PRIMARY,
                member_id='1234',
                dob='12-1968',
                current_age=55,
                retirement_age=65,
                current_salary=50000,
                social_security_start_age=62,
                existing_monthly_social_security_amount=1000,
                tda_balance_for_rmd=10000,
                rmd_utilized=2000
            )
        ],
        state_of_residence='CA'
    ),
    accounts=[
        Account(
            account_id='5',
            account_type='401k',
            taxability_type='T',
            member_i_ds=[
                'memberIDs0'
            ],
            current_balance=14589,
            current_holdings=[
                Category(
                    category_name='CASH',
                    category_id='10',
                    category_price=1,
                    quantity=200000,
                    cost_basis=14589
                )
            ],
            cashflow_details=CashflowDetails2(
                start_date='01-03-2024',
                end_date='01-11-2032',
                cashflow_amt=[
                    2500,
                    2575
                ]
            )
        )
    ],
    goal_profile_list=[
        GoalProfileSimulationEngine(
            goal_id='Goal1',
            start_date='01-12-2059',
            end_date='01-12-2067',
            priority='Need',
            goal_purpose='Non-education',
            goal_amt=[
                2215916.68281757,
                2282394.1833021,
                2350866.00880116,
                2421391.9890652,
                2494033.74873716,
                2568854.76119927,
                2645920.40403525,
                2725298.01615631,
                2807056.95664099,
                2891268.66534022
            ],
            scenario_type='retirement',
            additional_properties={
                'bequest': jsonpickle.decode('false')
            }
        ),
        GoalProfileSimulationEngine(
            goal_id='Goal2',
            start_date='01-01-2023',
            end_date='01-01-2025',
            priority='Want',
            goal_purpose='Non-education',
            goal_amt=[
                10600
            ],
            scenario_type='regular',
            additional_properties={
                'bequest': jsonpickle.decode('false')
            }
        ),
        GoalProfileSimulationEngine(
            goal_id='Goal3',
            start_date='01-01-2023',
            end_date='01-01-2028',
            priority='Want',
            goal_purpose='Non-education',
            goal_amt=[
                31907.039
            ],
            scenario_type='regular',
            additional_properties={
                'bequest': jsonpickle.decode('false')
            }
        ),
        GoalProfileSimulationEngine(
            goal_id='Goal4',
            start_date='01-01-2023',
            end_date='02-04-2025',
            priority='Dream',
            goal_purpose='Non-education',
            goal_amt=[
                5061.361
            ],
            scenario_type='regular',
            additional_properties={
                'bequest': jsonpickle.decode('false')
            }
        ),
        GoalProfileSimulationEngine(
            goal_id='Goal5',
            start_date='01-01-2023',
            end_date='02-01-2048',
            priority='Dream',
            goal_purpose='Non-education',
            goal_amt=[
                407057.448
            ],
            scenario_type='regular',
            additional_properties={
                'bequest': jsonpickle.decode('false')
            }
        ),
        GoalProfileSimulationEngine(
            goal_id='Goal6',
            start_date='01-01-2023',
            end_date='06-02-2024',
            priority='Want',
            goal_purpose='Non-education',
            goal_amt=[
                5024.45469099256
            ],
            scenario_type='regular',
            additional_properties={
                'bequest': jsonpickle.decode('false')
            }
        )
    ],
    reallocate=False,
    is_new_goal_priority=False,
    curr_date='01-01-2023',
    cashflow_date='01-01-2023;',
    is_new_investment_tenure=False,
    is_new_goal=False
)

try:
    result = goe_api.goe_simulation_engine(body)

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

