# Simple Integer

```python
simple_integer_controller = client.simple_integer
```

## Class Name

`SimpleInteger`

## Methods

* [Generate](../../doc/controllers/simple-integer.md#generate)
* [Validate](../../doc/controllers/simple-integer.md#validate)


# Generate

Generate

```python
def generate(self)
```

## Response Type

`int`

## Example Usage

```python
result = simple_integer_controller.generate()
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
| `body` | `int` | Body, Required | - |

## Response Type

[`ServerResponse`](../../doc/models/server-response.md)

## Example Usage

```python
body = 8

result = simple_integer_controller.validate(body)
print(result)
```

