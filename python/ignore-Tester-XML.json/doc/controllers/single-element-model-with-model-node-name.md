# Single Element Model With Model Node Name

```python
single_element_model_with_model_node_name_controller = client.single_element_model_with_model_node_name
```

## Class Name

`SingleElementModelWithModelNodeName`

## Methods

* [Generate](../../doc/controllers/single-element-model-with-model-node-name.md#generate)
* [Validate](../../doc/controllers/single-element-model-with-model-node-name.md#validate)


# Generate

This endpoint returns an XML document that should perfectly map onto the "Simple Elements" model

```python
def generate(self)
```

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`SingleElementWithNodeName`](../../doc/models/single-element-with-node-name.md).

## Example Usage

```python
result = single_element_model_with_model_node_name_controller.generate()

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
| `body` | [`SingleElementWithNodeName`](../../doc/models/single-element-with-node-name.md) | Body, Required | - |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`ServerResponse`](../../doc/models/server-response.md).

## Example Usage

```python
body = SingleElementWithNodeName(
    string_element='string-element4'
)

result = single_element_model_with_model_node_name_controller.validate(body)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

