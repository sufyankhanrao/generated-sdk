from allowadditionalenumitemsapi.allowadditionalenumitemsapi_client import AllowadditionalenumitemsapiClient
from allowadditionalenumitemsapi.configuration import Environment
from allowadditionalenumitemsapi.exceptions.api_exception import APIException

client = AllowadditionalenumitemsapiClient(
    environment=Environment.PRODUCTION
)

client_controller = client.client
try:
    result = client_controller.get_enums()
    print(result)
except APIException as e: 
    print(e)

