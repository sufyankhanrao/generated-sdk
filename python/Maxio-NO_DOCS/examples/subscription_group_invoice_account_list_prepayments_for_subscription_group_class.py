import dateutil.parser

from advancedbilling.advanced_billing_client import AdvancedBillingClient
from advancedbilling.configuration import Environment
from advancedbilling.exceptions.api_exception import APIException
from advancedbilling.http.auth.basic_auth import BasicAuthCredentials
from advancedbilling.models.list_prepayment_date_field import ListPrepaymentDateField
from advancedbilling.models.list_prepayments_filter import ListPrepaymentsFilter

client = AdvancedBillingClient(
    basic_auth_credentials=BasicAuthCredentials(
        username='BasicAuthUserName',
        password='BasicAuthPassword'
    ),
    environment=Environment.PRODUCTION,
    subdomain='subdomain',
    domain='chargify.com'
)

subscription_group_invoice_account_controller = client.subscription_group_invoice_account
collect = {
    'uid': 'uid0',
    'page': 2,
    'per_page': 50,
    'filter': ListPrepaymentsFilter(
        date_field=ListPrepaymentDateField.CREATED_AT,
        start_date=dateutil.parser.parse('2024-01-01').date(),
        end_date=dateutil.parser.parse('2024-01-31').date()
    )
}
try:
    result = subscription_group_invoice_account_controller.list_prepayments_for_subscription_group(collect)

    if result.is_success():
        print(result.body)
    elif result.is_error():
        print(result.errors)

except APIException as e: 
    print(e)

