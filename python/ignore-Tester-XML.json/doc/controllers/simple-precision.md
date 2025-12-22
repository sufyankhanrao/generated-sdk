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

`float`

## Example Usage

```python
result = simple_precision_controller.generate()
print(result)
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

[`ServerResponse`](../../doc/models/server-response.md)

## Example Usage

```python
body = 135.76

result = simple_precision_controller.validate(body)
print(result)
```

