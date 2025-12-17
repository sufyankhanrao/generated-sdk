
# Order Card Request

This entity models the data that is sent in the http request body for this operation.

## Structure

`OrderCardRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `card_details` | [`List[CardDetail]`](../../doc/models/card-detail.md) | Optional | List of CardOrder entity. The fields in this entity are described below. |

## Example (as JSON)

```json
{
  "CardDetails": [
    {
      "PayerId": 232,
      "PayerNumber": "PayerNumber2",
      "AccountId": 36,
      "AccountNumber": "AccountNumber4",
      "ColCoCode": 198,
      "CardDeliveryType": 2,
      "PINAdviceType": 4
    },
    {
      "PayerId": 232,
      "PayerNumber": "PayerNumber2",
      "AccountId": 36,
      "AccountNumber": "AccountNumber4",
      "ColCoCode": 198,
      "CardDeliveryType": 2,
      "PINAdviceType": 4
    }
  ]
}
```

