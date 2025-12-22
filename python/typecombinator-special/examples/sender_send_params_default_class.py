from typecombinatorspecial.configuration import Environment
from typecombinatorspecial.exceptions.api_exception import APIException
from typecombinatorspecial.models.days_enum import DaysEnum
from typecombinatorspecial.models.month_name_enum import MonthNameEnum
from typecombinatorspecial.models.month_number_enum import MonthNumberEnum
from typecombinatorspecial.typecombinatorspecial_client import TypecombinatorspecialClient

client = TypecombinatorspecialClient(
    environment=Environment.TESTING,
    sub_url='multitype/special'
)

sender_controller = client.sender
form_default_enum = MonthNameEnum.FEBRUARY

query_default_enum = DaysEnum.MONDAY

template_default_enum = MonthNumberEnum.JANUARY

try:
    result = sender_controller.send_params_default(
        form_default_enum=form_default_enum,
        query_default_enum=query_default_enum,
        template_default_enum=template_default_enum
    )
    print(result)
except APIException as e: 
    print(e)

