# Template Params

```python
template_params_controller = client.template_params
```

## Class Name

`TemplateParamsController`

## Methods

* [Send String Array](../../doc/controllers/template-params.md#send-string-array)
* [Send Integer Array](../../doc/controllers/template-params.md#send-integer-array)


# Send String Array

```python
def send_string_array(self,
                     strings)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `strings` | `List[str]` | Template, Required | - |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`EchoResponse`](../../doc/models/echo-response.md).

## Example Usage

```python
strings = [
    'strings5'
]

result = template_params_controller.send_string_array(strings)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# Send Integer Array

```python
def send_integer_array(self,
                      integers)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `integers` | `List[int]` | Template, Required | - |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`EchoResponse`](../../doc/models/echo-response.md).

## Example Usage

```python
integers = [
    45,
    46,
    47
]

result = template_params_controller.send_integer_array(integers)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

