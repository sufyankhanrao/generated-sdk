from reportingapi.configuration import Environment
from reportingapi.exceptions.api_exception import APIException
from reportingapi.exceptions.error_response_error_3_exception import ErrorResponseError3Exception
from reportingapi.reportingapi_client import ReportingapiClient

client = ReportingapiClient(
    environment=Environment.PRODUCTION
)

isc_details_controller = client.isc_details
try:
    result = isc_details_controller.get_list_of_independent_sales_channel()

    if result.is_success():
        print(result.body)
    elif result.is_error():
        print(result.errors)

except ErrorResponseError3Exception as e: 
    print(e)
except APIException as e: 
    print(e)

