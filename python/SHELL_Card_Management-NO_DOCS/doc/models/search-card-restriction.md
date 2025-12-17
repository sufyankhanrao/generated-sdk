
# Search Card Restriction

## Structure

`SearchCardRestriction`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `card_id` | `int` | Optional | Unique Card Id<br>Optional if PAN is given, else mandatory. |
| `pan` | `str` | Optional | Card PAN.<br>Optional if CardId is given, else mandatory.<br>Note: PAN is ignored if CardId is given.<br>Example: 7002051006629890645 |

## Example (as JSON)

```json
{
  "CardId": 186,
  "PAN": "PAN4"
}
```

