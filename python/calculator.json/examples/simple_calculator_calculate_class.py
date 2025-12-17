from apimaticcalculator.apimaticcalculator_client import ApimaticcalculatorClient
from apimaticcalculator.configuration import Environment
from apimaticcalculator.exceptions.api_exception import APIException
from apimaticcalculator.models.operation_type_enum import OperationTypeEnum

client = ApimaticcalculatorClient(
    environment=Environment.PRODUCTION
)

simple_calculator_controller = client.simple_calculator
collect = {
    'operation': OperationTypeEnum.MULTIPLY,
    'x': 222.14,
    'y': 165.14
}
try:
    result = simple_calculator_controller.get_calculate(collect)

    if result.is_success():
        print(result.body)
    elif result.is_error():
        print(result.errors)

except APIException as e: 
    print(e)

