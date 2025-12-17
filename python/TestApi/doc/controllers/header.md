# Header

```python
header_controller = client.header
```

## Class Name

`HeaderController`


# Send Headers

Sends a single header params

```python
def send_headers(self,
                custom_header,
                value)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `custom_header` | `str` | Header, Required | - |
| `value` | `str` | Form, Required | Represents the value of the custom header |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`ServerResponse`](../../doc/models/server-response.md).

## Example Usage

```python
custom_header = 'custom-header2'

value = 'value2'

result = header_controller.send_headers(
    custom_header,
    value
)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

