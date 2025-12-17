import dateutil.parser

from greenbyteapi.configuration import Environment
from greenbyteapi.exceptions.api_exception import APIException
from greenbyteapi.exceptions.problem_details_exception import ProblemDetailsException
from greenbyteapi.greenbyteapi_client import GreenbyteapiClient
from greenbyteapi.http.auth.custom_header_authentication import CustomHeaderAuthenticationCredentials
from greenbyteapi.models.predict_severity_enum import PredictSeverityEnum
from greenbyteapi.models.predict_status_enum import PredictStatusEnum

client = GreenbyteapiClient(
    custom_header_authentication_credentials=CustomHeaderAuthenticationCredentials(
        x_api_key='X-Api-Key'
    ),
    environment=Environment.PRODUCTION,
    customer='intro'
)

predict_controller = client.predict
device_ids = [
    1,
    2,
    3
]

timestamp_start = dateutil.parser.parse('2024-01-01T00:00:00Z')

timestamp_end = dateutil.parser.parse('2024-01-08T00:00:00Z')

site_ids = [
    1,
    2,
    3
]

component_ids = [
    1,
    2,
    3
]

status = PredictStatusEnum.ACTIVE

severity = PredictSeverityEnum.HIGH

fields = [
    'deviceId',
    'highSeverity'
]

page_size = 50

page = 1

use_utc = False

try:
    result = predict_controller.get_predict_alerts(
        device_ids,
        timestamp_start,
        timestamp_end,
        site_ids=site_ids,
        component_ids=component_ids,
        status=status,
        severity=severity,
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

