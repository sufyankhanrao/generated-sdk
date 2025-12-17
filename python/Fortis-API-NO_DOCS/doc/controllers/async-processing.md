# Async Processing

```python
async_processing_controller = client.async_processing
```

## Class Name

`AsyncProcessingController`


# Status Check

Retrieve the current status for a particular code.

```python
def status_check(self,
                status_code)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `status_code` | `uuid\|str` | Template, Required | A [UUID v4](https://datatracker.ietf.org/doc/html/rfc4122) that's unique for the Async Request |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`ResponseAsyncStatus`](../../doc/models/response-async-status.md).

## Example Usage

```python
status_code = '406c66c3-21cb-47fb-80fc-843bc42507fb'

result = async_processing_controller.status_check(status_code)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Example Response *(as JSON)*

```json
{
  "type": "AsyncStatus",
  "data": {
    "code": "406c66c3-21cb-47fb-80fc-843bc42507fb",
    "type": "Transaction",
    "id": "11e95f8ec39de8fbdb0a4f1a",
    "progress": 100,
    "error": null,
    "ttl": 7956886942
  }
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized | [`Response401tokenException`](../../doc/models/response-401-token-exception.md) |

