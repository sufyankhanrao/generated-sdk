# Attributes Model With Inheritance

```python
attributes_model_with_inheritance_controller = client.attributes_model_with_inheritance
```

## Class Name

`AttributesModelWithInheritance`

## Methods

* [Generate](../../doc/controllers/attributes-model-with-inheritance.md#generate)
* [Validate](../../doc/controllers/attributes-model-with-inheritance.md#validate)


# Generate

Generate

```python
def generate(self)
```

## Response Type

[`ModelWithInheritedAttributes`](../../doc/models/model-with-inherited-attributes.md)

## Example Usage

```python
result = attributes_model_with_inheritance_controller.generate()
print(result)
```


# Validate

This endpoint expects an XML document that should perfectly map onto the "ModelwithInheritedElements" model

```python
def validate(self,
            body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`ModelWithInheritedAttributes`](../../doc/models/model-with-inherited-attributes.md) | Body, Required | - |

## Response Type

[`ServerResponse`](../../doc/models/server-response.md)

## Example Usage

```python
body = ModelWithInheritedAttributes(
    string_element='string-element6',
    nonreserved='nonreserved8',
    number_element=6,
    precision=28.62,
    boolean_element=False,
    new_string_field='NewStringField6',
    attributes_type='ModelWithInheritedAttributes'
)

result = attributes_model_with_inheritance_controller.validate(body)
print(result)
```

