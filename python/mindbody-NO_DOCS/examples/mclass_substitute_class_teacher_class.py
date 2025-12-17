from mindbodypublicapi.configuration import Environment
from mindbodypublicapi.exceptions.api_exception import APIException
from mindbodypublicapi.mindbodypublicapi_client import MindbodypublicapiClient
from mindbodypublicapi.models.substitute_class_teacher_request import SubstituteClassTeacherRequest

client = MindbodypublicapiClient(
    environment=Environment.PRODUCTION
)

mclass_controller = client.mclass
version = '6'

request = SubstituteClassTeacherRequest(
    class_id=90,
    staff_id=188,
    override_conflicts=False,
    send_client_email=False,
    send_original_teacher_email=False,
    send_substitute_teacher_email=False
)

site_id = '-99'

authorization = 'authorization6'

try:
    result = mclass_controller.substitute_class_teacher(
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

