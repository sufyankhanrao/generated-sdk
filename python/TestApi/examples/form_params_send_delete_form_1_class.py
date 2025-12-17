import dateutil.parser

from tester.api_helper import APIHelper
from tester.configuration import Environment
from tester.exceptions.api_exception import APIException
from tester.exceptions.custom_error_response_exception import CustomErrorResponseException
from tester.exceptions.exception_with_boolean_exception import ExceptionWithBooleanException
from tester.exceptions.exception_with_date_exception import ExceptionWithDateException
from tester.exceptions.exception_with_dynamic_exception import ExceptionWithDynamicException
from tester.exceptions.exception_with_long_exception import ExceptionWithLongException
from tester.exceptions.exception_with_number_exception import ExceptionWithNumberException
from tester.exceptions.exception_with_precision_exception import ExceptionWithPrecisionException
from tester.exceptions.exception_with_rfc_3339_date_time_exception import ExceptionWithRfc3339DateTimeException
from tester.exceptions.exception_with_string_exception import ExceptionWithStringException
from tester.exceptions.exception_with_uuid_exception import ExceptionWithUUIDException
from tester.exceptions.global_test_exception import GlobalTestException
from tester.exceptions.nested_model_exception import NestedModelException
from tester.exceptions.rfc_1123_exception import Rfc1123Exception
from tester.exceptions.send_boolean_in_model_as_exception import SendBooleanInModelAsException
from tester.exceptions.send_date_in_model_as_exception import SendDateInModelAsException
from tester.exceptions.send_dynamic_in_model_as_exception import SendDynamicInModelAsException
from tester.exceptions.send_long_in_model_as_exception import SendLongInModelAsException
from tester.exceptions.send_number_in_model_as_exception import SendNumberInModelAsException
from tester.exceptions.send_precision_in_model_as_exception import SendPrecisionInModelAsException
from tester.exceptions.send_rfc_1123_in_model_as_exception import SendRfc1123InModelAsException
from tester.exceptions.send_rfc_3339_in_model_as_exception import SendRfc3339InModelAsException
from tester.exceptions.send_string_in_model_as_exception import SendStringInModelAsException
from tester.exceptions.send_unix_time_stamp_in_model_as_exception import SendUnixTimeStampInModelAsException
from tester.exceptions.send_uuid_in_model_as_exception import SendUuidInModelAsException
from tester.exceptions.unix_time_stamp_exception import UnixTimeStampException
from tester.models.days_1_enum import Days1Enum
from tester.models.days_enum import DaysEnum
from tester.models.person import Employee
from tester.models.person import Person
from tester.models.suite_code_enum import SuiteCodeEnum
from tester.tester_client import TesterClient

client = TesterClient(
    environment=Environment.TESTING,
    port='80',
    suites=SuiteCodeEnum.HEARTS
)

form_params_controller = client.form_params
model = Employee(
    address='address0',
    age=122,
    birthday=dateutil.parser.parse('2016-03-13').date(),
    birthtime=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
    name='name4',
    uid='uid4',
    department='department8',
    dependents=[
        Person(
            address='address4',
            age=28,
            birthday=dateutil.parser.parse('2016-03-13').date(),
            birthtime=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
            name='name8',
            uid='uid8',
            person_type='Per'
        )
    ],
    hired_at=APIHelper.HttpDateTime.from_value('Mon, 15 Jun 2009 20:45:30 GMT').datetime,
    joining_day=Days1Enum.MONDAY,
    salary=240,
    working_days=[
        DaysEnum.FRI_DAY,
        DaysEnum.THURSDAY,
        DaysEnum.WEDNESDAY_
    ],
    boss=Person(
        address='address8',
        age=94,
        birthday=dateutil.parser.parse('2016-03-13').date(),
        birthtime=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
        name='name2',
        uid='uid2',
        person_type='Per'
    ),
    person_type='Empl'
)

try:
    result = form_params_controller.send_delete_form_1(model)

    if result.is_success():
        print(result.body)
    elif result.is_error():
        print(result.errors)

except NestedModelException as e: 
    print(e)
except CustomErrorResponseException as e: 
    print(e)
except ExceptionWithStringException as e: 
    print(e)
except ExceptionWithBooleanException as e: 
    print(e)
except ExceptionWithDynamicException as e: 
    print(e)
except ExceptionWithUUIDException as e: 
    print(e)
except ExceptionWithDateException as e: 
    print(e)
except ExceptionWithNumberException as e: 
    print(e)
except ExceptionWithLongException as e: 
    print(e)
except ExceptionWithPrecisionException as e: 
    print(e)
except ExceptionWithRfc3339DateTimeException as e: 
    print(e)
except UnixTimeStampException as e: 
    print(e)
except Rfc1123Exception as e: 
    print(e)
except SendBooleanInModelAsException as e: 
    print(e)
except SendRfc3339InModelAsException as e: 
    print(e)
except SendRfc1123InModelAsException as e: 
    print(e)
except SendUnixTimeStampInModelAsException as e: 
    print(e)
except SendDateInModelAsException as e: 
    print(e)
except SendDynamicInModelAsException as e: 
    print(e)
except SendStringInModelAsException as e: 
    print(e)
except SendLongInModelAsException as e: 
    print(e)
except SendNumberInModelAsException as e: 
    print(e)
except SendPrecisionInModelAsException as e: 
    print(e)
except SendUuidInModelAsException as e: 
    print(e)
except GlobalTestException as e: 
    print(e)
except APIException as e: 
    print(e)

