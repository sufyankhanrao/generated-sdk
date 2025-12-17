import dateutil.parser

from mindbodypublicapi.configuration import Environment
from mindbodypublicapi.exceptions.api_exception import APIException
from mindbodypublicapi.mindbodypublicapi_client import MindbodypublicapiClient
from mindbodypublicapi.models.add_contact_log_request import AddContactLogRequest

client = MindbodypublicapiClient(
    environment=Environment.PRODUCTION
)

client_controller = client.client
version = '6'

request = AddContactLogRequest(
    client_id='ClientId0',
    contact_method='ContactMethod0',
    assigned_to_staff_id=202,
    text='Text8',
    followup_by_date=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
    contact_name='ContactName6',
    is_complete=False
)

site_id = '-99'

authorization = 'authorization6'

try:
    result = client_controller.add_contact_log(
        version,
        request,
        site_id,
        authorization=authorization
    )

    if result.is_success():
        print(result.body)
    elif result.is_error():
        print(result.errors)

except APIException as e: 
    print(e)

