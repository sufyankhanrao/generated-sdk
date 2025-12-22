# API

```python
client_controller = client.client
```

## Class Name

`APIController`


# Get Enums

```python
def get_enums(self,
             test_case=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `test_case` | [`TestCaseEnum`](../../doc/models/test-case-enum.md) | Query, Optional | - |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`EnumsAllowAdditionalResponse`](../../doc/models/enums-allow-additional-response.md).

## Example Usage

```python
result = client_controller.get_enums()

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

