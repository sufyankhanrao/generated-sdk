from mindbodypublicapi.configuration import Environment
from mindbodypublicapi.exceptions.api_exception import APIException
from mindbodypublicapi.mindbodypublicapi_client import MindbodypublicapiClient
from mindbodypublicapi.models.assign_staff_session_type_request import AssignStaffSessionTypeRequest

client = MindbodypublicapiClient(
    environment=Environment.PRODUCTION
)

staff_controller = client.staff
version = '6'

request = AssignStaffSessionTypeRequest(
    staff_id=188,
    session_type_id=82,
    active=False,
    time_length=222,
    prep_time=166,
    finish_time=246,
    pay_rate_type='PayRateType2',
    pay_rate_amount=169.62
)

site_id = '-99'

authorization = 'authorization6'

try:
    result = staff_controller.assign_staff_session_type(
        version,
        request,
        site_id,
        authorization=authorization
    )

    if result.is_success():
        print(result.body)
    elif result.is_error():
        print(result.errors)

except APIException as e: 
    print(e)

