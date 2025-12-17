
from mindbodypublicapi.configuration import Environment
from mindbodypublicapi.exceptions.api_exception import APIException
from mindbodypublicapi.mindbodypublicapi_client import MindbodypublicapiClient
from mindbodypublicapi.models.add_staff_request import AddStaffRequest

client = MindbodypublicapiClient(
    environment=Environment.PRODUCTION
)

staff_controller = client.staff
version = '6'

request = AddStaffRequest(
    first_name='FirstName8',
    last_name='LastName8',
    email='Email8',
    is_male=False,
    home_phone='HomePhone8',
    work_phone='WorkPhone2',
    mobile_phone='MobilePhone6'
)

site_id = '-99'

authorization = 'authorization6'

try:
    result = staff_controller.add_staff(
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

