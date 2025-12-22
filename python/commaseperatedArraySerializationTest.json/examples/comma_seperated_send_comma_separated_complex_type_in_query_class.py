import dateutil.parser
import jsonpickle

from commaseperatedarrayserialization.commaseperatedarrayserialization_client import CommaseperatedarrayserializationClient
from commaseperatedarrayserialization.configuration import Environment
from commaseperatedarrayserialization.exceptions.api_exception import APIException
from commaseperatedarrayserialization.models.complex_type import ComplexType
from commaseperatedarrayserialization.models.inner_complex_type import InnerComplexType
from commaseperatedarrayserialization.models.suite_code_enum import SuiteCodeEnum

client = CommaseperatedarrayserializationClient(
    environment=Environment.TESTING,
    port='80',
    suites=SuiteCodeEnum.HEARTS
)

comma_seperated_controller = client.comma_seperated
complex_type = ComplexType(
    number_list_type=[
        232
    ],
    number_map_type={
        'key0': 149,
        'key1': 150
    },
    inner_complex_type=InnerComplexType(
        string_type='stringType8',
        boolean_type=False,
        date_time_type=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
        date_type=dateutil.parser.parse('2016-03-13').date(),
        uuid_type='00001742-0000-0000-0000-000000000000',
        long_type=40,
        precision_type=8.18,
        object_type=jsonpickle.decode('{"key1":"val1","key2":"val2"}'),
        string_list_type=[
            'stringListType8'
        ]
    ),
    inner_complex_list_type=[
        InnerComplexType(
            string_type='stringType0',
            boolean_type=False,
            date_time_type=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
            date_type=dateutil.parser.parse('2016-03-13').date(),
            uuid_type='00001992-0000-0000-0000-000000000000',
            long_type=88,
            precision_type=70.1,
            object_type=jsonpickle.decode('{"key1":"val1","key2":"val2"}'),
            string_list_type=[
                'stringListType0',
                'stringListType1',
                'stringListType2'
            ]
        )
    ]
)

try:
    result = comma_seperated_controller.create_send_comma_separated_complex_type_in_query(complex_type)

    if result.is_success():
        print(result.body)
    elif result.is_error():
        print(result.errors)

except APIException as e: 
    print(e)

