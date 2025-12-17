from shellcardmanagementapis.configuration import Environment
from shellcardmanagementapis.exceptions.api_exception import APIException
from shellcardmanagementapis.http.auth.bearer_token import BearerTokenCredentials
from shellcardmanagementapis.models.card_contact import CardContact
from shellcardmanagementapis.models.card_detail import CardDetail
from shellcardmanagementapis.models.card_management_v_1_ordercard_request import CardManagementV1OrdercardRequest
from shellcardmanagementapis.models.pin_contact import PINContact
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

body = CardManagementV1OrdercardRequest(
    card_details=[
        CardDetail(
            card_delivery_type=1,
            pin_advice_type=1,
            payer_id=853,
            payer_number='PH50000843',
            account_id=854,
            account_number='PH50000844',
            col_co_code=86,
            col_co_id=1,
            card_type_id=1,
            token_type_id=107,
            emboss_text='PARKLEY',
            vrn='MV65YLH',
            driver_name='Robert',
            odometer_input_required=False,
            fleet_id_input_required=False,
            purchase_category_id=54,
            self_selected_encrypted_pin='0hCx7wfFp3z8QkW8dElhHiMwCwC1',
            self_selected_pin_key_id='123aaa33198dc8f3s4k77dsc78',
            self_selected_pin_session_key='WoWB+8UEd71+8QXwuE75flkAQ /4Q6gDFSn027oJ/0ne6LmzVIxJ87yoeqKS /C+OIBJ7bTvasLH+xvDSZtzoOZHr 7wfFmpfSyet8KnKjnagSicrUgpGk 7qFyOw3iA9/Qd6Oy9djYR3C3cDWEpj /YREZ1lBGReb9fqdSpoKx8mnGuPAw7',
            card_group_id=5,
            card_group_name='Group1',
            is_new_card_group=False,
            emboss_card_group=False,
            card_contact=CardContact(
                delivery_contact_name='Robert',
                delivery_company_name='WILTON AUFDERHAR',
                delivery_address_line_1='Herrn Dieter Whausen Lansstrab',
                delivery_zip_code='12130',
                delivery_city='manila',
                delivery_country='WILTON AUFDERHAR',
                delivery_contact_title='Mr.',
                delivery_address_line_2='10th avenue',
                delivery_address_line_3='makati city',
                delivery_region_id=43,
                delivery_region='Philippines',
                phone_number='99999999999',
                email_address='xxxxx@example.com',
                save_for_card_reissue=False
            ),
            pin_delivery_address_type=1,
            pin_contact=PINContact(
                delivery_contact_title='Mr.',
                delivery_contact_name='Robert',
                delivery_company_name='WILTON AUFDERHAR',
                delivery_address_line_1='Herrn Dieter Whausen Lansstrab',
                delivery_address_line_2='10th avenue',
                delivery_address_line_3='makati city',
                delivery_zip_code='12130',
                delivery_city='manila',
                delivery_region_id=43,
                delivery_region='Philippines',
                delivery_country='WILTON AUFDERHAR',
                phone_number='99999999999',
                email_address='xxxxx@example.com',
                save_for_pin_reminder=False
            ),
            notify_caller=False,
            caller='NextGenUI',
            notify_caller_on_sync=False,
            validate_fleet_id=False,
            fleet_option='ALERT',
            bundle_id='1046',
            usage_restriction_action='None',
            product_restriction_action='None',
            products=[
                '011',
                '033'
            ],
            product_groups=[
                '670246404',
                '40557126'
            ],
            expiry_date='1221',
            client_reference_id='cli123'
        )
    ]
)

try:
    result = card_controller.cardordercard(
        request_id,
        body=body
    )

    if result.is_success():
        print(result.body)
    elif result.is_error():
        print(result.errors)

except APIException as e: 
    print(e)

