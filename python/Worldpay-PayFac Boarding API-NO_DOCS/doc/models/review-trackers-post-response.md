
# Review Trackers Post Response

## Structure

`ReviewTrackersPostResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `correlation_id` | `str` | Optional | guid sent in the httpheader v-correlation-id |
| `http_status_code` | `str` | Optional | - |
| `http_status_message` | `str` | Optional | - |
| `enable_review_trackers` | `bool` | Optional | - |

## Example (as JSON)

```json
{
  "enableReviewTrackers": true,
  "correlationId": "correlationId6",
  "httpStatusCode": "httpStatusCode2",
  "httpStatusMessage": "httpStatusMessage6"
}
```

