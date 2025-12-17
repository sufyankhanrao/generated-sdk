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

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`ModelWithInheritedElements`](../../doc/models/model-with-inherited-elements.md).

## Example Usage

```python
result = elements_model_with_inheritance_controller.generate()

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
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

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`ServerResponse`](../../doc/models/server-response.md).

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

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

