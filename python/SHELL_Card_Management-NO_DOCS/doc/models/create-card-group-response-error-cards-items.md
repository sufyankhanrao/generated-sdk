
# Create Card Group Response Error Cards Items

## Structure

`CreateCardGroupResponseErrorCardsItems`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `card_id` | `int` | Optional | Card Id of the card. |
| `pan` | `str` | Optional | PAN of the card. |
| `error_code` | `str` | Optional | Error code for validation failure. |
| `error_description` | `str` | Optional | Description of validation failure. |

## Example (as JSON)

```json
{
  "CardId": 66,
  "PAN": "PAN2",
  "ErrorCode": "ErrorCode6",
  "ErrorDescription": "ErrorDescription2"
}
```

