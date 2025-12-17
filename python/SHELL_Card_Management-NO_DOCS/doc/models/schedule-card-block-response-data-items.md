
# Schedule Card Block Response Data Items

## Structure

`ScheduleCardBlockResponseDataItems`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `card_id` | `int` | Optional | Unique Id of the card. |
| `from_date` | `str` | Optional | Effective start date & time of Block / Unblock as updated in the intermediate queue table.<br><br>Format: yyyyMMdd HH:mm<br>Eg: 20230512 12:30 |
| `to_date` | `str` | Optional | Effective end date & time of Block / Unblock as updated in the intermediate queue table.<br><br>Format: yyyyMMdd HH:mm<br>Eg: 20230512 14:30 |
| `reference_id` | `int` | Optional | Effective end date & time of Block / Unblock as updated in the intermediate queue table.<br><br>Format: yyyyMMdd HH:mm<br>Eg: 20230512 14:30 |

## Example (as JSON)

```json
{
  "CardId": 86,
  "FromDate": "FromDate8",
  "ToDate": "ToDate8",
  "ReferenceId": 10
}
```

