from shellev.configuration import Environment
from shellev.exceptions.api_exception import APIException
from shellev.exceptions.bad_request_exception import BadRequestException
from shellev.exceptions.internal_server_error_exception import InternalServerErrorException
from shellev.exceptions.not_found_exception import NotFoundException
from shellev.exceptions.serviceunavailable_exception import ServiceunavailableException
from shellev.exceptions.too_many_requests_exception import TooManyRequestsException
from shellev.exceptions.unauthorized_exception import UnauthorizedException
from shellev.http.auth.o_auth_2 import ClientCredentialsAuthCredentials
from shellev.models.chargesession_start_body import ChargesessionStartBody
from shellev.shellev_client import ShellevClient

client = ShellevClient(
    client_credentials_auth_credentials=ClientCredentialsAuthCredentials(
        o_auth_client_id='OAuthClientId',
        o_auth_client_secret='OAuthClientSecret'
    ),
    environment=Environment.PRODUCTION
)

charging_controller = client.charging
request_id = '123e4567-e89b-12d3-a456-426614174000'

body = ChargesessionStartBody(
    ev_charge_number='NL-TNM-C00122045-K',
    evse_id='NL*TNM*E02003451*0'
)

try:
    result = charging_controller.start(
        request_id,
        body=body
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

