# Oneof Array Xml Model

```python
oneof_array_xml_model_controller = client.oneof_array_xml_model
```

## Class Name

`OneofArrayXmlModelController`

## Methods

* [Generate](../../doc/controllers/oneof-array-xml-model.md#generate)
* [Validate](../../doc/controllers/oneof-array-xml-model.md#validate)
* [Generate 1](../../doc/controllers/oneof-array-xml-model.md#generate-1)
* [Validate 1](../../doc/controllers/oneof-array-xml-model.md#validate-1)


# Generate

This endpoint returns a 'CatsOrDogs' model as xml.

```python
def generate(self)
```

## Response Type

[`CatsOrDogs`](../../doc/models/cats-or-dogs.md)

## Example Usage

```python
result = oneof_array_xml_model_controller.generate()
print(result)
```


# Validate

This endpoint expects a 'CatsOrDogs' model as xml.

```python
def validate(self,
            body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`CatsOrDogs`](../../doc/models/cats-or-dogs.md) | Body, Required | - |

## Response Type

`Any`

## Example Usage

```python
body = CatsOrDogs(
    value=jsonpickle.decode('{"key1":"val1","key2":"val2"}')
)

result = oneof_array_xml_model_controller.validate(body)
print(result)
```


# Generate 1

This endpoint returns a 'CatsOrDogs' model as xml.

```python
def generate_1(self)
```

## Response Type

[`CatsOrDogs`](../../doc/models/cats-or-dogs.md)

## Example Usage

```python
result = oneof_array_xml_model_controller.generate_1()
print(result)
```


# Validate 1

This endpoint expects a 'CatsOrDogs' model as xml.

```python
def validate_1(self,
              body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`CatsOrDogs`](../../doc/models/cats-or-dogs.md) | Body, Required | - |

## Response Type

`Any`

## Example Usage

```python
body = CatsOrDogs(
    value=jsonpickle.decode('{"key1":"val1","key2":"val2"}')
)

result = oneof_array_xml_model_controller.validate_1(body)
print(result)
```

