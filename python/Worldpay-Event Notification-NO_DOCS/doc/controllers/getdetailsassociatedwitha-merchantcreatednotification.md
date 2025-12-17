# Getdetailsassociatedwitha Merchantcreatednotification

```python
getdetailsassociatedwitha_merchantcreatednotification_controller = client.getdetailsassociatedwitha_merchantcreatednotification
```

## Class Name

`GetdetailsassociatedwithaMerchantcreatednotificationController`


# Get Notification Details

Retrieves the merchant created notification details associated with given notification ID

```python
def get_notification_details(self,
                            v_correlation_id,
                            notification_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `v_correlation_id` | `uuid\|str` | Header, Required | Correlation Id |
| `notification_id` | `str` | Template, Required | Unique identifier code for the notification.<br><br>**Constraints**: *Maximum Length*: `10` |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`NewMerchantAccountNotification`](../../doc/models/new-merchant-account-notification.md).

## Example Usage

```python
v_correlation_id = '24578e35-9bd2-238f-b4c2-0bc9ad9aed2b'

notification_id = '123456'

result = get_details_associated_with_a_merchant_created_notification_controller.get_notification_details(
    v_correlation_id,
    notification_id
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

