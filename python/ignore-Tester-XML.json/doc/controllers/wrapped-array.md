# Wrapped Array

```python
wrapped_array_controller = client.wrapped_array
```

## Class Name

`WrappedArray`

## Methods

* [Generate](../../doc/controllers/wrapped-array.md#generate)
* [Validate](../../doc/controllers/wrapped-array.md#validate)


# Generate

Generate

```python
def generate(self)
```

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`WrappedArrayWithElementName`](../../doc/models/wrapped-array-with-element-name.md).

## Example Usage

```python
result = wrapped_array_controller.generate()

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# Validate

This endpoint expects an XML document that should perfectly map onto the "simpleArray" model

```python
def validate(self,
            body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`WrappedArrayWithElementName`](../../doc/models/wrapped-array-with-element-name.md) | Body, Required | - |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`ServerResponse`](../../doc/models/server-response.md).

## Example Usage

```python
body = WrappedArrayWithElementName(
    elem=[
        'elem5'
    ]
)

result = wrapped_array_controller.validate(body)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

