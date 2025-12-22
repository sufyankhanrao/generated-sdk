# Simple Precision

```python
simple_precision_controller = client.simple_precision
```

## Class Name

`SimplePrecision`

## Methods

* [Generate](../../doc/controllers/simple-precision.md#generate)
* [Validate](../../doc/controllers/simple-precision.md#validate)


# Generate

Generate

```python
def generate(self)
```

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type `float`.

## Example Usage

```python
result = simple_precision_controller.generate()

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
| `body` | `float` | Body, Required | - |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`ServerResponse`](../../doc/models/server-response.md).

## Example Usage

```python
body = 135.76

result = simple_precision_controller.validate(body)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

