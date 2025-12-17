import dateutil.parser

from greenbyteapi.configuration import Environment
from greenbyteapi.exceptions.api_exception import APIException
from greenbyteapi.exceptions.problem_details_exception import ProblemDetailsException
from greenbyteapi.greenbyteapi_client import GreenbyteapiClient
from greenbyteapi.http.auth.custom_header_authentication import CustomHeaderAuthenticationCredentials
from greenbyteapi.models.aggregate_mode_enum import AggregateModeEnum
from greenbyteapi.models.contract_type_enum import ContractTypeEnum
from greenbyteapi.models.status_category_enum import StatusCategoryEnum

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

data_signal_id = 248

timestamp_start = dateutil.parser.parse('2024-01-01T00:00:00Z')

timestamp_end = dateutil.parser.parse('2024-01-08T00:00:00Z')

aggregate = AggregateModeEnum.SITE

aggregate_level = 0

category = [
    StatusCategoryEnum.STOP
]

contract_type = ContractTypeEnum.SERVICE

try:
    result = data_controller.get_data_per_category(
        device_ids,
        data_signal_id,
        timestamp_start,
        timestamp_end,
        aggregate=aggregate,
        aggregate_level=aggregate_level,
        category=category,
        contract_type=contract_type
    )

    if result.is_success():
        print(result.body)
    elif result.is_error():
        print(result.errors)

except ProblemDetailsException as e: 
    print(e)
except APIException as e: 
    print(e)

