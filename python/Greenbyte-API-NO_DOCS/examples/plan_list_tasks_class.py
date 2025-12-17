import dateutil.parser

from greenbyteapi.configuration import Environment
from greenbyteapi.exceptions.api_exception import APIException
from greenbyteapi.exceptions.problem_details_exception import ProblemDetailsException
from greenbyteapi.greenbyteapi_client import GreenbyteapiClient
from greenbyteapi.http.auth.custom_header_authentication import CustomHeaderAuthenticationCredentials
from greenbyteapi.models.task_state_enum import TaskStateEnum

client = GreenbyteapiClient(
    custom_header_authentication_credentials=CustomHeaderAuthenticationCredentials(
        x_api_key='X-Api-Key'
    ),
    environment=Environment.PRODUCTION,
    customer='intro'
)

plan_controller = client.plan
timestamp_start = dateutil.parser.parse('2024-01-01T00:00:00Z')

timestamp_end = dateutil.parser.parse('2024-01-08T00:00:00Z')

device_ids = [
    1,
    2,
    3
]

site_ids = [
    1,
    2,
    3
]

category_ids = [
    1,
    2,
    3
]

state = TaskStateEnum.UNRESOLVED

fields = [
    'taskId',
    'title'
]

page_size = 50

page = 1

use_utc = False

try:
    result = plan_controller.list_tasks(
        timestamp_start,
        timestamp_end,
        device_ids=device_ids,
        site_ids=site_ids,
        category_ids=category_ids,
        state=state,
        fields=fields,
        page_size=page_size,
        page=page,
        use_utc=use_utc
    )

    if result.is_success():
        print(result.body)
    elif result.is_error():
        print(result.errors)

except ProblemDetailsException as e: 
    print(e)
except APIException as e: 
    print(e)

