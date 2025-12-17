
# Accepted Cards Type Get Response

## Structure

`AcceptedCardsTypeGetResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `correlation_id` | `str` | Optional | guid sent in the httpheader v-correlation-id |
| `http_status_code` | `str` | Optional | - |
| `http_status_message` | `str` | Optional | - |
| `accepted_card` | [`AcceptedCard`](../../doc/models/accepted-card.md) | Optional | - |

## Example (as JSON)

```json
{
  "correlationId": "correlationId2",
  "httpStatusCode": "httpStatusCode2",
  "httpStatusMessage": "httpStatusMessage2",
  "acceptedCard": {
    "attributes": [
      {
        "name": "name4",
        "value": "value6"
      },
      {
        "name": "name4",
        "value": "value6"
      },
      {
        "name": "name4",
        "value": "value6"
      }
    ],
    "type": "EBT"
  }
}
```

