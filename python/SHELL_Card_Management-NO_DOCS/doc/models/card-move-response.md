
# Card Move Response

## Structure

`CardMoveResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `move_card_request_reference` | `int` | Optional | - |
| `successful_requests` | [`List[CardMoveResponseSuccessfulRequestsItems]`](../../doc/models/card-move-response-successful-requests-items.md) | Optional | - |
| `error_cards` | [`List[CardMoveResponseErrorCardsItems]`](../../doc/models/card-move-response-error-cards-items.md) | Optional | - |
| `request_id` | `str` | Optional | - |
| `error` | [`ErrorStatus`](../../doc/models/error-status.md) | Optional | - |

## Example (as JSON)

```json
{
  "MoveCardRequestReference": 70,
  "SuccessfulRequests": [
    {
      "AccountNumber": "AccountNumber8",
      "AccountId": 112,
      "PAN": "PAN0",
      "CardId": 18,
      "MoveCardReference": 248
    }
  ],
  "ErrorCards": [
    {
      "AccountNumber": "AccountNumber4",
      "AccountId": 230,
      "PAN": "PAN6",
      "CardId": 136,
      "ValidationErrorCode": "ValidationErrorCode6"
    },
    {
      "AccountNumber": "AccountNumber4",
      "AccountId": 230,
      "PAN": "PAN6",
      "CardId": 136,
      "ValidationErrorCode": "ValidationErrorCode6"
    }
  ],
  "RequestId": "RequestId2",
  "Error": {
    "Code": "Code4",
    "Description": "Description2"
  }
}
```

