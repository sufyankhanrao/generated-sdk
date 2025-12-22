# Simple UUID

```python
simple_uuid_controller = client.simple_uuid
```

## Class Name

`SimpleUUID`

## Methods

* [Generate](../../doc/controllers/simple-uuid.md#generate)
* [Validate](../../doc/controllers/simple-uuid.md#validate)


# Generate

Generate

```python
def generate(self)
```

## Response Type

`uuid|str`

## Example Usage

```python
result = simple_uuid_controller.generate()
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
| `body` | `uuid\|str` | Body, Required | - |

## Response Type

[`ServerResponse`](../../doc/models/server-response.md)

## Example Usage

```python
body = '00000df8-0000-0000-0000-000000000000'

result = simple_uuid_controller.validate(body)
print(result)
```

