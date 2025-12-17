
# PIN Reminder Card Details

Request entity object for PINReminderCardDetails

## Structure

`PINReminderCardDetails`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `card_id` | `int` | Optional | Card Id<br>Optional if Either PANID AND CardExpiryDate or PAN AND CardExpiryDate is passed, else Mandatory. Example: 275549 .<br/>Note:PANID, PAN & ExpiryDate parameters will be ignored if CardId is provided. |
| `panid` | `int` | Optional | PAN ID - Unique PAN ID<br>Optional if Either CardId or PAN AND  ExpiryDate is passed, else Mandatory. Example: 123456. <br/>Note:PANID parameter will be considered only if CardId is not provided |
| `pan` | `str` | Optional | PAN of the card.<br>Optional if Either CardId or PANID is passed, else Mandatory. <br/>Note:PAN & ExpiryDate parameters will be considered only if CardId & PANID are not provided |
| `card_expiry_date` | `str` | Optional | Expiry date of the card.<br>Mandatory if Either PAN or PANID is passed, else optional.<br>Format: yyyyMMdd |
| `pin_advice_type` | `int` | Required | PIN delivery method.<br>Mandatory<br>Allowed Values:<br><br>1. Paper<br><br>2. Email<br><br>3. SMS<br><br>**Constraints**: `>= 1`, `<= 3` |
| `pin_contact_type` | `int` | Optional | PIN Contact Type.<br>Mandatory<br>Allowed Values:<br><br>1. Use PIN Delivery contact details stored previously for this card<br>2. Use Card Delivery contact details stored previously for this card<br>3. Use default PIN Delivery contact details stored for this customer<br>4. Use new specific contact for PIN Reminder only<br><br>Note: - PINContactType “3” is only allowed for Paper delivery<br><br>**Constraints**: `>= 1`, `<= 4` |
| `pin_deliver_to` | [`PINDeliverTo`](../../doc/models/pin-deliver-to.md) | Optional | - |

## Example (as JSON)

```json
{
  "CardId": 104,
  "PANID": 136,
  "PAN": "PAN6",
  "CardExpiryDate": "CardExpiryDate2",
  "PINAdviceType": 3,
  "PINContactType": 4
}
```

