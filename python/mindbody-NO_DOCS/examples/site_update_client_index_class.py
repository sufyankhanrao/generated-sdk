from mindbodypublicapi.configuration import Environment
from mindbodypublicapi.exceptions.api_exception import APIException
from mindbodypublicapi.mindbodypublicapi_client import MindbodypublicapiClient
from mindbodypublicapi.models.update_site_client_index_request import UpdateSiteClientIndexRequest

client = MindbodypublicapiClient(
    environment=Environment.PRODUCTION
)

site_controller = client.site
version = '6'

request = UpdateSiteClientIndexRequest(
    client_index_id=194,
    client_index_name='ClientIndexName2',
    active=False,
    show_on_new_client=False,
    show_on_enrollment_roster=False,
    edit_on_enrollment_roster=False,
    sort_order=50
)

site_id = '-99'

authorization = 'authorization6'

try:
    result = site_controller.update_client_index(
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

