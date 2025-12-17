from shellcardmanagementapis.configuration import Environment
from shellcardmanagementapis.exceptions.api_exception import APIException
from shellcardmanagementapis.http.auth.basic_auth import BasicAuthCredentials
from shellcardmanagementapis.models.delivery_address_update import DeliveryAddressUpdate
from shellcardmanagementapis.models.delivery_address_update_request import DeliveryAddressUpdateRequest
from shellcardmanagementapis.models.update_card_renewal_address_2 import UpdateCardRenewalAddress2
from shellcardmanagementapis.shell_card_management_ap_is_client import ShellCardManagementApIsClient

client = ShellCardManagementApIsClient(
    basic_auth_credentials=BasicAuthCredentials(
        username='Username',
        password='Password'
    ),
    environment=Environment.SIT
)

card_controller = client.card
apikey = 'apikey6'

body = DeliveryAddressUpdateRequest(
    col_co_id=5,
    col_co_code=5,
    payer_id=123456,
    payer_number='GB000000123',
    account_id=12356,
    account_number='GB000000124',
    delivery_address_updates=[
        DeliveryAddressUpdate(
            use_customer_default_address=True,
            card_id=123,
            pan='7002051006629889654',
            card_expiry_date='20170930',
            update_card_renewal_address=UpdateCardRenewalAddress2(
                contact_name='Jack',
                company_name='Travel Transport',
                address_line='Elm Street 11',
                zip_code='1023EA',
                country_id=8,
                contact_title='Mr',
                city='London',
                region_id=2,
                email_address='testmail@gmail.com',
                phone_number='+99999999999'
            )
        )
    ]
)

try:
    result = card_controller.deliveryaddressupdate(
        apikey,
        body=body
    )

    if result.is_success():
        print(result.body)
    elif result.is_error():
        print(result.errors)

except APIException as e: 
    print(e)

