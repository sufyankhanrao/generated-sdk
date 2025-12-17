from mindbodypublicapi.configuration import Environment
from mindbodypublicapi.exceptions.api_exception import APIException
from mindbodypublicapi.mindbodypublicapi_client import MindbodypublicapiClient
from mindbodypublicapi.models.class_client_detail import ClassClientDetail
from mindbodypublicapi.models.remove_clients_from_classes_request import RemoveClientsFromClassesRequest

client = MindbodypublicapiClient(
    environment=Environment.PRODUCTION
)

mclass_controller = client.mclass
version = '6'

request = RemoveClientsFromClassesRequest(
    details=[
        ClassClientDetail(
            client_ids=[
                'ClientIds5'
            ],
            class_id=190
        ),
        ClassClientDetail(
            client_ids=[
                'ClientIds5'
            ],
            class_id=190
        )
    ],
    test=False,
    send_email=False,
    late_cancel=False,
    limit=32
)

site_id = '-99'

authorization = 'authorization6'

try:
    result = mclass_controller.remove_clients_from_classes(
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

