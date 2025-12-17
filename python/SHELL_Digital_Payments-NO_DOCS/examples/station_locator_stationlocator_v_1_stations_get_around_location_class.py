from shelldigitalpayments.configuration import Environment
from shelldigitalpayments.exceptions.api_exception import APIException
from shelldigitalpayments.exceptions.station_locator_bad_request_exception import StationLocatorBadRequestException
from shelldigitalpayments.exceptions.station_locator_forbidden_exception import StationLocatorForbiddenException
from shelldigitalpayments.exceptions.station_locator_internal_server_error_exception import StationLocatorInternalServerErrorException
from shelldigitalpayments.exceptions.station_locator_not_found_exception import StationLocatorNotFoundException
from shelldigitalpayments.exceptions.station_locator_unauthorized_exception import StationLocatorUnauthorizedException
from shelldigitalpayments.http.auth.o_auth_token_post import OAuthTokenPostCredentials
from shelldigitalpayments.shell_digital_payments_client import ShellDigitalPaymentsClient

client = ShellDigitalPaymentsClient(
    o_auth_token_post_credentials=OAuthTokenPostCredentials(
        x_apigee_authorization='X-Apigee-Authorization'
    ),
    environment=Environment.PRODUCTION
)

station_locator_controller = client.station_locator
m = 'aroundLocation'

lon = 77.6730103

lat = 12.9132169

radius = 0.3

try:
    result = station_locator_controller.stationlocator_v_1_stations_get_around_location(
        m,
        lon,
        lat,
        radius
    )

    if result.is_success():
        print(result.body)
    elif result.is_error():
        print(result.errors)

except StationLocatorBadRequestException as e: 
    print(e)
except StationLocatorUnauthorizedException as e: 
    print(e)
except StationLocatorForbiddenException as e: 
    print(e)
except StationLocatorNotFoundException as e: 
    print(e)
except StationLocatorInternalServerErrorException as e: 
    print(e)
except APIException as e: 
    print(e)

