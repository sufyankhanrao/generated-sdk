from typecombinatorglobal.configuration import Environment
from typecombinatorglobal.exceptions.api_exception import APIException
from typecombinatorglobal.models.deer import Deer
from typecombinatorglobal.typecombinatorglobal_client import TypecombinatorglobalClient

client = TypecombinatorglobalClient(
    environment=Environment.PRODUCTION,
    port='3000',
    sub_url='multitype/global'
)

form_controller = client.form
alias = Deer(
    name='deer21',
    weight='30 kg',
    mtype='Hunted'
)

alias_of_alias = Deer(
    name='deer22',
    weight='20 kg',
    mtype='Hunted'
)

try:
    result = form_controller.send_alias(
        alias,
        alias_of_alias
    )

    if result.is_success():
        print(result.body)
    elif result.is_error():
        print(result.errors)

except APIException as e: 
    print(e)

