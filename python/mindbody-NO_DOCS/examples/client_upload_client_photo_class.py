from mindbodypublicapi.configuration import Environment
from mindbodypublicapi.exceptions.api_exception import APIException
from mindbodypublicapi.mindbodypublicapi_client import MindbodypublicapiClient
from mindbodypublicapi.models.upload_client_photo_request import UploadClientPhotoRequest

client = MindbodypublicapiClient(
    environment=Environment.PRODUCTION
)

client_controller = client.client
version = '6'

request = UploadClientPhotoRequest(
    bytes='Bytes6',
    client_id='ClientId0'
)

site_id = '-99'

authorization = 'authorization6'

try:
    result = client_controller.upload_client_photo(
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

