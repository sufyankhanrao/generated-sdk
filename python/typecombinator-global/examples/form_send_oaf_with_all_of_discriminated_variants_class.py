from typecombinatorglobal.configuration import Environment
from typecombinatorglobal.exceptions.api_exception import APIException
from typecombinatorglobal.models.animal import Animal
from typecombinatorglobal.models.animal import Cat
from typecombinatorglobal.models.deer import Deer
from typecombinatorglobal.models.lion import Lion
from typecombinatorglobal.models.person import Employee
from typecombinatorglobal.typecombinatorglobal_client import TypecombinatorglobalClient

client = TypecombinatorglobalClient(
    environment=Environment.PRODUCTION,
    port='3000',
    sub_url='multitype/global'
)

form_controller = client.form
one_of_animal_lion_disc_kind = Lion(
    id='23',
    weight='100 kg',
    mtype='hunter',
    kind='wild'
)

one_of_cat_lion_disc_kind = Lion(
    id='23',
    weight='100 kg',
    mtype='hunter',
    kind='wild'
)

one_of_animal_lion = Animal(
    pet_type='Animal',
    id=2,
    friend=Deer(
        name='deer22',
        weight='20 kg',
        mtype='Hunted'
    ),
    enemy=Lion(
        id='23',
        weight='100 kg',
        mtype='hunter',
        kind='northener'
    ),
    kind='kind2'
)

one_of_cat_lion = Cat(
    name='hosico',
    color='yellow',
    one_of_kind='One Of kind2',
    pet_type='catty',
    id='String5',
    friend=Lion(
        id='id0',
        weight='weight6',
        mtype='hunter',
        kind='kind8'
    ),
    enemy=Lion(
        id='id0',
        weight='weight6',
        mtype='type0',
        kind='northener'
    ),
    kind='kind2'
)

one_of_cat_dog_and_lion_deer = Animal(
    pet_type='Animal',
    id='23',
    friend=Lion(
        id='id0',
        weight='weight6',
        mtype='hunter',
        kind='kind8'
    ),
    enemy=Lion(
        id='id0',
        weight='weight6',
        mtype='type0',
        kind='northener'
    ),
    kind='kind2'
)

one_of_employee_entrepreneur_disc = Employee(
    name='John',
    ssn=123,
    salary=157.76,
    build='Endomorphs',
    mtype='Empl'
)

one_of_employee_entrepreneur = Employee(
    name='John',
    ssn=123,
    salary=157.76,
    build='Endomorphs',
    mtype='Empl'
)

try:
    result = form_controller.send_oaf_with_all_of_discriminated_variants(
        one_of_animal_lion_disc_kind,
        one_of_cat_lion_disc_kind,
        one_of_animal_lion,
        one_of_cat_lion,
        one_of_cat_dog_and_lion_deer,
        one_of_employee_entrepreneur_disc,
        one_of_employee_entrepreneur
    )

    if result.is_success():
        print(result.body)
    elif result.is_error():
        print(result.errors)

except APIException as e: 
    print(e)

