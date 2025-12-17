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
from goeapi.models.annuity_payout_freq import AnnuityPayoutFreq
from goeapi.models.annuity_price import AnnuityPrice
from goeapi.models.annuity_type import AnnuityType
from goeapi.models.contribution_freq import ContributionFreq
from goeapi.models.goe_with_annuities_input_model import GoeWithAnnuitiesInputModel
from goeapi.models.marital_status import MaritalStatus
from goeapi.models.other_income_freq import OtherIncomeFreq
from goeapi.models.risk_profile_5 import RiskProfile5
from goeapi.models.value import Value

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
body = GoeWithAnnuitiesInputModel(
    include_annuities=True,
    date_of_birth='01-01-1981',
    retirement_age=61,
    drawdown_age=66,
    planning_age=82,
    current_salary=350000,
    total_account_balance=1260000,
    balance_proportion=0.1,
    periodic_contributions=8750,
    contribution_freq=ContributionFreq.MONTHLY,
    outside_assets=210000,
    current_portfolio_id=None,
    current_date='01-01-2024',
    risk_profile=RiskProfile5.AGGRESSIVE,
    annuity_type=AnnuityType.DEFERRED,
    annuity_price=[
        AnnuityPrice(
            age=43,
            value=[
                Value(
                    year=2024,
                    rate=10
                )
            ]
        ),
        AnnuityPrice(
            age=44,
            value=[
                Value(
                    year=2025,
                    rate=10
                )
            ]
        ),
        AnnuityPrice(
            age=45,
            value=[
                Value(
                    year=2026,
                    rate=10
                )
            ]
        ),
        AnnuityPrice(
            age=46,
            value=[
                Value(
                    year=2027,
                    rate=10
                )
            ]
        ),
        AnnuityPrice(
            age=47,
            value=[
                Value(
                    year=2028,
                    rate=10
                )
            ]
        ),
        AnnuityPrice(
            age=48,
            value=[
                Value(
                    year=2029,
                    rate=10
                )
            ]
        ),
        AnnuityPrice(
            age=49,
            value=[
                Value(
                    year=2030,
                    rate=10
                )
            ]
        ),
        AnnuityPrice(
            age=50,
            value=[
                Value(
                    year=2031,
                    rate=10
                )
            ]
        ),
        AnnuityPrice(
            age=51,
            value=[
                Value(
                    year=2032,
                    rate=10
                )
            ]
        ),
        AnnuityPrice(
            age=52,
            value=[
                Value(
                    year=2033,
                    rate=10
                )
            ]
        ),
        AnnuityPrice(
            age=53,
            value=[
                Value(
                    year=2034,
                    rate=10
                )
            ]
        ),
        AnnuityPrice(
            age=54,
            value=[
                Value(
                    year=2035,
                    rate=10
                )
            ]
        ),
        AnnuityPrice(
            age=55,
            value=[
                Value(
                    year=2036,
                    rate=10
                )
            ]
        ),
        AnnuityPrice(
            age=56,
            value=[
                Value(
                    year=2037,
                    rate=10
                )
            ]
        ),
        AnnuityPrice(
            age=57,
            value=[
                Value(
                    year=2038,
                    rate=10
                )
            ]
        ),
        AnnuityPrice(
            age=58,
            value=[
                Value(
                    year=2039,
                    rate=10
                )
            ]
        ),
        AnnuityPrice(
            age=59,
            value=[
                Value(
                    year=2040,
                    rate=10
                )
            ]
        ),
        AnnuityPrice(
            age=60,
            value=[
                Value(
                    year=2041,
                    rate=10
                )
            ]
        ),
        AnnuityPrice(
            age=61,
            value=[
                Value(
                    year=2042,
                    rate=10
                )
            ]
        )
    ],
    annuity_payout_freq=AnnuityPayoutFreq.YEARLY,
    marital_status=MaritalStatus.MARRIED,
    spousal_salary=250000,
    job_tenure=31,
    current_annuity_balance=35000,
    retirement_income_goal=25000,
    drawdown_age_ss=64,
    income_from_ss=10000,
    other_income=25000,
    other_income_freq=OtherIncomeFreq.YEARLY,
    calculate_retirement_income_goal=True,
    additional_properties={
        'currAge': jsonpickle.decode('43')
    }
)

try:
    result = goe_api.goe_with_annuities(body)

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

