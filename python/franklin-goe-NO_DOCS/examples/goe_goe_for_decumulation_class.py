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
from goeapi.models.goe_for_decumulation_input_model import GoeForDecumulationInputModel
from goeapi.models.infusion_type import InfusionType
from goeapi.models.reallocation_freq_1 import ReallocationFreq1
from goeapi.models.risk_profile import RiskProfile

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
body = GoeForDecumulationInputModel(
    future_annuity_proj=True,
    risk_profile=RiskProfile.AGGRESSIVE,
    current_portfolio_id=None,
    date_of_birth='15-06-2020',
    db_income=[
        1000,
        1000,
        1000,
        1000,
        1000,
        1000
    ],
    other_guaranteed_income=[
        1000,
        1000,
        1000,
        1000,
        1000,
        1000
    ],
    existing_annuities_income=[
        1000,
        1000,
        1000,
        1000,
        1000,
        1000
    ],
    state_income=[
        1000,
        1000,
        1000,
        1000,
        1000,
        1000
    ],
    target_expenditures=[
        20400,
        20808,
        21224.2,
        21648.7,
        22081.7
    ],
    fixed_expense_fact=[
        158.68,
        158.69
    ],
    current_wealth=10000,
    initial_investment=100000,
    include_annuities=True,
    infusion_type=InfusionType.YEARLY,
    start_date='01-01-2023',
    end_date='01-01-2052',
    annuity_rate=0.0865,
    reallocation_freq=ReallocationFreq1.YEARLY,
    is_new_goal_priority=True,
    is_new_risk_profile=True,
    is_new_investment_tenure=True,
    is_new_goal=True,
    loss_threshold=100000,
    gender='unisex',
    health_status=0,
    cashflow_date='01-01-2024',
    retirement_age=65,
    reallocate=False
)

try:
    result = goe_api.goe_for_decumulation(body)

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

