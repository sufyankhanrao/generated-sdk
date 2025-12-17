from pagarmeapisdk.configuration import Environment
from pagarmeapisdk.exceptions.api_exception import APIException
from pagarmeapisdk.exceptions.error_exception import ErrorException
from pagarmeapisdk.http.auth.basic_auth import BasicAuthCredentials
from pagarmeapisdk.models.create_plan_item_request import CreatePlanItemRequest
from pagarmeapisdk.models.create_pricing_scheme_request import CreatePricingSchemeRequest
from pagarmeapisdk.pagarmeapisdk_client import PagarmeapisdkClient

client = PagarmeapisdkClient(
    service_referer_name='ServiceRefererName',
    basic_auth_credentials=BasicAuthCredentials(
        username='BasicAuthUserName',
        password='BasicAuthPassword'
    ),
    environment=Environment.PRODUCTION
)

plans_controller = client.plans
plan_id = 'plan_id8'

request = CreatePlanItemRequest(
    name='name6',
    pricing_scheme=CreatePricingSchemeRequest(
        scheme_type='scheme_type8'
    ),
    id='id6',
    description='description6'
)

try:
    result = plans_controller.create_plan_item(
        plan_id,
        request
    )

    if result.is_success():
        print(result.body)
    elif result.is_error():
        print(result.errors)

except ErrorException as e: 
    print(e)
except APIException as e: 
    print(e)

