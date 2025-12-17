# Nested Attributes Model

```python
nested_attributes_model_controller = client.nested_attributes_model
```

## Class Name

`NestedAttributesModel`

## Methods

* [Generate](../../doc/controllers/nested-attributes-model.md#generate)
* [Validate](../../doc/controllers/nested-attributes-model.md#validate)


# Generate

Generate

```python
def generate(self)
```

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`ModelWithNestedAttributesModel`](../../doc/models/model-with-nested-attributes-model.md).

## Example Usage

```python
result = nested_attributes_model_controller.generate()

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# Validate

This endpoint expects an XML document that should perfectly map onto the "ModelWithNestedAttributesModel" model

```python
def validate(self,
            body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`ModelWithNestedAttributesModel`](../../doc/models/model-with-nested-attributes-model.md) | Body, Required | - |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`ServerResponse`](../../doc/models/server-response.md).

## Example Usage

```python
body = ModelWithNestedAttributesModel(
    simple_attributes=SimpleAttributes(
        string_element='string-element6',
        nonreserved='nonreserved8',
        number_element=6,
        precision=28.62,
        boolean_element=False,
        attributes_type='SimpleAttributes'
    ),
    simple='simple6'
)

result = nested_attributes_model_controller.validate(body)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

