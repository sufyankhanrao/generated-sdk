import dateutil.parser

from mindbodypublicapi.configuration import Environment
from mindbodypublicapi.exceptions.api_exception import APIException
from mindbodypublicapi.mindbodypublicapi_client import MindbodypublicapiClient
from mindbodypublicapi.models.appointment_gender_preference_1_enum import AppointmentGenderPreference1Enum
from mindbodypublicapi.models.client_suspension_info import ClientSuspensionInfo
from mindbodypublicapi.models.client_with_suspension_info import ClientWithSuspensionInfo
from mindbodypublicapi.models.update_client_request import UpdateClientRequest

client = MindbodypublicapiClient(
    environment=Environment.PRODUCTION
)

client_controller = client.client
version = '6'

request = UpdateClientRequest(
    client=ClientWithSuspensionInfo(
        suspension_info=ClientSuspensionInfo(
            booking_suspended=False,
            suspension_start_date='SuspensionStartDate8',
            suspension_end_date='SuspensionEndDate2'
        ),
        appointment_gender_preference=AppointmentGenderPreference1Enum.ENUM_NONE,
        birth_date=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
        country='Country8',
        creation_date=dateutil.parser.parse('2016-03-13T12:52:32.123Z')
    ),
    test=False,
    cross_regional_update=False,
    new_id='NewId2',
    lead_channel_id=216
)

site_id = '-99'

authorization = 'authorization6'

try:
    result = client_controller.update_client(
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

