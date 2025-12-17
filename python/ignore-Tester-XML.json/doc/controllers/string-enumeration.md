# String Enumeration

```python
string_enumeration_controller = client.string_enumeration
```

## Class Name

`StringEnumeration`

## Methods

* [Generate](../../doc/controllers/string-enumeration.md#generate)
* [Validate](../../doc/controllers/string-enumeration.md#validate)


# Generate

Generate

```python
def generate(self)
```

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`StringEnum`](../../doc/models/string-enum.md).

## Example Usage

```python
result = string_enumeration_controller.generate()

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# Validate

validate

```python
def validate(self,
            body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`StringEnum`](../../doc/models/string-enum.md) | Body, Required | - |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`ServerResponse`](../../doc/models/server-response.md).

## Example Usage

```python
body = StringEnum.VALID_STRING

result = string_enumeration_controller.validate(body)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

