import dateutil
import dateutil.parser
import jsonpickle

from testcodesamples.api_helper import APIHelper
from testcodesamples.configuration import Environment
from testcodesamples.exceptions.api_exception import APIException
from testcodesamples.models.person import EmployeeRequired
from testcodesamples.models.person import Person
from testcodesamples.testcodesamples_client import TestcodesamplesClient

client = TestcodesamplesClient(
    environment=Environment.TESTING,
    port='80',
    suites=1
)

custom_types_controller = client.custom_types
employee_array_of_map = EmployeeRequired(
    address='address0',
    age=122,
    name='name4',
    uid='uid4',
    department='department8',
    boolean_var=False,
    object_var=jsonpickle.decode('{"key1":"val1","key2":"val2"}'),
    dynamic_var=jsonpickle.decode('{"key1":"val1","key2":"val2"}'),
    date_time_unix_var=dateutil.datetime.utcfromtimestamp(1480809600),
    r_fc_1123_var=APIHelper.HttpDateTime.from_value('Mon, 15 Jun 2009 20:45:30 GMT').datetime,
    r_fc_3339_var=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
    date_var=dateutil.parser.parse('2016-03-13').date(),
    dependents=[
        Person(
            address='address4',
            age=28,
            name='name8',
            uid='uid8',
            birthday=dateutil.parser.parse('2016-03-13').date(),
            birthtime=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
            person_type='Per'
        )
    ],
    hired_at=APIHelper.HttpDateTime.from_value('Mon, 15 Jun 2009 20:45:30 GMT').datetime,
    joining_day="Monday",
    salary=230,
    boss=Person(
        address='address8',
        age=94,
        name='name2',
        uid='uid2',
        birthday=dateutil.parser.parse('2016-03-13').date(),
        birthtime=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
        person_type='Per'
    ),
    birthday=dateutil.parser.parse('2016-03-13').date(),
    birthtime=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
    person_type='Empl'
)

employee_map_of_array = {
    'key0': [
        False,
        True
    ],
    'key1': [
        True,
        False,
        True
    ],
    'key2': [
        False
    ]
}

try:
    result = custom_types_controller.custom_type_map_of_array_and_array_of_map_required(
        employee_array_of_map,
        employee_map_of_array
    )
    print(result)
except APIException as e: 
    print(e)

