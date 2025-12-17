from complexheaderparametersapi.complexheaderparametersapi_client import ComplexheaderparametersapiClient
from complexheaderparametersapi.configuration import Environment
from complexheaderparametersapi.exceptions.api_exception import APIException
from complexheaderparametersapi.models.paypal_mock_response_schema import PaypalMockResponseSchema

client = ComplexheaderparametersapiClient(
    environment=Environment.PRODUCTION
)

client_controller = client.client
pay_pal_mock_response = PaypalMockResponseSchema(
    mock_application_codes='DUPLICATE_INVOICE_ID'
)

try:
    result = client_controller.retrieve_checkout_order(
        pay_pal_mock_response=pay_pal_mock_response
    )

    if result.is_success():
        print(result.body)
    elif result.is_error():
        print(result.errors)

except APIException as e: 
    print(e)

