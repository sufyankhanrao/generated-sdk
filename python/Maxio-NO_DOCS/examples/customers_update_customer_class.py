from advancedbilling.advanced_billing_client import AdvancedBillingClient
from advancedbilling.configuration import Environment
from advancedbilling.exceptions.api_exception import APIException
from advancedbilling.exceptions.customer_error_response_exception import CustomerErrorResponseException
from advancedbilling.http.auth.basic_auth import BasicAuthCredentials
from advancedbilling.models.update_customer import UpdateCustomer
from advancedbilling.models.update_customer_request import UpdateCustomerRequest

client = AdvancedBillingClient(
    basic_auth_credentials=BasicAuthCredentials(
        username='BasicAuthUserName',
        password='BasicAuthPassword'
    ),
    environment=Environment.PRODUCTION,
    subdomain='subdomain',
    domain='chargify.com'
)

customers_controller = client.customers
id = 112

body = UpdateCustomerRequest(
    customer=UpdateCustomer(
        first_name='Martha',
        last_name='Washington',
        email='martha.washington@example.com'
    )
)

try:
    result = customers_controller.update_customer(
        id,
        body=body
    )

    if result.is_success():
        print(result.body)
    elif result.is_error():
        print(result.errors)

except CustomerErrorResponseException as e: 
    print(e)
except APIException as e: 
    print(e)

