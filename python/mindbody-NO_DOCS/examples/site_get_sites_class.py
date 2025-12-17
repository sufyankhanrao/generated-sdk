from mindbodypublicapi.configuration import Environment
from mindbodypublicapi.exceptions.api_exception import APIException
from mindbodypublicapi.mindbodypublicapi_client import MindbodypublicapiClient

client = MindbodypublicapiClient(
    environment=Environment.PRODUCTION
)

site_controller = client.site
version = '6'

authorization = 'authorization6'

request_include_lead_channels = False

request_limit = 62

request_offset = 100

request_site_ids = [
    135,
    136
]

try:
    result = site_controller.get_sites(
        version,
        authorization=authorization,
        request_include_lead_channels=request_include_lead_channels,
        request_limit=request_limit,
        request_offset=request_offset,
        request_site_ids=request_site_ids
    )

    if result.is_success():
        print(result.body)
    elif result.is_error():
        print(result.errors)

except APIException as e: 
    print(e)

