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
vehicle_header = Vehicle(
    make='Toyota',
    model='Camry',
    year=2022,
    engine=Engine(
        horsepower=3000,
        fuel_type=FuelTypeEnum.PETROL
    )
)

try:
    result = client_controller.submit_vehicle_information(vehicle_header)
    print(result)
except APIException as e: 
    print(e)

