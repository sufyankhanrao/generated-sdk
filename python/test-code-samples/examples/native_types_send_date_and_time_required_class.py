import dateutil
import dateutil.parser

from testcodesamples.api_helper import APIHelper
from testcodesamples.configuration import Environment
from testcodesamples.exceptions.api_exception import APIException
from testcodesamples.testcodesamples_client import TestcodesamplesClient

client = TestcodesamplesClient(
    environment=Environment.TESTING,
    port='80',
    suites=1
)

native_types_controller = client.native_types
unix_date_time_var = dateutil.datetime.utcfromtimestamp(1480809600)

rfc_1123_date_time_var = APIHelper.HttpDateTime.from_value('Mon, 15 Jun 2009 20:45:30 GMT').datetime

rfc_3339_date_time = dateutil.parser.parse('2016-03-13T12:52:32.123Z')

date_var = dateutil.parser.parse('2016-03-13').date()

try:
    result = native_types_controller.send_date_and_time_required(
        unix_date_time_var,
        rfc_1123_date_time_var,
        rfc_3339_date_time,
        date_var
    )
    print(result)
except APIException as e: 
    print(e)

