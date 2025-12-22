import dateutil.parser

from pathlib import Path

from testerfilesandmultipart.utilities.file_wrapper import FileWrapper
from testerfilesandmultipart.api_helper import APIHelper
from testerfilesandmultipart.configuration import Environment
from testerfilesandmultipart.exceptions.api_exception import APIException
from testerfilesandmultipart.models.days import Days
from testerfilesandmultipart.models.person import Employee
from testerfilesandmultipart.models.person import Person
from testerfilesandmultipart.testerfilesandmultipart_client import TesterfilesandmultipartClient

client = TesterfilesandmultipartClient(
    environment=Environment.PRODUCTION,
    port='80'
)

multipart_params_controller = client.multipart_params
collect = {
    'file': FileWrapper(Path('dummy_file').open('rb'), 'optional-content-type'),
    'integers': 30,
    'models': [
        Employee(
            address='address0',
            age=122,
            birthday=dateutil.parser.parse('2016-03-13').date(),
            birthtime=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
            name='name4',
            uid='uid4',
            department='department6',
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
            joining_day=Days.MONDAY,
            salary=88,
            working_days=[
                Days.SATURDAY,
                Days.SUNDAY
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
    ],
    'strings': 'strings0'
}
try:
    result = multipart_params_controller.send_multipart_with_json(collect)

    if result.is_success():
        print(result.body)
    elif result.is_error():
        print(result.errors)

except APIException as e: 
    print(e)

