# Body

```python
body_controller = client.body
```

## Class Name

`BodyController`


# Create Send Child

```python
def create_send_child(self,
                     un_set,
                     set_to_null,
                     field,
                     child)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `un_set` | `bool` | Query, Required | - |
| `set_to_null` | `bool` | Query, Required | - |
| `field` | `str` | Query, Required | - |
| `child` | [`ChildClass`](../../doc/models/child-class.md) | Body, Required | - |

## Response Type

[`ServerResponse`](../../doc/models/server-response.md)

## Example Usage

```python
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

result = body_controller.create_send_child(
    un_set,
    set_to_null,
    field,
    child
)
print(result)
```

