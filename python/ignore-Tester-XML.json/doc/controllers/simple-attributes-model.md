# Simple Attributes Model

```python
simple_attributes_model_controller = client.simple_attributes_model
```

## Class Name

`SimpleAttributesModel`

## Methods

* [Generate](../../doc/controllers/simple-attributes-model.md#generate)
* [Validate](../../doc/controllers/simple-attributes-model.md#validate)


# Generate

This endpoint returns an XML document that should perfectly map onto the "Simple Attributes" model

```python
def generate(self)
```

## Response Type

[`SimpleAttributes`](../../doc/models/simple-attributes.md)

## Example Usage

```python
result = simple_attributes_model_controller.generate()
print(result)
```


# Validate

This endpoint expects an XML document that should perfectly map onto the "Simple Attributes" model

```python
def validate(self,
            body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`SimpleAttributes`](../../doc/models/simple-attributes.md) | Body, Required | - |

## Response Type

[`ServerResponse`](../../doc/models/server-response.md)

## Example Usage

```python
body = SimpleAttributes(
    string_element='string-element4',
    nonreserved='nonreserved6',
    number_element=164,
    precision=247.8,
    boolean_element=False,
    attributes_type='SimpleAttributes'
)

result = simple_attributes_model_controller.validate(body)
print(result)
```

