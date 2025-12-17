from mindbodypublicapi.configuration import Environment
from mindbodypublicapi.exceptions.api_exception import APIException
from mindbodypublicapi.mindbodypublicapi_client import MindbodypublicapiClient

client = MindbodypublicapiClient(
    environment=Environment.PRODUCTION
)

staff_controller = client.staff
version = '6'

site_id = '-99'

authorization = 'authorization6'

request_active_only = False

request_limit = 62

request_offset = 100

request_sales_rep_numbers = [
    123,
    124,
    125
]

try:
    result = staff_controller.get_sales_reps(
        version,
        site_id,
        authorization=authorization,
        request_active_only=request_active_only,
        request_limit=request_limit,
        request_offset=request_offset,
        request_sales_rep_numbers=request_sales_rep_numbers
    )

    if result.is_success():
        print(result.body)
    elif result.is_error():
        print(result.errors)

except APIException as e: 
    print(e)

