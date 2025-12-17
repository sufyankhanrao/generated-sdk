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
from goeapi.models.goal_priority import GoalPriority
from goeapi.models.infusion_type import InfusionType
from goeapi.models.reallocation_freq import ReallocationFreq
from goeapi.models.risk_profile_6 import RiskProfile6
from goeapi.models.run_pipe_input_model import RunPipeInputModel
from goeapi.models.scenario_type_1 import ScenarioType1

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
body = RunPipeInputModel(
    is_new_goal_priority=True,
    is_new_investment_tenure=True,
    is_new_risk_profile=True,
    is_new_goal=True,
    get_path=True,
    reallocation_freq=ReallocationFreq.YEARLY,
    goal_amount=1000000,
    initial_investment=95027,
    current_wealth=95027,
    start_date='13-01-2021',
    end_date='10-10-2055',
    goal_priority=GoalPriority.NEED,
    current_portfolio_id=None,
    infusions=[
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0
    ],
    risk_profile=RiskProfile6.MODERATE,
    scenario_type=ScenarioType1.REGULAR,
    infusion_type=InfusionType.YEARLY,
    cashflow_date='11-10-2020',
    curr_date='13-01-2021',
    use_age_based_cap=False,
    additional_properties={
        'lastReallocatedDate': jsonpickle.decode('"01-01-2020"'),
        'isNearTermVolatility': jsonpickle.decode('true'),
        'calibrateRecommendations': jsonpickle.decode('true')
    }
)

version = '4'

try:
    result = goe_api.run_pipe(
        body,
        version=version
    )

    if result.is_success():
        print(result.body)
    elif result.is_error():
        print(result.errors)

except MessageException as e: 
    print(e)
except ValidationMessageOneException as e: 
    print(e)
except InternalServerMessageException as e: 
    print(e)
except ApiException as e: 
    print(e)

