# Elements Model With Inheritance

```python
elements_model_with_inheritance_controller = client.elements_model_with_inheritance
```

## Class Name

`ElementsModelWithInheritance`

## Methods

* [Generate](../../doc/controllers/elements-model-with-inheritance.md#generate)
* [Validate](../../doc/controllers/elements-model-with-inheritance.md#validate)


# Generate

Generate

```python
def generate(self)
```

## Response Type

[`ModelWithInheritedElements`](../../doc/models/model-with-inherited-elements.md)

## Example Usage

```python
result = elements_model_with_inheritance_controller.generate()
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
| `body` | [`ModelWithInheritedElements`](../../doc/models/model-with-inherited-elements.md) | Body, Required | - |

## Response Type

[`ServerResponse`](../../doc/models/server-response.md)

## Example Usage

```python
body = ModelWithInheritedElements(
    string_element='string-element2',
    nonreserved='nonreserved4',
    number_element=150,
    precision=22.38,
    boolean_element=False,
    new_string_field='NewStringField6',
    model_type='ModelWithInheritedElements'
)

result = elements_model_with_inheritance_controller.validate(body)
print(result)
```

