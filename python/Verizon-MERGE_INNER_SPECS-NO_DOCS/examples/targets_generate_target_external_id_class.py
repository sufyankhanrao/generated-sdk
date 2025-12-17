from verizon.configuration import Environment
from verizon.exceptions.api_exception import APIException
from verizon.models.account_identifier import AccountIdentifier
from verizon.models.generate_external_id_request import GenerateExternalIDRequest
from verizon.verizon_client import VerizonClient

client = VerizonClient(
    environment=Environment.PRODUCTION
)

targets_controller = client.targets
body = GenerateExternalIDRequest(
    accountidentifier=AccountIdentifier(
        billingaccountid='0000000000-00001'
    )
)

try:
    result = targets_controller.generate_target_external_id(body)

    if result.is_success():
        print(result.body)
    elif result.is_error():
        print(result.errors)

except APIException as e: 
    print(e)

