from mindbodypublicapi.configuration import Environment
from mindbodypublicapi.exceptions.api_exception import APIException
from mindbodypublicapi.mindbodypublicapi_client import MindbodypublicapiClient
from mindbodypublicapi.models.generate_signed_live_stream_url_request import GenerateSignedLiveStreamUrlRequest

client = MindbodypublicapiClient(
    environment=Environment.PRODUCTION
)

live_stream_controller = client.live_stream
version = '6'

request = GenerateSignedLiveStreamUrlRequest(
    client_id=98,
    subscriber_id=198,
    user_display_name='UserDisplayName6',
    service_id=130,
    api_user='ApiUser2'
)

site_id = '-99'

authorization = 'authorization6'

try:
    result = live_stream_controller.generate_signed_live_stream_url(
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

