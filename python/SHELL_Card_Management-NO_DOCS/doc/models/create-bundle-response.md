
# Create Bundle Response

## Structure

`CreateBundleResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `request_id` | `str` | Optional | Request Id of the API call |
| `bundle_creation_status` | [`ErrorStatus`](../../doc/models/error-status.md) | Optional | - |
| `bundle_id` | `str` | Optional | Identifier of the newly created bundle |
| `day_time_restriction_status` | [`ErrorStatus`](../../doc/models/error-status.md) | Optional | - |
| `day_time_restriction_profile_id` | `str` | Optional | Identifier of the day/time restriction profile created |
| `location_restriction_status` | [`ErrorStatus`](../../doc/models/error-status.md) | Optional | - |
| `location_restriction_profile_id` | `str` | Optional | Identifier of the location restriction profile created |
| `usage_restriction_status` | [`ErrorStatus`](../../doc/models/error-status.md) | Optional | - |
| `product_restriction_status` | [`ErrorStatus`](../../doc/models/error-status.md) | Optional | - |
| `cards` | [`BundleCardRestrictionStatus`](../../doc/models/bundle-card-restriction-status.md) | Optional | - |
| `error` | [`ErrorStatus`](../../doc/models/error-status.md) | Optional | - |

## Example (as JSON)

```json
{
  "RequestId": "2ace3991-5d03-4a68-ac68-ca9119b25101",
  "BundleCreationStatus": {
    "Code": "Code8",
    "Description": "Description8"
  },
  "BundleId": "BundleId2",
  "DayTimeRestrictionStatus": {
    "Code": "Code4",
    "Description": "Description2"
  },
  "DayTimeRestrictionProfileId": "DayTimeRestrictionProfileId0"
}
```

