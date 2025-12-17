
# Fulfillment Callback

## Structure

`FulfillmentCallback`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `order_id` | `str` | Required | - |
| `fulfillment_status` | [`FulfillmentStatusEnum`](../../doc/models/fulfillment-status-enum.md) | Required | - |
| `tracking_number` | `str` | Optional | - |
| `carrier` | `str` | Optional | - |
| `estimated_delivery` | `date` | Optional | - |
| `timestamp` | `datetime` | Optional | - |

## Example (as JSON)

```json
{
  "orderId": "order_789",
  "fulfillmentStatus": "fulfilled",
  "trackingNumber": "TRK123456789",
  "carrier": "FedEx",
  "estimatedDelivery": "2025-09-22",
  "timestamp": "09/19/2025 14:00:00"
}
```

