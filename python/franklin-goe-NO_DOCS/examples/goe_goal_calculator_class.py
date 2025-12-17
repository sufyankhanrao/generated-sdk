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
from goeapi.models.goal_calculator_goal_priority_attribute import GoalCalculatorGoalPriorityAttribute
from goeapi.models.goal_calculator_input_model import GoalCalculatorInputModel
from goeapi.models.infusion_type import InfusionType
from goeapi.models.reallocation_freq import ReallocationFreq
from goeapi.models.risk_profile import RiskProfile
from goeapi.models.scenario_type import ScenarioType

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
body = GoalCalculatorInputModel(
    is_new_goal=True,
    is_new_risk_profile=True,
    is_new_investment_tenure=True,
    is_new_goal_priority=True,
    reallocation_freq=ReallocationFreq.YEARLY,
    get_path=True,
    current_portfolio_id=None,
    loss_threshold=None,
    scenario_type=ScenarioType.REGULAR,
    risk_profile=RiskProfile.AGGRESSIVE,
    initial_investment=100000,
    current_wealth=100000,
    goal_priority=GoalCalculatorGoalPriorityAttribute.NEED,
    goal_amount=0,
    start_date='19-09-2023',
    end_date='01-11-2032',
    infusion_type=InfusionType.YEARLY,
    infusions=[
        0,
        5000,
        5000,
        5000,
        5000,
        5000,
        5000,
        5000,
        5000,
        5000,
        0
    ],
    reallocate=False,
    use_age_based_cap=False,
    curr_date='19-09-2023',
    calibrate_recommendations=True,
    stepup_date='01-01-2024',
    inflation=0
)

try:
    result = goe_api.goal_calculator(body)

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

