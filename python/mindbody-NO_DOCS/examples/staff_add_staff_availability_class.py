from mindbodypublicapi.configuration import Environment
from mindbodypublicapi.exceptions.api_exception import APIException
from mindbodypublicapi.mindbodypublicapi_client import MindbodypublicapiClient
from mindbodypublicapi.models.add_staff_availability_request import AddStaffAvailabilityRequest

client = MindbodypublicapiClient(
    environment=Environment.PRODUCTION
)

staff_controller = client.staff
version = '6'

request = AddStaffAvailabilityRequest(
    staff_id=188,
    is_availability=False,
    days_of_week=[
        'DaysOfWeek7'
    ],
    start_time='StartTime4',
    end_time='EndTime0',
    start_date='StartDate0',
    end_date='EndDate6',
    description='Description0',
    program_ids=[
        238
    ],
    location_id=238,
    status='Status4'
)

site_id = '-99'

authorization = 'authorization6'

try:
    result = staff_controller.add_staff_availability(
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

