import dateutil.parser

from mindbodypublicapi.configuration import Environment
from mindbodypublicapi.exceptions.api_exception import APIException
from mindbodypublicapi.mindbodypublicapi_client import MindbodypublicapiClient

client = MindbodypublicapiClient(
    environment=Environment.PRODUCTION
)

mclass_controller = client.mclass
version = '6'

site_id = '-99'

authorization = 'authorization6'

get_courses_request_course_i_ds = [
    11,
    12,
    13
]

get_courses_request_end_date = dateutil.parser.parse('2016-03-13T12:52:32.123Z')

get_courses_request_limit = 158

get_courses_request_location_i_ds = [
    175,
    176
]

get_courses_request_offset = 92

get_courses_request_program_i_ds = [
    250
]

get_courses_request_semester_i_ds = [
    73,
    74,
    75
]

get_courses_request_staff_i_ds = [
    73
]

get_courses_request_start_date = dateutil.parser.parse('2016-03-13T12:52:32.123Z')

try:
    result = mclass_controller.get_courses(
        version,
        site_id,
        authorization=authorization,
        get_courses_request_course_i_ds=get_courses_request_course_i_ds,
        get_courses_request_end_date=get_courses_request_end_date,
        get_courses_request_limit=get_courses_request_limit,
        get_courses_request_location_i_ds=get_courses_request_location_i_ds,
        get_courses_request_offset=get_courses_request_offset,
        get_courses_request_program_i_ds=get_courses_request_program_i_ds,
        get_courses_request_semester_i_ds=get_courses_request_semester_i_ds,
        get_courses_request_staff_i_ds=get_courses_request_staff_i_ds,
        get_courses_request_start_date=get_courses_request_start_date
    )

    if result.is_success():
        print(result.body)
    elif result.is_error():
        print(result.errors)

except APIException as e: 
    print(e)

