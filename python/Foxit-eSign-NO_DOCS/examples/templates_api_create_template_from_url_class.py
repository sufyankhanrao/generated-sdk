import jsonpickle

from foxitesigntest.configuration import Environment
from foxitesigntest.exceptions.api_exception import APIException
from foxitesigntest.foxitesigntest_client import FoxitesigntestClient
from foxitesigntest.http.auth.o_auth_2 import BearerAuthCredentials
from foxitesigntest.models.permissions_enum import PermissionsEnum
from foxitesigntest.models.template_party import TemplateParty
from foxitesigntest.models.url_template import URLTemplate

client = FoxitesigntestClient(
    bearer_auth_credentials=BearerAuthCredentials(
        access_token='AccessToken'
    ),
    environment=Environment.US_SERVER
)

templates_api_controller = client.templates_api
body = URLTemplate(
    template_name='onboardingmulti_2.pdf',
    template_url='https://developers.esigngenie.com/uploads/eSignGenieAPISampleDoc.pdf',
    process_text_tags=True,
    process_acro_fields=True,
    share_all=False,
    number_of_parties=2,
    parties=[
        TemplateParty(
            permission=PermissionsEnum.FILL_FIELDS_AND_SIGN,
            sequence=1,
            party_role='Manager'
        ),
        TemplateParty(
            permission=PermissionsEnum.FILL_FIELDS_AND_SIGN,
            sequence=2,
            party_role='Manager 2'
        )
    ],
    input_type='url',
    theme_color='#42caf4',
    author_email='jon.doe@ggmail.com',
    create_embedded_template_session=True,
    fields=[
        jsonpickle.decode('{"type":"text","x":348,"y":157,"width":171,"height":28,"pageNumber":1,"documentNumber":1,"hideFieldNameForRecipients":true,"name":"Number(fillable) d0107804-ce35-45e8-8d06-a26d67f0d9bd","tooltip":"First Name","value":"","required":false,"characterLimit":100,"party":1,"fontSize":12,"fontColor":"#000000","options":["None"],"tabOrder":1}'),
        jsonpickle.decode('{"type":"text","x":348,"y":257,"width":171,"height":28,"pageNumber":1,"documentNumber":1,"hideFieldNameForRecipients":true,"name":"Number(fillable) d0107804-ce35-45e8-8d06-a26d67a1e9ee","tooltip":"Last Name","value":"","required":false,"characterLimit":100,"party":1,"fontSize":12,"fontColor":"#000000","options":["None"],"tabOrder":2}'),
        jsonpickle.decode('{"type":"checkbox","x":348,"y":357,"width":13,"height":13,"pageNumber":1,"documentNumber":1,"name":"isBorn","tooltip":"First child?","required":false,"party":1,"group":null,"multicheck":true,"checked":true,"tabOrder":3,"hideCheckboxBorder":true}'),
        jsonpickle.decode('{"type":"date","x":348,"y":457,"width":60,"height":13,"pageNumber":1,"documentNumber":1,"tooltip":"Date this is signed","required":true,"party":1,"name":"exampleDateField","hideFieldNameForRecipients":true,"value":"","dateFormat":"MM-DD-YYYY"}')
    ]
)

try:
    result = templates_api_controller.create_template_from_url(body)

    if result.is_success():
        print(result.body)
    elif result.is_error():
        print(result.errors)

except APIException as e: 
    print(e)

