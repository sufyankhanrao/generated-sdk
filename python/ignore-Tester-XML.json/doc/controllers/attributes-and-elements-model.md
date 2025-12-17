# Attributes and Elements Model

```python
attributes_and_elements_model_controller = client.attributes_and_elements_model
```

## Class Name

`AttributesAndElementsModel`

## Methods

* [Generate](../../doc/controllers/attributes-and-elements-model.md#generate)
* [Validate](../../doc/controllers/attributes-and-elements-model.md#validate)
* [Generate Array](../../doc/controllers/attributes-and-elements-model.md#generate-array)
* [Validate Array](../../doc/controllers/attributes-and-elements-model.md#validate-array)


# Generate

This endpoint returns an XML document that should perfectly map onto the "AttributesAndElements" model

```python
def generate(self)
```

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`AttributesAndElements`](../../doc/models/attributes-and-elements.md).

## Example Usage

```python
result = attributes_and_elements_model_controller.generate()

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# Validate

This endpoint expects an XML document that should perfectly map onto the "AttributesAndElements" model

```python
def validate(self,
            body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`AttributesAndElements`](../../doc/models/attributes-and-elements.md) | Body, Required | - |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`ServerResponse`](../../doc/models/server-response.md).

## Example Usage

```python
body = AttributesAndElements(
    string_attr='string-attr8',
    number_attr=70,
    string_element='string-element4',
    number_element=164
)

result = attributes_and_elements_model_controller.validate(body)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# Generate Array

This endpoint returns an XML document that should perfectly map onto the "AttributesAndElements" model array

```python
def generate_array(self)
```

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`List[AttributesAndElements]`](../../doc/models/attributes-and-elements.md).

## Example Usage

```python
result = attributes_and_elements_model_controller.generate_array()

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# Validate Array

This endpoint expects an XML document that should perfectly map onto the "AttributesAndElements" model array

```python
def validate_array(self,
                  body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`List[AttributesAndElements]`](../../doc/models/attributes-and-elements.md) | Body, Required | - |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`ServerResponse`](../../doc/models/server-response.md).

## Example Usage

```python
body = [
    AttributesAndElements(
        string_attr='string-attr8',
        number_attr=70,
        string_element='string-element4',
        number_element=164
    )
]

result = attributes_and_elements_model_controller.validate_array(body)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

