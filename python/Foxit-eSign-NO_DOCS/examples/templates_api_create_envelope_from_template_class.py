
from foxitesigntest.configuration import Environment
from foxitesigntest.exceptions.api_exception import APIException
from foxitesigntest.foxitesigntest_client import FoxitesigntestClient
from foxitesigntest.http.auth.o_auth_2 import BearerAuthCredentials
from foxitesigntest.models.base_envelopefrom_template import BaseEnvelopefromTemplate
from foxitesigntest.models.party import Party
from foxitesigntest.models.permissions_enum import PermissionsEnum
from foxitesigntest.models.signer_auth_levels_enum import SignerAuthLevelsEnum

client = FoxitesigntestClient(
    bearer_auth_credentials=BearerAuthCredentials(
        access_token='AccessToken'
    ),
    environment=Environment.US_SERVER
)

templates_api_controller = client.templates_api
body = BaseEnvelopefromTemplate(
    template_ids=[
        271591
    ],
    parties=[
        Party(
            first_name='FIRST_NAME_OF_RECIPIENT_PARTY',
            last_name='LAST_NAME_OF_RECIPIENT_PARTY',
            email_id='peter.parker@spiderman.com',
            permission=PermissionsEnum.FILL_FIELDS_AND_SIGN,
            sequence=1,
            signer_auth_level=SignerAuthLevelsEnum.NO,
            allow_name_change='true',
            workflow_sequence=1,
            host_email_id='EMAIL_ID_OF_INPERSON_ADMINISTRATOR'
        ),
        Party(
            first_name='FIRST_NAME_OF_RECIPIENT_PARTY',
            last_name='LAST_NAME_OF_RECIPIENT_PARTY',
            email_id='bruce@batman.com',
            permission=PermissionsEnum.FILL_FIELDS_AND_SIGN,
            sequence=2,
            signer_auth_level=SignerAuthLevelsEnum.NO,
            allow_name_change='true',
            workflow_sequence=2,
            host_email_id='EMAIL_ID_OF_INPERSON_ADMINISTRATOR'
        )
    ],
    folder_name='Testing Flow1',
    allow_advanced_email_validation=False,
    sign_in_sequence=False,
    in_person_enable=False,
    send_now=True,
    sign_success_url_all_parties=False,
    create_embedded_sending_session=True,
    fix_recipient_parties=True,
    fix_documents=True,
    send_success_url='YOUR_PAGE_TO_REDIRECT_USER_FROM_EMBEDDED_SESSION',
    send_error_url='YOUR_PAGE_TO_REDIRECT_USER_FROM_EMBEDDED_SESSION',
    hide_signer_select_option=False,
    hide_signer_actions=False,
    hide_sender_name=True,
    hide_send_button=True,
    hide_folder_name=False,
    hide_documents_name=True,
    hide_add_me_button=False,
    hide_add_new_button=True,
    hide_add_group_button=False,
    create_embedded_signing_session=True,
    create_embedded_signing_session_for_all_parties=False,
    embedded_signers_email_ids=[
        'peter.parker@spiderman.com',
        'bruce@batman.com'
    ],
    sign_success_url='YOUR_PAGE_TO_REDIRECT_USER_FROM_EMBEDDED_SESSION',
    sign_decline_url='YOUR_PAGE_TO_REDIRECT_USER_FROM_EMBEDDED_SESSION',
    sign_later_url='YOUR_PAGE_TO_REDIRECT_USER_FROM_EMBEDDED_SESSION',
    sign_error_url='YOUR_PAGE_TO_REDIRECT_USER_FROM_EMBEDDED_SESSION',
    hide_next_required_field_btn=False,
    theme_color='ANY_CSS_COLOR_TO_MATCH_YOUR_APPLICATION',
    hide_decline_to_sign=False,
    hide_more_action=False,
    hide_add_parties_option=False,
    session_expire=False,
    expiry=300000,
    sender_email='jon.dpe@ggmail.com',
    allow_send_now_and_embedded_signing_session=False,
    enable_step_by_step=False
)

try:
    result = templates_api_controller.create_envelope_from_template(body)

    if result.is_success():
        print(result.body)
    elif result.is_error():
        print(result.errors)

except APIException as e: 
    print(e)

