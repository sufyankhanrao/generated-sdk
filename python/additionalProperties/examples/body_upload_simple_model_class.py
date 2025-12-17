from additionalpropertiestester.additionalpropertiestester_client import AdditionalpropertiestesterClient
from additionalpropertiestester.configuration import Environment
from additionalpropertiestester.exceptions.api_exception import APIException
from additionalpropertiestester.models.another_complex_model import AnotherComplexModel
from additionalpropertiestester.models.complex_model import ComplexModel
from additionalpropertiestester.models.simple_model import SimpleModel

client = AdditionalpropertiestesterClient(
    environment=Environment.PRODUCTION
)

body_controller = client.body
body = SimpleModel(
    required_property='Another required property',
    additional_properties={
        'anotherComplexModel': AnotherComplexModel(
            name='Another Complex Model',
            job='Worker',
            additional_properties={
                'salary': '10000 PKR',
                'working Hours': '9 AM to 5 PM'
            }
        ),
        'complexModel': ComplexModel(
            name='Complex Model',
            age='26 Years',
            additional_properties={
                'internalAnotherComplexModel': AnotherComplexModel(
                    name='Internal Another Complex Model',
                    job='Worker',
                    additional_properties={
                        'salary': '10000 PKR',
                        'working Hours': '9 AM to 5 PM'
                    }
                )
            }
        )
    }
)

try:
    result = body_controller.upload_simple_model(body)

    if result.is_success():
        print(result.body)
    elif result.is_error():
        print(result.errors)

except APIException as e: 
    print(e)

