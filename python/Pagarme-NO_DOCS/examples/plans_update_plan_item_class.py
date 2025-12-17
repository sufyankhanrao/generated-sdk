from pagarmeapisdk.configuration import Environment
from pagarmeapisdk.exceptions.api_exception import APIException
from pagarmeapisdk.exceptions.error_exception import ErrorException
from pagarmeapisdk.http.auth.basic_auth import BasicAuthCredentials
from pagarmeapisdk.models.update_plan_item_request import UpdatePlanItemRequest
from pagarmeapisdk.models.update_price_bracket_request import UpdatePriceBracketRequest
from pagarmeapisdk.models.update_pricing_scheme_request import UpdatePricingSchemeRequest
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

plan_item_id = 'plan_item_id0'

body = UpdatePlanItemRequest(
    name='name6',
    description='description4',
    status='status2',
    pricing_scheme=UpdatePricingSchemeRequest(
        scheme_type='scheme_type8',
        price_brackets=[
            UpdatePriceBracketRequest(
                start_quantity=144,
                price=174
            )
        ]
    )
)

try:
    result = plans_controller.update_plan_item(
        plan_id,
        plan_item_id,
        body
    )

    if result.is_success():
        print(result.body)
    elif result.is_error():
        print(result.errors)

except ErrorException as e: 
    print(e)
except APIException as e: 
    print(e)

