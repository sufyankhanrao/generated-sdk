import dateutil
import dateutil.parser
import jsonpickle

from testcodesamples.configuration import Environment
from testcodesamples.exceptions.api_exception import APIException
from testcodesamples.models.person import EmployeeOptional
from testcodesamples.testcodesamples_client import TestcodesamplesClient

client = TestcodesamplesClient(
    environment=Environment.TESTING,
    port='80',
    suites=1
)

custom_types_controller = client.custom_types
model = {
    'key0': EmployeeOptional(
        address='address0',
        age=122,
        name='name4',
        uid='uid4',
        department='department8',
        boolean_var=False,
        object_var=jsonpickle.decode('{"key1":"val1","key2":"val2"}'),
        dynamic_var=jsonpickle.decode('{"key1":"val1","key2":"val2"}'),
        date_time_unix_var=dateutil.datetime.utcfromtimestamp(1480809600),
        birthday=dateutil.parser.parse('2016-03-13').date(),
        birthtime=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
        person_type='Empl'
    ),
    'key1': EmployeeOptional(
        address='address0',
        age=122,
        name='name4',
        uid='uid4',
        department='department8',
        boolean_var=False,
        object_var=jsonpickle.decode('{"key1":"val1","key2":"val2"}'),
        dynamic_var=jsonpickle.decode('{"key1":"val1","key2":"val2"}'),
        date_time_unix_var=dateutil.datetime.utcfromtimestamp(1480809600),
        birthday=dateutil.parser.parse('2016-03-13').date(),
        birthtime=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
        person_type='Empl'
    )
}

model_optional = {
    'key0': EmployeeOptional(
        address='address0',
        age=122,
        name='name4',
        uid='uid4',
        department='department0',
        boolean_var=False,
        object_var=jsonpickle.decode('{"key1":"val1","key2":"val2"}'),
        dynamic_var=jsonpickle.decode('{"key1":"val1","key2":"val2"}'),
        date_time_unix_var=dateutil.datetime.utcfromtimestamp(1480809600),
        birthday=dateutil.parser.parse('2016-03-13').date(),
        birthtime=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
        person_type='Empl'
    )
}

try:
    result = custom_types_controller.send_model_in_form_optional(
        model,
        model_optional=model_optional
    )

    if result.is_success():
        print(result.body)
    elif result.is_error():
        print(result.errors)

except APIException as e: 
    print(e)

