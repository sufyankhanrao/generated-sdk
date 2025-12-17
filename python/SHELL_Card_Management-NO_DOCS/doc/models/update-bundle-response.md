
# Update Bundle Response

## Structure

`UpdateBundleResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `request_id` | `str` | Optional | Request Id of the API call |
| `request_action_status` | [`ErrorStatus`](../../doc/models/error-status.md) | Optional | - |
| `day_time_restriction_status` | [`ErrorStatus`](../../doc/models/error-status.md) | Optional | - |
| `location_restriction_status` | [`ErrorStatus`](../../doc/models/error-status.md) | Optional | - |
| `product_restriction_status` | [`ErrorStatus`](../../doc/models/error-status.md) | Optional | - |
| `usage_restriction_status` | [`ErrorStatus`](../../doc/models/error-status.md) | Optional | - |
| `error` | [`ErrorStatus`](../../doc/models/error-status.md) | Optional | - |

## Example (as JSON)

```json
{
  "RequestId": "2ace3991-5d03-4a68-ac68-ca9119b25101",
  "RequestActionStatus": {
    "Code": "Code6",
    "Description": "Description0"
  },
  "DayTimeRestrictionStatus": {
    "Code": "Code4",
    "Description": "Description2"
  },
  "LocationRestrictionStatus": {
    "Code": "Code6",
    "Description": "Description0"
  },
  "ProductRestrictionStatus": {
    "Code": "Code8",
    "Description": "Description8"
  }
}
```

