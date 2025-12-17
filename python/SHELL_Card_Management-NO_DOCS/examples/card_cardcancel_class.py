from shellcardmanagementapis.configuration import Environment
from shellcardmanagementapis.exceptions.api_exception import APIException
from shellcardmanagementapis.exceptions.error_object_exception import ErrorObjectException
from shellcardmanagementapis.http.auth.bearer_token import BearerTokenCredentials
from shellcardmanagementapis.models.card_management_v_1_cancel_request import CardManagementV1CancelRequest
from shellcardmanagementapis.models.card_settings import CardSettings
from shellcardmanagementapis.models.update_card import UpdateCard
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

body = CardManagementV1CancelRequest(
    cards=[
        UpdateCard(
            caller='NextGenUI',
            is_replacement_chargeable=True,
            notify_caller=False,
            notify_caller_on_sync=False,
            order_card_replacement=True,
            card_settings=CardSettings(
                card_delivery_type=1,
                self_selected_encrypted_pin='0hCx7wfFp3z8QkW8dElhHiMwCwC1',
                self_selected_pin_key_id='123aaa33198dc8f3s4k77dsc78',
                self_selected_pin_session_key='WoWB+8UEd71+8QXwuE75flkAQ /4Q6gDFSn027oJ/0ne6LmzVIxJ87yoeqKS /C+OIBJ7bTvasLH+xvDSZtzoOZHr 7wfFmpfSyet8KnKjnagSicrUgpGk 7qFyOw3iA9/Qd6Oy9djYR3C3cDWEpj /YREZ1lBGReb9fqdSpoKx8mnGuPAw7',
                validate_fleet_id=False,
                card_group_id=156,
                delivery_contact_title='Mr',
                delivery_contact_name='SAPE',
                delivery_company_name='welcome',
                delivery_address_line_1='123/89',
                delivery_address_line_2='Mac Street',
                delivery_address_line_3='NLStrret',
                delivery_zip_code='1213242',
                delivery_city='Chennai',
                delivery_region_id=54,
                delivery_region='Mountain Province',
                delivery_country='CZ',
                phone_number='99999999999',
                email_address='xxxxx@examp"le.com',
                pin_delivery_address_type=1,
                pin_advice_type=1,
                pin_delivery_contact_title='5058F1AF',
                pin_delivery_contact_name='WILTON',
                pin_delivery_company_name='WILTON AUFDERHAR',
                pin_delivery_address_line_1='Herrn Dieter Whausen Lansstrab',
                pin_delivery_address_line_2='Wall street',
                pin_delivery_address_line_3='Wall Street',
                pin_delivery_zip_code='12103',
                pin_delivery_city='Berlin',
                pin_delivery_region_id=1,
                pin_delivery_region='Berlin-Brandenburg',
                pin_delivery_country='DEU',
                pin_phone_number='99999999999',
                pin_email_address='xxxxx@example.com',
                save_for_pin_reminder=False,
                save_for_card_reissue=False,
                expiry_date='1221'
            ),
            account_id=854,
            account_number='PH50000844',
            card_expiry_date='20181031',
            card_id=125,
            col_co_code=86,
            col_co_id=1,
            pan='7002861007636000020',
            payer_id=853,
            payer_number='PH50000843'
        )
    ],
    reason_text='Lost'
)

try:
    result = card_controller.cardcancel(
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

