from typecombinatorglobal.configuration import Environment
from typecombinatorglobal.exceptions.api_exception import APIException
from typecombinatorglobal.models.animal import Cat
from typecombinatorglobal.models.lion import Lion
from typecombinatorglobal.typecombinatorglobal_client import TypecombinatorglobalClient

client = TypecombinatorglobalClient(
    environment=Environment.PRODUCTION,
    port='3000',
    sub_url='multitype/global'
)

form_controller = client.form
one_of_cat_dog_all_of_pet_type = Cat(
    name='hosico',
    color='yellow',
    one_of_kind='One Of kind2',
    pet_type='Cat',
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

one_of_cat_dog_oaf_pet_type = Cat(
    name='hosico',
    color='yellow',
    one_of_kind='One Of kind2',
    pet_type='Kitty',
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

one_of_cat_dog_kind = Cat(
    name='hosico',
    color='yellow',
    one_of_kind='small',
    pet_type='Cat',
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

try:
    result = form_controller.send_all_of_discriminated(
        one_of_cat_dog_all_of_pet_type,
        one_of_cat_dog_oaf_pet_type,
        one_of_cat_dog_kind
    )
    print(result)
except APIException as e: 
    print(e)

