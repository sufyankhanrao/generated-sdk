# Simple String

```python
simple_string_controller = client.simple_string
```

## Class Name

`SimpleString`

## Methods

* [Generate](../../doc/controllers/simple-string.md#generate)
* [Validate](../../doc/controllers/simple-string.md#validate)
* [Generate Array](../../doc/controllers/simple-string.md#generate-array)
* [Validate Array](../../doc/controllers/simple-string.md#validate-array)


# Generate

Generate

```python
def generate(self)
```

## Response Type

`str`

## Example Usage

```python
result = simple_string_controller.generate()
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
| `body` | `str` | Body, Required | - |

## Response Type

[`ServerResponse`](../../doc/models/server-response.md)

## Example Usage

```python
body = 'body6'

result = simple_string_controller.validate(body)
print(result)
```


# Generate Array

Generate

```python
def generate_array(self)
```

## Response Type

`List[str]`

## Example Usage

```python
result = simple_string_controller.generate_array()
print(result)
```


# Validate Array

Validate

```python
def validate_array(self,
                  body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | `List[str]` | Body, Required | - |

## Response Type

[`ServerResponse`](../../doc/models/server-response.md)

## Example Usage

```python
body = [
    'body4',
    'body5'
]

result = simple_string_controller.validate_array(body)
print(result)
```

