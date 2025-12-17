from shellcardmanagementapis.configuration import Environment
from shellcardmanagementapis.exceptions.api_exception import APIException
from shellcardmanagementapis.exceptions.error_object_exception import ErrorObjectException
from shellcardmanagementapis.http.auth.bearer_token import BearerTokenCredentials
from shellcardmanagementapis.models.card_management_v_1_pinreminder_request import CardManagementV1PinreminderRequest
from shellcardmanagementapis.models.pin_deliver_to import PINDeliverTo
from shellcardmanagementapis.models.pin_reminder_card_details import PINReminderCardDetails
from shellcardmanagementapis.shell_card_management_ap_is_client import ShellCardManagementApIsClient

client = ShellCardManagementApIsClient(
    bearer_token_credentials=BearerTokenCredentials(
        o_auth_client_id='OAuthClientId',
        o_auth_client_secret='OAuthClientSecret'
    ),
    environment=Environment.SIT
)

card_controller = client.card
request_id = 'RequestId8'

body = CardManagementV1PinreminderRequest(
    account_number='CZ00000927',
    col_co_code=32,
    payer_number='CZ00000927',
    pin_reminder_card_details=[
        PINReminderCardDetails(
            pin_advice_type=1,
            card_id=463402,
            pan='7027329200000115820',
            card_expiry_date='20241031',
            pin_contact_type=4,
            pin_deliver_to=PINDeliverTo(
                company_name='CGI',
                address_line='Address1',
                zip_code='938373',
                city='City1',
                contact_name='Alex',
                contact_title='Mr',
                region_id=0,
                country_id=0,
                phone_number='9998883332',
                email_address='abc.gmail.com',
                save_pin_reminder=False
            )
        )
    ]
)

try:
    result = card_controller.cardpinreminder(
        request_id,
        body=body
    )

    if result.is_success():
        print(result.body)
    elif result.is_error():
        print(result.errors)

except ErrorObjectException as e: 
    print(e)
except APIException as e: 
    print(e)

