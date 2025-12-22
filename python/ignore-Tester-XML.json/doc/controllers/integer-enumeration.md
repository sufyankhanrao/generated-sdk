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

[`IntegerEnum`](../../doc/models/integer-enum.md)

## Example Usage

```python
result = integer_enumeration_controller.generate()
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
| `body` | [`IntegerEnum`](../../doc/models/integer-enum.md) | Body, Required | - |

## Response Type

[`ServerResponse`](../../doc/models/server-response.md)

## Example Usage

```python
body = IntegerEnum.FOURTYSEVEN

result = integer_enumeration_controller.validate(body)
print(result)
```

