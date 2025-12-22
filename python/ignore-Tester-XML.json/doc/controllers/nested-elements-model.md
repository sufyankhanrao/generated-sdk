# Nested Elements Model

```python
nested_elements_model_controller = client.nested_elements_model
```

## Class Name

`NestedElementsModel`

## Methods

* [Generate](../../doc/controllers/nested-elements-model.md#generate)
* [Validate](../../doc/controllers/nested-elements-model.md#validate)


# Generate

Generate

```python
def generate(self)
```

## Response Type

[`ModelWithNestedElementsModel`](../../doc/models/model-with-nested-elements-model.md)

## Example Usage

```python
result = nested_elements_model_controller.generate()
print(result)
```


# Validate

This endpoint expects an XML document that should perfectly map onto the "ModelwithNestedElementsModel" model

```python
def validate(self,
            body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`ModelWithNestedElementsModel`](../../doc/models/model-with-nested-elements-model.md) | Body, Required | - |

## Response Type

[`ServerResponse`](../../doc/models/server-response.md)

## Example Usage

```python
body = ModelWithNestedElementsModel(
    elements=SimpleElements(
        string_element='string-element0',
        nonreserved='nonreserved2',
        number_element=240,
        precision=43.76,
        boolean_element=False,
        model_type='SimpleElements'
    ),
    simple='simple6'
)

result = nested_elements_model_controller.validate(body)
print(result)
```

