# Complete Notification

```python
complete_notification_controller = client.complete_notification
```

## Class Name

`CompleteNotificationController`


# Acknowledge Notification

Complete an event notification with a success message or detailed error message in case of processing failure

```python
def acknowledge_notification(self,
                            v_correlation_id,
                            notification_id,
                            body=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `v_correlation_id` | `uuid\|str` | Header, Required | Correlation Id |
| `notification_id` | `int` | Template, Required | Notification ID |
| `body` | [`AcknowledgeRequest`](../../doc/models/acknowledge-request.md) | Body, Optional | - |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`AcknowledgeResponse`](../../doc/models/acknowledge-response.md).

## Example Usage

```python
v_correlation_id = '24578e35-9bd2-238f-b4c2-0bc9ad9aed2b'

notification_id = 123456

body = AcknowledgeRequest(
    http_status_code='200',
    http_status_message='OK'
)

result = complete_notification_controller.acknowledge_notification(
    v_correlation_id,
    notification_id,
    body=body
)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| Default | Default errors | [`ErrorResponseException`](../../doc/models/error-response-exception.md) |

