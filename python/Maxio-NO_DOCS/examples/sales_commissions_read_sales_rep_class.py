from advancedbilling.advanced_billing_client import AdvancedBillingClient
from advancedbilling.configuration import Environment
from advancedbilling.exceptions.api_exception import APIException
from advancedbilling.http.auth.basic_auth import BasicAuthCredentials

client = AdvancedBillingClient(
    basic_auth_credentials=BasicAuthCredentials(
        username='BasicAuthUserName',
        password='BasicAuthPassword'
    ),
    environment=Environment.PRODUCTION,
    subdomain='subdomain',
    domain='chargify.com'
)

sales_commissions_controller = client.sales_commissions
seller_id = 'seller_id8'

sales_rep_id = 'sales_rep_id4'

authorization = 'Bearer <<apiKey>>'

page = 2

per_page = 100

try:
    result = sales_commissions_controller.read_sales_rep(
        seller_id,
        sales_rep_id,
        authorization=authorization,
        page=page,
        per_page=per_page
    )

    if result.is_success():
        print(result.body)
    elif result.is_error():
        print(result.errors)

except APIException as e: 
    print(e)

