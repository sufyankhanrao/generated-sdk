
from advancedbilling.advanced_billing_client import AdvancedBillingClient
from advancedbilling.configuration import Environment
from advancedbilling.exceptions.api_exception import APIException
from advancedbilling.exceptions.error_list_response_exception import ErrorListResponseException
from advancedbilling.http.auth.basic_auth import BasicAuthCredentials
from advancedbilling.models.card_type import CardType
from advancedbilling.models.create_subscription import CreateSubscription
from advancedbilling.models.create_subscription_request import CreateSubscriptionRequest
from advancedbilling.models.customer_attributes import CustomerAttributes
from advancedbilling.models.payment_profile_attributes import PaymentProfileAttributes

client = AdvancedBillingClient(
    basic_auth_credentials=BasicAuthCredentials(
        username='BasicAuthUserName',
        password='BasicAuthPassword'
    ),
    environment=Environment.PRODUCTION,
    subdomain='subdomain',
    domain='chargify.com'
)

subscriptions_controller = client.subscriptions
body = CreateSubscriptionRequest(
    subscription=CreateSubscription(
        product_handle='basic',
        customer_attributes=CustomerAttributes(
            first_name='Joe',
            last_name='Blow',
            email='joe@example.com',
            organization='Acme',
            reference='XYZ',
            address='123 Mass Ave.',
            address_2='address_24',
            city='Boston',
            state='MA',
            zip='02120',
            country='US',
            phone='(617) 111 - 0000'
        ),
        credit_card_attributes=PaymentProfileAttributes(
            first_name='Joe',
            last_name='Smith',
            full_number='4111111111111111',
            card_type=CardType.VISA,
            expiration_month='1',
            expiration_year='2021',
            billing_address='123 Mass Ave.',
            billing_address_2='billing_address_22',
            billing_city='Boston',
            billing_state='MA',
            billing_country='US',
            billing_zip='02120'
        )
    )
)

try:
    result = subscriptions_controller.create_subscription(
        body=body
    )

    if result.is_success():
        print(result.body)
    elif result.is_error():
        print(result.errors)

except ErrorListResponseException as e: 
    print(e)
except APIException as e: 
    print(e)

