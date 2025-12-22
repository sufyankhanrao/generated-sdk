# Query

This controller contains the usage of globally defined type combinators in query

```python
query_controller = client.query
```

## Class Name

`QueryController`


# Send Primitive

Send all Globally defined primitive TypeCombinators in query

```python
def send_primitive(self,
                  one_of_primitive,
                  any_of_primitive,
                  one_of_and_any_of_primitive)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `one_of_primitive` | str \| int | Query, Required | OneOf with primitive types and metadata. |
| `any_of_primitive` | str \| int | Query, Required | AnyOf with primitive types and metadata. |
| `one_of_and_any_of_primitive` | str \| int \| bool | Query, Required | OneOf and AnyOf cases at the same level and also at inner levels with primitive types and metadata. |

## Response Type

str | int

## Example Usage

```python
one_of_primitive = 2

any_of_primitive = 'some string'

one_of_and_any_of_primitive = 'some other string'

result = query_controller.send_primitive(
    one_of_primitive,
    any_of_primitive,
    one_of_and_any_of_primitive
)
print(result)
```

## Example Response

```
2
```

