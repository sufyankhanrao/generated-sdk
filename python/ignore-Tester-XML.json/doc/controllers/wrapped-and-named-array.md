# Wrapped and Named Array

```python
wrapped_and_named_array_controller = client.wrapped_and_named_array
```

## Class Name

`WrappedAndNamedArray`

## Methods

* [Generate](../../doc/controllers/wrapped-and-named-array.md#generate)
* [Validate](../../doc/controllers/wrapped-and-named-array.md#validate)


# Generate

Generate

```python
def generate(self)
```

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`WrappedArrayWithElementAndWrappingName`](../../doc/models/wrapped-array-with-element-and-wrapping-name.md).

## Example Usage

```python
result = wrapped_and_named_array_controller.generate()

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
| `body` | [`WrappedArrayWithElementAndWrappingName`](../../doc/models/wrapped-array-with-element-and-wrapping-name.md) | Body, Required | - |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`ServerResponse`](../../doc/models/server-response.md).

## Example Usage

```python
body = WrappedArrayWithElementAndWrappingName(
    elem=[
        'elem5'
    ]
)

result = wrapped_and_named_array_controller.validate(body)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

