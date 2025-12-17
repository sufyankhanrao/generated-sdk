from greenbyteapi.configuration import Environment
from greenbyteapi.exceptions.api_exception import APIException
from greenbyteapi.exceptions.problem_details_exception import ProblemDetailsException
from greenbyteapi.greenbyteapi_client import GreenbyteapiClient
from greenbyteapi.http.auth.custom_header_authentication import CustomHeaderAuthenticationCredentials
from greenbyteapi.models.aggregate_mode_enum import AggregateModeEnum
from greenbyteapi.models.calculation_mode_real_time_enum import CalculationModeRealTimeEnum

client = GreenbyteapiClient(
    custom_header_authentication_credentials=CustomHeaderAuthenticationCredentials(
        x_api_key='X-Api-Key'
    ),
    environment=Environment.PRODUCTION,
    customer='intro'
)

data_controller = client.data
device_ids = [
    1,
    2,
    3
]

data_signal_ids = [
    1,
    5
]

aggregate = AggregateModeEnum.SITE

aggregate_level = 0

calculation = CalculationModeRealTimeEnum.SUM

try:
    result = data_controller.get_real_time_data(
        device_ids,
        data_signal_ids,
        aggregate=aggregate,
        aggregate_level=aggregate_level,
        calculation=calculation
    )

    if result.is_success():
        print(result.body)
    elif result.is_error():
        print(result.errors)

except ProblemDetailsException as e: 
    print(e)
except APIException as e: 
    print(e)

