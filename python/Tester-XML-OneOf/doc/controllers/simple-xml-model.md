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

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`Cat`](../../doc/models/cat.md).

## Example Usage

```python
result = simple_xml_model_controller.generate()

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
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

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type `Any`.

## Example Usage

```python
body = Cat(
    meows=False
)

result = simple_xml_model_controller.validate(body)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# Generate 1

This endpoint returns a 'Dog' model as xml.

```python
def generate_1(self)
```

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`Dog`](../../doc/models/dog.md).

## Example Usage

```python
result = simple_xml_model_controller.generate_1()

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
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

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type `Any`.

## Example Usage

```python
body = Dog(
    barks=False
)

result = simple_xml_model_controller.validate_1(body)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

