from foxitesigntest.configuration import Environment
from foxitesigntest.exceptions.api_exception import APIException
from foxitesigntest.foxitesigntest_client import FoxitesigntestClient
from foxitesigntest.http.auth.o_auth_2 import BearerAuthCredentials
from pathlib import Path

from foxitesigntest.utilities.file_wrapper import FileWrapper

client = FoxitesigntestClient(
    bearer_auth_credentials=BearerAuthCredentials(
        access_token='AccessToken'
    ),
    environment=Environment.US_SERVER
)

envelopes_api_controller = client.envelopes_api
file = FileWrapper(Path('dummy_file').open('rb'), 'optional-content-type')

data = '{\n   "folderName":"onboardingmulti_2.pdf",\n      "parties":[\n      {\n         "firstName":"Signer",\n         "lastName":"1",\n         "emailId":"jorgeluceda+101@gmail.com",\n         "permission":"FILL_FIELDS_AND_SIGN",\n         "sequence":1,\n         "allowNameChange":false\n      }\n   ],\n   "fields":[\n      {\n         "type":"text",\n         "x":348,\n         "y":157,\n         "width":171,\n         "height":28,\n         "pageNumber":1,\n         "documentNumber":1,\n         "hideFieldNameForRecipients": true,\n         "name":"Number(fillable) d0107804-ce35-45e8-8d06-a26d67f0d9bd",\n         "tooltip":"First Name",\n         "value":"",\n         "required":false,\n         "characterLimit":100,\n         "party":1,\n         "fontSize":12,\n         "fontColor":"#000000",\n         "options":[\n            "None"\n         ],\n         "tabOrder":1\n      },\n    {\n         "type":"text",\n         "x":348,\n         "y":257,\n         "width":171,\n         "height":28,\n         "pageNumber":1,\n         "documentNumber":1,\n         "hideFieldNameForRecipients": true,\n         "name":"Number(fillable) d0107804-ce35-45e8-8d06-a26d67a1e9ee",\n         "tooltip":"Last Name",\n         "value":"",\n         "required":false,\n         "characterLimit":100,\n         "party":1,\n         "fontSize":12,\n         "fontColor":"#000000",\n         "options":[\n            "None"\n         ],\n         "tabOrder":2\n      },\n        {\n            "type":"checkbox",\n            "x":348,\n            "y":357,\n            "width":13,\n            "height":13,\n            "pageNumber":1,\n            "documentNumber":1,\n            "name":"isBorn",\n            "tooltip":"First child?",\n            "required":false,\n            "party":1,\n            "group":null,\n            "multicheck":true,\n            "checked": true,\n            "tabOrder":3,\n            "hideCheckboxBorder": true\n        },\n        {\n            "type":"date",\n            "x":348,\n            "y":457,\n            "width":60,\n            "height":13,\n            "pageNumber":1,\n            "documentNumber":1,\n            "tooltip":"Date this is signed",\n            "required":true,\n            "party":1,\n            "name": "exampleDateField",\n            "hideFieldNameForRecipients": true,\n            "value": "",\n            "dateFormat": "MM-DD-YYYY"\n        }\n   ],\n   "sendNow": true,\n   "createEmbeddedSigningSession": true,\n   "createEmbeddedSigningSessionForAllParties": true\n}'

try:
    result = envelopes_api_controller.create_envelope_from_binary(
        file,
        data
    )

    if result.is_success():
        print(result.body)
    elif result.is_error():
        print(result.errors)

except APIException as e: 
    print(e)

