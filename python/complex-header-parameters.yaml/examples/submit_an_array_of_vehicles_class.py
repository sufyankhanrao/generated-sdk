from complexheaderparametersapi.complexheaderparametersapi_client import ComplexheaderparametersapiClient
from complexheaderparametersapi.configuration import Environment
from complexheaderparametersapi.exceptions.api_exception import APIException
from complexheaderparametersapi.models.engine import Engine
from complexheaderparametersapi.models.fuel_type_enum import FuelTypeEnum
from complexheaderparametersapi.models.vehicle import Vehicle

client = ComplexheaderparametersapiClient(
    environment=Environment.PRODUCTION
)

client_controller = client.client
array_of_vehicles = [
    Vehicle(
        make='Toyota',
        model='Camry',
        year=2022,
        engine=Engine(
            horsepower=3000,
            fuel_type=FuelTypeEnum.PETROL
        )
    ),
    Vehicle(
        make='Toyota',
        model='Yaris',
        year=2020,
        engine=Engine(
            horsepower=1300,
            fuel_type=FuelTypeEnum.PETROL
        )
    )
]

try:
    result = client_controller.submit_an_array_of_vehicles(array_of_vehicles)
    print(result)
except APIException as e: 
    print(e)

