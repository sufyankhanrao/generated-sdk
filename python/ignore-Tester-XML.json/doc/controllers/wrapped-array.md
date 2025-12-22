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

[`WrappedArrayWithElementName`](../../doc/models/wrapped-array-with-element-name.md)

## Example Usage

```python
result = wrapped_array_controller.generate()
print(result)
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

[`ServerResponse`](../../doc/models/server-response.md)

## Example Usage

```python
body = WrappedArrayWithElementName(
    elem=[
        'elem5'
    ]
)

result = wrapped_array_controller.validate(body)
print(result)
```

