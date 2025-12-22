# Named Elements Array

```python
named_elements_array_controller = client.named_elements_array
```

## Class Name

`NamedElementsArray`

## Methods

* [Generate](../../doc/controllers/named-elements-array.md#generate)
* [Validate](../../doc/controllers/named-elements-array.md#validate)


# Generate

Generate

```python
def generate(self)
```

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`SimpleArrayWithElementName`](../../doc/models/simple-array-with-element-name.md).

## Example Usage

```python
result = named_elements_array_controller.generate()

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# Validate

This endpoint expects an XML document that should perfectly map onto the "simpleArrayWithElementName" model

```python
def validate(self,
            body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`SimpleArrayWithElementName`](../../doc/models/simple-array-with-element-name.md) | Body, Required | - |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`ServerResponse`](../../doc/models/server-response.md).

## Example Usage

```python
body = SimpleArrayWithElementName(
    elem=[
        'elem5'
    ]
)

result = named_elements_array_controller.validate(body)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

