from greenbyteapi.configuration import Environment
from greenbyteapi.exceptions.api_exception import APIException
from greenbyteapi.exceptions.problem_details_exception import ProblemDetailsException
from greenbyteapi.greenbyteapi_client import GreenbyteapiClient
from greenbyteapi.http.auth.custom_header_authentication import CustomHeaderAuthenticationCredentials
from greenbyteapi.models.contract_type_enum import ContractTypeEnum

client = GreenbyteapiClient(
    custom_header_authentication_credentials=CustomHeaderAuthenticationCredentials(
        x_api_key='X-Api-Key'
    ),
    environment=Environment.PRODUCTION,
    customer='intro'
)

statuses_controller = client.statuses
device_ids = [
    1,
    2,
    3
]

lost_production_signal_id = 432

fields = [
    'deviceId',
    'message',
    'lostProduction'
]

sort_asc = False

page_size = 50

page = 1

use_utc = False

contract_type = ContractTypeEnum.SERVICE

try:
    result = statuses_controller.get_active_statuses(
        device_ids,
        lost_production_signal_id=lost_production_signal_id,
        fields=fields,
        sort_asc=sort_asc,
        page_size=page_size,
        page=page,
        use_utc=use_utc,
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

