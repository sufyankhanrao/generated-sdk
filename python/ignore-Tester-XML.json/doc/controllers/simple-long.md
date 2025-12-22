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

`int`

## Example Usage

```python
result = simple_long_controller.generate()
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

result = simple_long_controller.validate(body)
print(result)
```

