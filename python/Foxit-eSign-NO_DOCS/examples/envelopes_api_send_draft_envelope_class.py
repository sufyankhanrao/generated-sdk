import jsonpickle

from foxitesigntest.configuration import Environment
from foxitesigntest.exceptions.api_exception import APIException
from foxitesigntest.foxitesigntest_client import FoxitesigntestClient
from foxitesigntest.http.auth.o_auth_2 import BearerAuthCredentials
from foxitesigntest.models.draft_envelope import DraftEnvelope
from foxitesigntest.models.party import Party
from foxitesigntest.models.permissions_enum import PermissionsEnum

client = FoxitesigntestClient(
    bearer_auth_credentials=BearerAuthCredentials(
        access_token='AccessToken'
    ),
    environment=Environment.US_SERVER
)

envelopes_api_controller = client.envelopes_api
body = DraftEnvelope(
    folder_id=2520579,
    folder_name='Example Documents',
    parties=[
        Party(
            first_name='John',
            last_name='Doe',
            email_id='john.doe@example.com',
            permission=PermissionsEnum.FILL_FIELDS_AND_SIGN,
            sequence=1
        )
    ],
    sign_in_sequence=False,
    in_person_enable=False,
    fields=[
        jsonpickle.decode('{"type":"text","name":"Signer Name","x":108,"y":500,"width":60,"height":20,"documentNumber":1,"pageNumber":1,"tabOrder":1,"party":1,"tooltip":"","required":true,"characterLimit":100,"fontSize":12,"fontColor":"#000000","hideFieldNameForRecipients":false}'),
        jsonpickle.decode('{"type":"date","x":336,"y":500,"width":60,"height":20,"documentNumber":1,"pageNumber":1,"tabOrder":1,"party":1,"name":"Date","required":true,"fontSize":12,"dateFormat":"MM-DD-YYYY"}'),
        jsonpickle.decode('{"type":"signature","x":108,"y":565,"width":60,"height":20,"documentNumber":1,"pageNumber":1,"party":1,"required":true}'),
        jsonpickle.decode('{"type":"date","x":336,"y":565,"width":60,"height":20,"documentNumber":1,"pageNumber":1,"tabOrder":1,"party":1,"name":"Date Signed","required":true,"fontSize":12,"dateFormat":"MM-DD-YYYY","readOnly":true,"systemField":true}')
    ],
    send_now=True,
    create_embedded_signing_session=True,
    embedded_signers_email_ids=[
        'peter@ggmail.com',
        'spidey@ggmail.com'
    ],
    allow_send_now_and_embedded_signing_session=False,
    allow_advanced_email_validation=False,
    sign_success_url_all_parties=False,
    email_template_id=2,
    signer_instruction_id=1,
    confirmation_instruction_id=3,
    session_expire=False,
    sender_email='"user2@example.com"',
    create_executed_folder=False,
    hide_field_name_for_recipients=False,
    hide_checkbox_border=False,
    hide_decline_to_sign=False,
    hide_more_action=False,
    hide_next_required_fieldbtn=False
)

try:
    result = envelopes_api_controller.send_draft_envelope(body)

    if result.is_success():
        print(result.body)
    elif result.is_error():
        print(result.errors)

except APIException as e: 
    print(e)

