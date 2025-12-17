from mindbodypublicapi.configuration import Environment
from mindbodypublicapi.exceptions.api_exception import APIException
from mindbodypublicapi.mindbodypublicapi_client import MindbodypublicapiClient
from mindbodypublicapi.models.update_staff_permissions_request import UpdateStaffPermissionsRequest

client = MindbodypublicapiClient(
    environment=Environment.PRODUCTION
)

staff_controller = client.staff
version = '6'

request = UpdateStaffPermissionsRequest(
    staff_id=188,
    permission_group_name='PermissionGroupName8'
)

site_id = '-99'

authorization = 'authorization6'

try:
    result = staff_controller.update_staff_permissions(
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

