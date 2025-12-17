
# Card Restriction Response

## Structure

`CardRestrictionResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `request_id` | `str` | Optional | Request Id of the API call |
| `restriction_request_reference` | `float` | Optional | Reference number for tracking the execution of the card restriction requests. |
| `cards` | [`List[RestrictioncardsRes]`](../../doc/models/restrictioncards-res.md) | Optional | - |
| `error` | [`ErrorStatus`](../../doc/models/error-status.md) | Optional | - |

## Example (as JSON)

```json
{
  "RequestId": "2ace3991-5d03-4a68-ac68-ca9119b25101",
  "RestrictionRequestReference": 140.46,
  "Cards": [
    {
      "AccountId": 184,
      "AccountNumber": "AccountNumber8",
      "CardId": "CardId8",
      "PAN": "PAN0",
      "UsageRestrictionStatus": "UsageRestrictionStatus8"
    },
    {
      "AccountId": 184,
      "AccountNumber": "AccountNumber8",
      "CardId": "CardId8",
      "PAN": "PAN0",
      "UsageRestrictionStatus": "UsageRestrictionStatus8"
    },
    {
      "AccountId": 184,
      "AccountNumber": "AccountNumber8",
      "CardId": "CardId8",
      "PAN": "PAN0",
      "UsageRestrictionStatus": "UsageRestrictionStatus8"
    }
  ],
  "Error": {
    "Code": "Code4",
    "Description": "Description2"
  }
}
```

