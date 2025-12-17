# Health

Resource to check the service availability.

```python
health_controller = client.health
```

## Class Name

`HealthController`


# Healthcheck

This URI will retrieve the health status of the PayFac submerchant provisioning APIs and will display if the status is UP or DOWN.

```python
def healthcheck(self,
               v_correlation_id,
               content_type="application/json")
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `v_correlation_id` | `uuid\|str` | Header, Required | The unique UUID that is sent in each request |
| `content_type` | `str` | Header, Optional | The original media type of the resource<br><br>**Default**: `"application/json"` |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`HealthCheckResponse`](../../doc/models/health-check-response.md).

## Example Usage

```python
v_correlation_id = '0000139e-0000-0000-0000-000000000000'

content_type = 'application/json'

result = health_controller.healthcheck(
    v_correlation_id,
    content_type=content_type
)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 500 | Server Error | [`M500ErrorResponseException`](../../doc/models/m500-error-response-exception.md) |
| 503 | Service Unavailable | `APIException` |

