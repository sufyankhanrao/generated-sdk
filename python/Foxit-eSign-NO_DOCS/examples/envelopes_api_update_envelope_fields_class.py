import jsonpickle

from foxitesigntest.configuration import Environment
from foxitesigntest.exceptions.api_exception import APIException
from foxitesigntest.foxitesigntest_client import FoxitesigntestClient
from foxitesigntest.http.auth.o_auth_2 import BearerAuthCredentials
from foxitesigntest.models.envelope_fields_update import EnvelopeFieldsUpdate

client = FoxitesigntestClient(
    bearer_auth_credentials=BearerAuthCredentials(
        access_token='AccessToken'
    ),
    environment=Environment.US_SERVER
)

envelopes_api_controller = client.envelopes_api
body = EnvelopeFieldsUpdate(
    folder_id=96,
    fields=jsonpickle.decode('{"FIELD1_NAME":"VALUE","FIELD2_NAME":"VALUE"}')
)

try:
    result = envelopes_api_controller.update_envelope_fields(body)

    if result.is_success():
        print(result.body)
    elif result.is_error():
        print(result.errors)

except APIException as e: 
    print(e)

