import dateutil.parser

from mindbodypublicapi.configuration import Environment
from mindbodypublicapi.exceptions.api_exception import APIException
from mindbodypublicapi.mindbodypublicapi_client import MindbodypublicapiClient

client = MindbodypublicapiClient(
    environment=Environment.PRODUCTION
)

client_controller = client.client
version = '6'

site_id = '-99'

authorization = 'authorization6'

request_client_i_ds = [
    'request.clientIDs9',
    'request.clientIDs0',
    'request.clientIDs1'
]

request_include_inactive = False

request_is_prospect = False

request_last_modified_date = dateutil.parser.parse('2016-03-13T12:52:32.123Z')

request_limit = 62

request_offset = 100

request_search_text = 'request.searchText0'

request_unique_ids = [
    123,
    124,
    125
]

try:
    result = client_controller.get_clients(
        version,
        site_id,
        authorization=authorization,
        request_client_i_ds=request_client_i_ds,
        request_include_inactive=request_include_inactive,
        request_is_prospect=request_is_prospect,
        request_last_modified_date=request_last_modified_date,
        request_limit=request_limit,
        request_offset=request_offset,
        request_search_text=request_search_text,
        request_unique_ids=request_unique_ids
    )

    if result.is_success():
        print(result.body)
    elif result.is_error():
        print(result.errors)

except APIException as e: 
    print(e)

