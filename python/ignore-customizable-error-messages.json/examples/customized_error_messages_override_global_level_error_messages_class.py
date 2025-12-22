from customizableerrormessages.configuration import Environment
from customizableerrormessages.customizableerrormessages_client import CustomizableerrormessagesClient
from customizableerrormessages.exceptions.api_exception import APIException
from customizableerrormessages.exceptions.error_model_1_exception import ErrorModel1Exception
from customizableerrormessages.exceptions.error_model_2_exception import ErrorModel2Exception
from customizableerrormessages.exceptions.error_model_3_exception import ErrorModel3Exception

client = CustomizableerrormessagesClient(
    environment=Environment.PRODUCTION
)

customized_error_messages_controller = client.customized_error_messages
try:
    result = customized_error_messages_controller.override_global_level_error_messages()

    if result.is_success():
        print(result.body)
    elif result.is_error():
        print(result.errors)

except ErrorModel2Exception as e: 
    print(e)
except ErrorModel1Exception as e: 
    print(e)
except ErrorModel3Exception as e: 
    print(e)
except APIException as e: 
    print(e)

