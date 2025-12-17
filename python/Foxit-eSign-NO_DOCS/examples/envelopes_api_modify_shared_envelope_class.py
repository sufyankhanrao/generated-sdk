from foxitesigntest.configuration import Environment
from foxitesigntest.exceptions.api_exception import APIException
from foxitesigntest.foxitesigntest_client import FoxitesigntestClient
from foxitesigntest.http.auth.o_auth_2 import BearerAuthCredentials
from foxitesigntest.models.field import Field
from foxitesigntest.models.modify_shared_envelope import ModifySharedEnvelope
from foxitesigntest.models.party import Party
from foxitesigntest.models.permissions_enum import PermissionsEnum

client = FoxitesigntestClient(
    bearer_auth_credentials=BearerAuthCredentials(
        access_token='AccessToken'
    ),
    environment=Environment.US_SERVER
)

envelopes_api_controller = client.envelopes_api
body = ModifySharedEnvelope(
    folder_id=2520579,
    folder_name='eSignature Document',
    parties=[
        Party(
            first_name='John',
            last_name='Doe',
            email_id='john.doe@example.com',
            permission=PermissionsEnum.FILL_FIELDS_AND_SIGN,
            sequence=1
        )
    ],
    create_embedded_signing_session=True,
    fields=[
        Field()
    ],
    send_now=True,
    sign_in_sequence=False,
    in_person_enable=False,
    fix_recipient_parties=False,
    fix_documents=False,
    create_embedded_sending_session=False,
    embedded_signers_email_ids=[
        'peter@ggmail.com',
        'spidey@ggmail.com'
    ],
    allow_send_now_and_embedded_signing_session=False,
    allow_advanced_email_validation=False,
    sign_success_url_all_parties=False,
    email_template_id=3,
    signer_instruction_id=2,
    confirmation_instruction_id=4,
    session_expire=False,
    sender_email='"user2@example.com"',
    create_executed_folder=False,
    hide_add_me_button=False,
    hide_add_new_button=False,
    hide_add_group_button=False,
    hide_field_name_for_recipients=False,
    hide_checkbox_border=False,
    hide_signer_select_option=False,
    hide_signer_actions=False,
    hide_sender_name=False,
    hide_folder_name=False,
    hide_documents_name=False,
    hide_decline_to_sign=False,
    hide_more_action=False,
    hide_send_button=False,
    hide_next_required_fieldbtn=False,
    enable_step_by_step=False
)

try:
    result = envelopes_api_controller.modify_shared_envelope(body)

    if result.is_success():
        print(result.body)
    elif result.is_error():
        print(result.errors)

except APIException as e: 
    print(e)

