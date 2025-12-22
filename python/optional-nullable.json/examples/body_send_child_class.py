from optionalandnullable.configuration import Environment
from optionalandnullable.exceptions.api_exception import APIException
from optionalandnullable.models.grand_parent_class import ChildClass
from optionalandnullable.optionalandnullable_client import OptionalandnullableClient

client = OptionalandnullableClient(
    environment=Environment.PRODUCTION
)

body_controller = client.body
un_set = False

set_to_null = False

field = 'field6'

child = ChildClass(
    grand_parent_required_nullable='Grand_Parent_Required_Nullable6',
    grand_parent_required='not nullable and required',
    parent_required_nullable='Parent_Required_Nullable8',
    parent_required='not nullable and required',
    required_nullable='Required_Nullable2',
    required='not nullable and required',
    optional_nullable_with_default_value='With default value',
    mclass=23,
    parent_optional_nullable_with_default_value='Has default value'
)

try:
    result = body_controller.create_send_child(
        un_set,
        set_to_null,
        field,
        child
    )
    print(result)
except APIException as e: 
    print(e)

