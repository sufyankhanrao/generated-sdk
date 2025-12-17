from complexheaderparametersapi.complexheaderparametersapi_client import ComplexheaderparametersapiClient
from complexheaderparametersapi.configuration import Environment
from complexheaderparametersapi.exceptions.api_exception import APIException
from complexheaderparametersapi.models.car import Car
from complexheaderparametersapi.models.engine import Engine
from complexheaderparametersapi.models.fuel_type_enum import FuelTypeEnum

client = ComplexheaderparametersapiClient(
    environment=Environment.PRODUCTION
)

client_controller = client.client
one_of_vehicle = Car(
    make='Toyota',
    model='Yaris',
    doors=2,
    engine=Engine(
        horsepower=1500,
        fuel_type=FuelTypeEnum.PETROL
    )
)

try:
    result = client_controller.submit_a_one_of_vehicle(one_of_vehicle)

    if result.is_success():
        print(result.body)
    elif result.is_error():
        print(result.errors)

except APIException as e: 
    print(e)

