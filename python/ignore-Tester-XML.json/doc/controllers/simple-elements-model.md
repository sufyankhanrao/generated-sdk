# Simple Elements Model

```python
simple_elements_model_controller = client.simple_elements_model
```

## Class Name

`SimpleElementsModel`

## Methods

* [Generate](../../doc/controllers/simple-elements-model.md#generate)
* [Validate](../../doc/controllers/simple-elements-model.md#validate)


# Generate

This endpoint returns an XML document that should perfectly map onto the "Simple Elements" model

```python
def generate(self)
```

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`SimpleElements`](../../doc/models/simple-elements.md).

## Example Usage

```python
result = simple_elements_model_controller.generate()

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
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
| `body` | [`SimpleElements`](../../doc/models/simple-elements.md) | Body, Required | - |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`ServerResponse`](../../doc/models/server-response.md).

## Example Usage

```python
body = SimpleElements(
    string_element='string-element4',
    nonreserved='nonreserved6',
    number_element=164,
    precision=247.8,
    boolean_element=False,
    model_type='SimpleElements'
)

result = simple_elements_model_controller.validate(body)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

