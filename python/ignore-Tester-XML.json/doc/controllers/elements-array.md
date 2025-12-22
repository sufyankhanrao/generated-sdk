# Elements Array

```python
elements_array_controller = client.elements_array
```

## Class Name

`ElementsArray`

## Methods

* [Generate](../../doc/controllers/elements-array.md#generate)
* [Validate](../../doc/controllers/elements-array.md#validate)


# Generate

Generate

```python
def generate(self)
```

## Response Type

[`SimpleArray`](../../doc/models/simple-array.md)

## Example Usage

```python
result = elements_array_controller.generate()
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
| `body` | [`SimpleArray`](../../doc/models/simple-array.md) | Body, Required | - |

## Response Type

[`ServerResponse`](../../doc/models/server-response.md)

## Example Usage

```python
body = SimpleArray(
    elem=[
        'elem5'
    ]
)

result = elements_array_controller.validate(body)
print(result)
```

