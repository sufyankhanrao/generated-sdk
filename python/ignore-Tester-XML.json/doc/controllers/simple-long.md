# Simple Long

```python
simple_long_controller = client.simple_long
```

## Class Name

`SimpleLong`

## Methods

* [Generate](../../doc/controllers/simple-long.md#generate)
* [Validate](../../doc/controllers/simple-long.md#validate)


# Generate

Generate

```python
def generate(self)
```

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type `int`.

## Example Usage

```python
result = simple_long_controller.generate()

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# Validate

Validate

```python
def validate(self,
            body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | `int` | Body, Required | - |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`ServerResponse`](../../doc/models/server-response.md).

## Example Usage

```python
body = 8

result = simple_long_controller.validate(body)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

