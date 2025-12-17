from greenbyteapi.configuration import Environment
from greenbyteapi.exceptions.api_exception import APIException
from greenbyteapi.exceptions.problem_details_exception import ProblemDetailsException
from greenbyteapi.greenbyteapi_client import GreenbyteapiClient
from greenbyteapi.http.auth.custom_header_authentication import CustomHeaderAuthenticationCredentials

client = GreenbyteapiClient(
    custom_header_authentication_credentials=CustomHeaderAuthenticationCredentials(
        x_api_key='X-Api-Key'
    ),
    environment=Environment.PRODUCTION,
    customer='intro'
)

alerts_controller = client.alerts
device_ids = [
    1,
    2,
    3
]

fields = [
    'ruleId',
    'timestampStart'
]

sort_asc = False

page_size = 50

page = 1

use_utc = False

try:
    result = alerts_controller.get_active_alerts(
        device_ids,
        fields=fields,
        sort_asc=sort_asc,
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

