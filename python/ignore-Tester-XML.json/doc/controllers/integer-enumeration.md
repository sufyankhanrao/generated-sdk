# Integer Enumeration

```python
integer_enumeration_controller = client.integer_enumeration
```

## Class Name

`IntegerEnumeration`

## Methods

* [Generate](../../doc/controllers/integer-enumeration.md#generate)
* [Validate](../../doc/controllers/integer-enumeration.md#validate)


# Generate

Generate

```python
def generate(self)
```

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`IntegerEnum`](../../doc/models/integer-enum.md).

## Example Usage

```python
result = integer_enumeration_controller.generate()

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
| `body` | [`IntegerEnum`](../../doc/models/integer-enum.md) | Body, Required | - |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`ServerResponse`](../../doc/models/server-response.md).

## Example Usage

```python
body = IntegerEnum.FOURTYSEVEN

result = integer_enumeration_controller.validate(body)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

