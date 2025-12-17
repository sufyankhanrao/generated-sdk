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
from goeapi.models.goal_discovery_goal_priority_attribute import GoalDiscoveryGoalPriorityAttribute
from goeapi.models.goal_discovery_input_model import GoalDiscoveryInputModel
from goeapi.models.goal_tenure_2 import GoalTenure2
from goeapi.models.goal_type import GoalType
from goeapi.models.infusion_type_1 import InfusionType1
from goeapi.models.infusions_2 import Infusions2
from goeapi.models.initial_investment_2 import InitialInvestment2
from goeapi.models.risk_profile_1 import RiskProfile1
from goeapi.models.target_wealth_2 import TargetWealth2

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
body = GoalDiscoveryInputModel(
    goal_type=GoalType.RETIREMENT,
    risk_profile=RiskProfile1.MODERATE,
    initial_investment=InitialInvestment2(
        min=100000,
        max=77.92
    ),
    goal_priority=[
        GoalDiscoveryGoalPriorityAttribute.NEED
    ],
    infusion_type=InfusionType1.YEARLY,
    infusions=Infusions2(
        min=102,
        max=20
    ),
    goal_tenure=GoalTenure2(
        min=120,
        max=38
    ),
    target_wealth=TargetWealth2(
        min=100000,
        max=35.54
    ),
    page_size=12000
)

try:
    result = goe_api.goal_discovery(body)

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

