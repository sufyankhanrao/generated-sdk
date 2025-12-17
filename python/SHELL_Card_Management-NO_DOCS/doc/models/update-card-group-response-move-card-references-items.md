
# Update Card Group Response Move Card References Items

## Structure

`UpdateCardGroupResponseMoveCardReferencesItems`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `card_id` | `int` | Optional | Card Id of the card.<br>Example: 123 |
| `pan` | `str` | Optional | PAN of the card.<br>Example: 7002051123456789145 |
| `reference` | `int` | Optional | Reference number for tracking of update status request of the specific card. |

## Example (as JSON)

```json
{
  "CardId": 2,
  "PAN": "PAN4",
  "Reference": 44
}
```

