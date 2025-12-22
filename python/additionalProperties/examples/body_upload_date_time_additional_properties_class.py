import dateutil.parser

from additionalpropertiestester.additionalpropertiestester_client import AdditionalpropertiestesterClient
from additionalpropertiestester.configuration import Environment
from additionalpropertiestester.exceptions.api_exception import APIException
from additionalpropertiestester.models.date_time_additional_properties import DateTimeAdditionalProperties

client = AdditionalpropertiestesterClient(
    environment=Environment.PRODUCTION
)

body_controller = client.body
body = DateTimeAdditionalProperties(
    required_property=dateutil.parser.parse('2024-11-01T00:00:00Z'),
    additional_properties={
        'additionalProperty1': dateutil.parser.parse('2023-11-01T00:00:00Z'),
        'additionalProperty2': dateutil.parser.parse('2027-11-01T00:00:00Z')
    }
)

try:
    result = body_controller.upload_date_time_additional_properties(body)
    print(result)
except APIException as e: 
    print(e)

