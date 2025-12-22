import dateutil.parser

from additionalpropertiestester.additionalpropertiestester_client import AdditionalpropertiestesterClient
from additionalpropertiestester.configuration import Environment
from additionalpropertiestester.exceptions.api_exception import APIException
from additionalpropertiestester.models.date_additional_properties import DateAdditionalProperties

client = AdditionalpropertiestesterClient(
    environment=Environment.PRODUCTION
)

body_controller = client.body
body = DateAdditionalProperties(
    required_property=dateutil.parser.parse('2024-11-01').date(),
    additional_properties={
        'additionalProperty1': dateutil.parser.parse('2023-11-01').date(),
        'additionalProperty2': dateutil.parser.parse('2027-11-01').date()
    }
)

try:
    result = body_controller.upload_date_additional_properties(body)

    if result.is_success():
        print(result.body)
    elif result.is_error():
        print(result.errors)

except APIException as e: 
    print(e)

