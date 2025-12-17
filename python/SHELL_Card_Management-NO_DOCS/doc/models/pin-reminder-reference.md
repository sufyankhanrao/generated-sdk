
# PIN Reminder Reference

This class holds the PIN Reminder References

## Structure

`PINReminderReference`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `card_id` | `int` | Optional | Card Id |
| `panid` | `int` | Optional | PAN ID |
| `pan` | `int` | Optional | PAN |
| `card_expiry_date` | `str` | Optional | Expiry date of the card.<br>Mandatory if Either PAN or PANID is passed, else optional.<br>Format: yyyyMMdd |
| `reference_id` | `int` | Optional | Individual card pin reminder reference number for the Pin Reminder request. |

## Example (as JSON)

```json
{
  "CardId": 122,
  "PANID": 154,
  "PAN": 52,
  "CardExpiryDate": "CardExpiryDate4",
  "ReferenceId": 46
}
```

