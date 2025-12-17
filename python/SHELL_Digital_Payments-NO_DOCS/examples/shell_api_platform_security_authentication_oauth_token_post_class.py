from shelldigitalpayments.configuration import Environment
from shelldigitalpayments.exceptions.access_token_error_exception import AccessTokenErrorException
from shelldigitalpayments.exceptions.api_exception import APIException
from shelldigitalpayments.shell_digital_payments_client import ShellDigitalPaymentsClient

client = ShellDigitalPaymentsClient(
    environment=Environment.PRODUCTION
)

shell_api_platform_security_authentication_controller = client.shell_api_platform_security_authentication
grant_type = 'client_credentials'

client_id = 'SOFflRakNlwnWlxfOXQ4GHDVyqGawuKA'

client_secret = 'cRnWgw7gACqM3gVS'

try:
    result = shell_api_platform_security_authentication_controller.oauth_token_post(
        grant_type,
        client_id,
        client_secret
    )

    if result.is_success():
        print(result.body)
    elif result.is_error():
        print(result.errors)

except AccessTokenErrorException as e: 
    print(e)
except APIException as e: 
    print(e)

