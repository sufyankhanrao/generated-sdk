
# Card Day Time Restrictions

## Structure

`CardDayTimeRestrictions`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `level` | `str` | Optional | Describes at which level the restriction is set at.<br>Possible values:<br>OU = Restriction set at ColCo card type<br>Customer = Restriction set at customer card type |
| `monday` | `bool` | Optional | Whether the transaction is allowed on Mondays or not. |
| `tuesday` | `bool` | Optional | Whether the transaction is allowed on Tuesdays or not. |
| `wednesday` | `bool` | Optional | Whether the transaction is allowed on Wednesdays or not. |
| `thursday` | `bool` | Optional | Whether the transaction is allowed on Thursdays or not. |
| `friday` | `bool` | Optional | Whether the transaction is allowed on Fridays or not. |
| `saturday` | `bool` | Optional | Whether the transaction is allowed on Saturdays or not. |
| `sunday` | `bool` | Optional | Whether the transaction is allowed on Sundays or not. |
| `time_from` | `str` | Optional | The time in the day from when the transaction is allowed.<br>Format: HH:mm: ss<br>E.g., 21:00:00<br><br>Note:<br><br>1) The client application has to convert the value to the required date-time data type.<br>2) The value will be 00:00:00 when no restriction set for this field. |
| `time_to` | `str` | Optional | allowed.<br>Format: HH:mm: ss<br>E.g., 21:00:00<br><br>Note:<br><br>1) The client application has to convert the value to the required date-time data type.<br>2) The value will be 00:00:00 when no restriction set for this field. |

## Example (as JSON)

```json
{
  "Level": "OU= 24537",
  "TimeFrom": "07:56:00",
  "TimeTo": "08:19:09",
  "Monday": false,
  "Tuesday": false,
  "Wednesday": false,
  "Thursday": false
}
```

