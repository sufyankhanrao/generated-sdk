from advancedbilling.advanced_billing_client import AdvancedBillingClient
from advancedbilling.configuration import Environment
from advancedbilling.exceptions.api_exception import APIException
from advancedbilling.exceptions.customer_error_response_exception import CustomerErrorResponseException
from advancedbilling.http.auth.basic_auth import BasicAuthCredentials
from advancedbilling.models.create_customer import CreateCustomer
from advancedbilling.models.create_customer_request import CreateCustomerRequest

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
body = CreateCustomerRequest(
    customer=CreateCustomer(
        first_name='Martha',
        last_name='Washington',
        email='martha@example.com',
        cc_emails='george@example.com',
        organization='ABC, Inc.',
        reference='1234567890',
        address='123 Main Street',
        address_2='Unit 10',
        city='Anytown',
        state='MA',
        zip='02120',
        country='US',
        phone='555-555-1212',
        locale='es-MX'
    )
)

try:
    result = customers_controller.create_customer(
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

