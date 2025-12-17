
# Accepted Cards Get Response

## Structure

`AcceptedCardsGetResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `correlation_id` | `str` | Optional | guid sent in the httpheader v-correlation-id |
| `http_status_code` | `str` | Optional | - |
| `http_status_message` | `str` | Optional | - |
| `accepted_cards` | [`List[AcceptedCard]`](../../doc/models/accepted-card.md) | Optional | - |

## Example (as JSON)

```json
{
  "correlationId": "correlationId8",
  "httpStatusCode": "httpStatusCode4",
  "httpStatusMessage": "httpStatusMessage8",
  "acceptedCards": [
    {
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
      "type": "FleetCor"
    }
  ]
}
```

