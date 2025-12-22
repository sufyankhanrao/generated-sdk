# Oneof Xml Model

```python
oneof_xml_model_controller = client.oneof_xml_model
```

## Class Name

`OneofXmlModelController`

## Methods

* [Generate](../../doc/controllers/oneof-xml-model.md#generate)
* [Validate](../../doc/controllers/oneof-xml-model.md#validate)
* [Generate 1](../../doc/controllers/oneof-xml-model.md#generate-1)
* [Validate 1](../../doc/controllers/oneof-xml-model.md#validate-1)


# Generate

This endpoint returns a 'CatOrDog' model as xml.

```python
def generate(self)
```

## Response Type

[`CatOrDog`](../../doc/models/cat-or-dog.md)

## Example Usage

```python
result = oneof_xml_model_controller.generate()
print(result)
```


# Validate

This endpoint expects a 'CatOrDog' model as xml.

```python
def validate(self,
            body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`CatOrDog`](../../doc/models/cat-or-dog.md) | Body, Required | - |

## Response Type

`Any`

## Example Usage

```python
body = CatOrDog(
    value=jsonpickle.decode('{"key1":"val1","key2":"val2"}')
)

result = oneof_xml_model_controller.validate(body)
print(result)
```


# Generate 1

This endpoint returns a 'CatOrDog' model as xml.

```python
def generate_1(self)
```

## Response Type

[`CatOrDog`](../../doc/models/cat-or-dog.md)

## Example Usage

```python
result = oneof_xml_model_controller.generate_1()
print(result)
```


# Validate 1

This endpoint expects a 'CatOrDog' model as xml.

```python
def validate_1(self,
              body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`CatOrDog`](../../doc/models/cat-or-dog.md) | Body, Required | - |

## Response Type

`Any`

## Example Usage

```python
body = CatOrDog(
    value=jsonpickle.decode('{"key1":"val1","key2":"val2"}')
)

result = oneof_xml_model_controller.validate_1(body)
print(result)
```

