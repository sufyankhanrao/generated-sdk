import dateutil.parser

from mindbodypublicapi.configuration import Environment
from mindbodypublicapi.exceptions.api_exception import APIException
from mindbodypublicapi.mindbodypublicapi_client import MindbodypublicapiClient

client = MindbodypublicapiClient(
    environment=Environment.PRODUCTION
)

mclass_controller = client.mclass
version = '6'

request_class_id = 222

site_id = '-99'

authorization = 'authorization6'

request_last_modified_date = dateutil.parser.parse('2016-03-13T12:52:32.123Z')

try:
    result = mclass_controller.get_class_visits(
        version,
        request_class_id,
        site_id,
        authorization=authorization,
        request_last_modified_date=request_last_modified_date
    )

    if result.is_success():
        print(result.body)
    elif result.is_error():
        print(result.errors)

except APIException as e: 
    print(e)

