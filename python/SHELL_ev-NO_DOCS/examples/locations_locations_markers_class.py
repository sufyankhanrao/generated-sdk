from shellev.configuration import Environment
from shellev.exceptions.api_exception import APIException
from shellev.exceptions.bad_request_exception import BadRequestException
from shellev.exceptions.internal_server_error_exception import InternalServerErrorException
from shellev.exceptions.not_found_exception import NotFoundException
from shellev.exceptions.serviceunavailable_exception import ServiceunavailableException
from shellev.exceptions.too_many_requests_exception import TooManyRequestsException
from shellev.exceptions.unauthorized_exception import UnauthorizedException
from shellev.http.auth.o_auth_2 import ClientCredentialsAuthCredentials
from shellev.shellev_client import ShellevClient

client = ShellevClient(
    client_credentials_auth_credentials=ClientCredentialsAuthCredentials(
        o_auth_client_id='OAuthClientId',
        o_auth_client_secret='OAuthClientSecret'
    ),
    environment=Environment.PRODUCTION
)

locations_controller = client.locations
request_id = '123e4567-e89b-12d3-a456-426614174000'

west = 152.84

south = 13.76

east = 16.36

north = 73.98

zoom = 'zoom0'

country = [
    'NED'
]

exclude_country = [
    'NED'
]

try:
    result = locations_controller.locations_markers(
        request_id,
        west,
        south,
        east,
        north,
        zoom,
        country=country,
        exclude_country=exclude_country
    )

    if result.is_success():
        print(result.body)
    elif result.is_error():
        print(result.errors)

except BadRequestException as e: 
    print(e)
except UnauthorizedException as e: 
    print(e)
except NotFoundException as e: 
    print(e)
except TooManyRequestsException as e: 
    print(e)
except InternalServerErrorException as e: 
    print(e)
except ServiceunavailableException as e: 
    print(e)
except APIException as e: 
    print(e)

