from foxitesigntest.configuration import Environment
from foxitesigntest.exceptions.api_exception import APIException
from foxitesigntest.foxitesigntest_client import FoxitesigntestClient
from foxitesigntest.models.content_type_enum import ContentTypeEnum
from foxitesigntest.models.grant_type_enum import GrantTypeEnum
from foxitesigntest.models.scope_enum import ScopeEnum

client = FoxitesigntestClient(
    environment=Environment.US_SERVER
)

authentication_api_controller = client.authentication_api
content_type = ContentTypeEnum.ENUM_APPLICATIONXWWWFORMURLENCODED

client_id = 'client_id8'

client_secret = 'client_secret8'

grant_type = GrantTypeEnum.CLIENT_CREDENTIALS

scope = ScopeEnum.READWRITE

try:
    result = authentication_api_controller.generate_access_token(
        content_type,
        client_id,
        client_secret,
        grant_type,
        scope
    )

    if result.is_success():
        print(result.body)
    elif result.is_error():
        print(result.errors)

except APIException as e: 
    print(e)

