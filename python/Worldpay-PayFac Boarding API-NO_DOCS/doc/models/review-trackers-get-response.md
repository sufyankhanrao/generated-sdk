
# Review Trackers Get Response

## Structure

`ReviewTrackersGetResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `correlation_id` | `str` | Optional | guid sent in the httpheader v-correlation-id |
| `http_status_code` | `str` | Optional | - |
| `http_status_message` | `str` | Optional | - |
| `enable_review_trackers` | `bool` | Optional | - |
| `opt_in_date` | `str` | Optional | Opt in date |
| `opt_out_date` | `str` | Optional | Opt out date |
| `bill_start_date` | `str` | Optional | Bill start date |

## Example (as JSON)

```json
{
  "enableReviewTrackers": true,
  "optInDate": "2006-06-22",
  "optOutDate": "2006-12-22",
  "billStartDate": "2006-08-22",
  "correlationId": "correlationId0",
  "httpStatusCode": "httpStatusCode6",
  "httpStatusMessage": "httpStatusMessage0"
}
```

