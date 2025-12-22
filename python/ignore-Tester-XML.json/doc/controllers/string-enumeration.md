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

[`StringEnum`](../../doc/models/string-enum.md)

## Example Usage

```python
result = string_enumeration_controller.generate()
print(result)
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

[`ServerResponse`](../../doc/models/server-response.md)

## Example Usage

```python
body = StringEnum.VALID_STRING

result = string_enumeration_controller.validate(body)
print(result)
```

