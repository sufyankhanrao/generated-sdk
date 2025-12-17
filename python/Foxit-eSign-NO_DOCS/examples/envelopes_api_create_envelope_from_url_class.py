import jsonpickle

from foxitesigntest.configuration import Environment
from foxitesigntest.exceptions.api_exception import APIException
from foxitesigntest.foxitesigntest_client import FoxitesigntestClient
from foxitesigntest.http.auth.o_auth_2 import BearerAuthCredentials
from foxitesigntest.models.party import Party
from foxitesigntest.models.permissions_enum import PermissionsEnum
from foxitesigntest.models.url_envelope import URLEnvelope

client = FoxitesigntestClient(
    bearer_auth_credentials=BearerAuthCredentials(
        access_token='AccessToken'
    ),
    environment=Environment.US_SERVER
)

envelopes_api_controller = client.envelopes_api
body = URLEnvelope(
    folder_name='Foxit eSign Contract.pdf',
    file_urls=[
        'https://www.esigngenie.com/wp-content/uploads/2022/04/Orange.pdf'
    ],
    file_names=[
        'Foxit eSign Contract.pdf'
    ],
    parties=[
        Party(
            first_name='Peter',
            last_name='Parker',
            email_id='spiderman@demo.com',
            permission=PermissionsEnum.FILL_FIELDS_AND_SIGN,
            sequence=1,
            allow_name_change='false'
        )
    ],
    create_embedded_signing_session=True,
    process_text_tags=False,
    process_acro_fields=False,
    input_type='url',
    fields=[
        jsonpickle.decode('{"type":"text","name":"Signer Name","x":108,"y":500,"width":60,"height":20,"documentNumber":1,"pageNumber":1,"tabOrder":1,"party":1,"tooltip":"","required":true,"characterLimit":100,"fontSize":12,"fontColor":"#000000","hideFieldNameForRecipients":false}'),
        jsonpickle.decode('{"type":"date","x":336,"y":500,"width":60,"height":20,"documentNumber":1,"pageNumber":1,"tabOrder":1,"party":1,"name":"Date","required":true,"fontSize":12,"dateFormat":"MM-DD-YYYY"}'),
        jsonpickle.decode('{"type":"signature","x":108,"y":565,"width":60,"height":20,"documentNumber":1,"pageNumber":1,"party":1,"required":true}'),
        jsonpickle.decode('{"type":"date","x":336,"y":565,"width":60,"height":20,"documentNumber":1,"pageNumber":1,"tabOrder":1,"party":1,"name":"Date Signed","required":true,"fontSize":12,"dateFormat":"MM-DD-YYYY","readOnly":true,"systemField":true}')
    ],
    send_now=True,
    create_embedded_signing_session_for_all_parties=True
)

try:
    result = envelopes_api_controller.create_envelope_from_url(body)

    if result.is_success():
        print(result.body)
    elif result.is_error():
        print(result.errors)

except APIException as e: 
    print(e)

