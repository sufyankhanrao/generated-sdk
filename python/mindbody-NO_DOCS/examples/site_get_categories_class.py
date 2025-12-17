from mindbodypublicapi.configuration import Environment
from mindbodypublicapi.exceptions.api_exception import APIException
from mindbodypublicapi.mindbodypublicapi_client import MindbodypublicapiClient

client = MindbodypublicapiClient(
    environment=Environment.PRODUCTION
)

site_controller = client.site
version = '6'

site_id = '-99'

authorization = 'authorization6'

request_active = False

request_category_ids = [
    140,
    141
]

request_limit = 62

request_offset = 100

request_service = False

request_sub_category_ids = [
    173,
    174,
    175
]

try:
    result = site_controller.get_categories(
        version,
        site_id,
        authorization=authorization,
        request_active=request_active,
        request_category_ids=request_category_ids,
        request_limit=request_limit,
        request_offset=request_offset,
        request_service=request_service,
        request_sub_category_ids=request_sub_category_ids
    )

    if result.is_success():
        print(result.body)
    elif result.is_error():
        print(result.errors)

except APIException as e: 
    print(e)

