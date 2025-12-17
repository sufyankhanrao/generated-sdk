from mindbodypublicapi.configuration import Environment
from mindbodypublicapi.exceptions.api_exception import APIException
from mindbodypublicapi.mindbodypublicapi_client import MindbodypublicapiClient
from mindbodypublicapi.models.send_password_reset_email_request import SendPasswordResetEmailRequest

client = MindbodypublicapiClient(
    environment=Environment.PRODUCTION
)

client_controller = client.client
version = '6'

request = SendPasswordResetEmailRequest(
    user_email='UserEmail2',
    user_first_name='UserFirstName2',
    user_last_name='UserLastName8'
)

site_id = '-99'

authorization = 'authorization6'

try:
    result = client_controller.send_password_reset_email(
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

