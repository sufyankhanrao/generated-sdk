from shellcardmanagementapis.configuration import Environment
from shellcardmanagementapis.exceptions.api_exception import APIException
from shellcardmanagementapis.http.auth.basic_auth import BasicAuthCredentials
from shellcardmanagementapis.models.create_card_group_request import CreateCardGroupRequest
from shellcardmanagementapis.models.create_card_group_request_cards_items import CreateCardGroupRequestCardsItems
from shellcardmanagementapis.shell_card_management_ap_is_client import ShellCardManagementApIsClient

client = ShellCardManagementApIsClient(
    basic_auth_credentials=BasicAuthCredentials(
        username='Username',
        password='Password'
    ),
    environment=Environment.SIT
)

customer_controller = client.customer
apikey = 'apikey6'

request_id = 'RequestId8'

body = CreateCardGroupRequest(
    col_co_code=86,
    col_co_id=1,
    payer_number='PH50000843',
    payer_id=853,
    account_id=854,
    account_number='PH50000844',
    print_on_card=True,
    card_group_name='GROUP1',
    cards=[
        CreateCardGroupRequestCardsItems(
            account_id=123,
            account_number='ACC123',
            card_id=123,
            pan='ABC12345672'
        )
    ]
)

try:
    result = customer_controller.createcardgroup(
        apikey,
        request_id,
        body=body
    )

    if result.is_success():
        print(result.body)
    elif result.is_error():
        print(result.errors)

except APIException as e: 
    print(e)

