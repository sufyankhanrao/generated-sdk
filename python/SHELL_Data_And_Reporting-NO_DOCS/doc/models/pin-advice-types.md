
# PIN Advice Types

## Structure

`PINAdviceTypes`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `pin_advice_type_id` | `int` | Optional | Id of of PIN advice type.<br>Possible Values:<br><br>1. Paper<br>2. Email<br>3. SMS<br>4. None |
| `is_card_order_option` | `bool` | Optional | Whether the PIN advice type is available for card ordering |
| `is_pin_reminder_option` | `bool` | Optional | Whether the PIN advice type is available for PIN Reminder |

## Example (as JSON)

```json
{
  "PINAdviceTypeID": 1,
  "IsCardOrderOption": false,
  "IsPINReminderOption": false
}
```

