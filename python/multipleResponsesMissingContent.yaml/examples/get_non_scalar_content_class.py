from multipleresponsesmissingcontent.configuration import Environment
from multipleresponsesmissingcontent.exceptions.api_exception import APIException
from multipleresponsesmissingcontent.multipleresponsesmissingcontent_client import MultipleresponsesmissingcontentClient

client = MultipleresponsesmissingcontentClient(
    environment=Environment.PRODUCTION
)

client_controller = client.client
try:
    result = client_controller.get_non_scalar_content()
    print(result)
except APIException as e: 
    print(e)

