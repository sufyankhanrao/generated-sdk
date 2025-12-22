# Simple Xml Model

```python
simple_xml_model_controller = client.simple_xml_model
```

## Class Name

`SimpleXmlModelController`

## Methods

* [Generate](../../doc/controllers/simple-xml-model.md#generate)
* [Validate](../../doc/controllers/simple-xml-model.md#validate)
* [Generate 1](../../doc/controllers/simple-xml-model.md#generate-1)
* [Validate 1](../../doc/controllers/simple-xml-model.md#validate-1)


# Generate

This endpoint returns a cat model in xml

```python
def generate(self)
```

## Response Type

[`Cat`](../../doc/models/cat.md)

## Example Usage

```python
result = simple_xml_model_controller.generate()
print(result)
```


# Validate

This endpoint expects a 'Cat' model as xml.

```python
def validate(self,
            body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`Cat`](../../doc/models/cat.md) | Body, Required | - |

## Response Type

`Any`

## Example Usage

```python
body = Cat(
    meows=False
)

result = simple_xml_model_controller.validate(body)
print(result)
```


# Generate 1

This endpoint returns a 'Dog' model as xml.

```python
def generate_1(self)
```

## Response Type

[`Dog`](../../doc/models/dog.md)

## Example Usage

```python
result = simple_xml_model_controller.generate_1()
print(result)
```


# Validate 1

This endpoint expects a 'Dog' model as xml.

```python
def validate_1(self,
              body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`Dog`](../../doc/models/dog.md) | Body, Required | - |

## Response Type

`Any`

## Example Usage

```python
body = Dog(
    barks=False
)

result = simple_xml_model_controller.validate_1(body)
print(result)
```

