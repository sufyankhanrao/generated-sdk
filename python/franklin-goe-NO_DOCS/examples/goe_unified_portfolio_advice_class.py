import jsonpickle
import logging

from goeapi.configuration import Environment
from goeapi.exceptions.api_exception import ApiException
from goeapi.exceptions.internal_server_message_exception import InternalServerMessageException
from goeapi.exceptions.message_exception import MessageException
from goeapi.exceptions.validation_message_one_exception import ValidationMessageOneException
from goeapi.goeapi_client import GoeapiClient
from goeapi.http.auth.oauth_2 import BearerAuthCredentials
from goeapi.logging.configuration.api_logging_configuration import LoggingConfiguration
from goeapi.logging.configuration.api_logging_configuration import RequestLoggingConfiguration
from goeapi.logging.configuration.api_logging_configuration import ResponseLoggingConfiguration
from goeapi.models.goal_profile import GoalProfile
from goeapi.models.reallocation_freq_5 import ReallocationFreq5
from goeapi.models.risk_profile_7 import RiskProfile7
from goeapi.models.unified_portfolio_advice_input_model_v_4 import UnifiedPortfolioAdviceInputModelV4

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
body = UnifiedPortfolioAdviceInputModelV4(
    is_new_goal_priority=True,
    is_new_risk_profile=True,
    is_new_investment_tenure=True,
    is_new_goal=True,
    get_path=True,
    reallocation_freq=ReallocationFreq5.YEARLY,
    initial_investment=86000,
    current_wealth=None,
    current_portfolio_id=None,
    infusions=[
        0,
        4000,
        4000,
        4000,
        4000,
        4000,
        4000,
        4000,
        4000,
        4000,
        -21000,
        -19000,
        -75000,
        -23000,
        -23000,
        -23000
    ],
    risk_profile=RiskProfile7.AGGRESSIVE,
    infusion_type='yearly',
    goal_profile_list=[
        GoalProfile(
            goal_id='Goal1',
            goal_amt=[
                25000
            ],
            start_date='01-01-2021',
            end_date='01-01-2031',
            priority='Need',
            scenario_type='regular'
        ),
        GoalProfile(
            goal_id='Goal2',
            goal_amt=[
                52000
            ],
            start_date='01-01-2021',
            end_date='01-01-2033',
            priority='Need',
            scenario_type='regular'
        ),
        GoalProfile(
            goal_id='Goal3',
            goal_amt=[
                2000,
                2000,
                2000,
                2000,
                2000,
                2000,
                2000,
                2000,
                2000,
                2000,
                2000,
                2000,
                2000,
                2000,
                2000
            ],
            start_date='01-01-2022',
            end_date='01-01-2036',
            priority='Need',
            scenario_type='retirement'
        ),
        GoalProfile(
            goal_id='Goal4',
            goal_amt=[
                21000,
                21000,
                21000,
                21000,
                21000
            ],
            start_date='01-01-2032',
            end_date='01-01-2036',
            priority='Need',
            scenario_type='retirement'
        )
    ],
    is_near_term_volatility=False,
    cashflow_date='01-01-2021',
    curr_date='04-01-2021',
    additional_properties={
        'calibrateGoalRec': jsonpickle.decode('true')
    }
)

try:
    result = goe_api.unified_portfolio_advice(body)

    if result.is_success():
        print(result.body)
    elif result.is_error():
        print(result.errors)

except ValidationMessageOneException as e: 
    print(e)
except MessageException as e: 
    print(e)
except InternalServerMessageException as e: 
    print(e)
except ApiException as e: 
    print(e)

