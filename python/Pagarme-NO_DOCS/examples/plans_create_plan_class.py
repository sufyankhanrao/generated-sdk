from pagarmeapisdk.configuration import Environment
from pagarmeapisdk.exceptions.api_exception import APIException
from pagarmeapisdk.exceptions.error_exception import ErrorException
from pagarmeapisdk.http.auth.basic_auth import BasicAuthCredentials
from pagarmeapisdk.models.create_plan_item_request import CreatePlanItemRequest
from pagarmeapisdk.models.create_plan_request import CreatePlanRequest
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
body = CreatePlanRequest(
    name='name6',
    description='description4',
    statement_descriptor='statement_descriptor6',
    items=[
        CreatePlanItemRequest(
            name='name8',
            pricing_scheme=CreatePricingSchemeRequest(
                scheme_type='scheme_type8'
            ),
            id='id8',
            description='description2'
        )
    ],
    shippable=False,
    payment_methods=[
        'payment_methods9'
    ],
    installments=[
        207
    ],
    currency='currency6',
    interval='interval6',
    interval_count=170,
    billing_days=[
        201,
        200
    ],
    billing_type='billing_type0',
    pricing_scheme=CreatePricingSchemeRequest(
        scheme_type='scheme_type8'
    ),
    metadata={
        'key0': 'metadata7',
        'key1': 'metadata8'
    }
)

try:
    result = plans_controller.create_plan(body)

    if result.is_success():
        print(result.body)
    elif result.is_error():
        print(result.errors)

except ErrorException as e: 
    print(e)
except APIException as e: 
    print(e)

