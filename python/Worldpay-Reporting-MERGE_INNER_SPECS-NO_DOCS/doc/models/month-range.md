
# Month Range

Month Range for which the transaction is processed.

## Structure

`MonthRange`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `start_month` | `str` | Optional | Start month<br><br>**Constraints**: *Minimum Length*: `7`, *Maximum Length*: `7`, *Pattern*: `^[0-9]{4}-[0-9]{2}$` |
| `end_month` | `str` | Optional | End month. Maximum month range support 13 Months.<br><br>**Constraints**: *Minimum Length*: `7`, *Maximum Length*: `7`, *Pattern*: `^[0-9]{4}-[0-9]{2}$` |

## Example (as JSON)

```json
{
  "startMonth": "2022-01",
  "endMonth": "2022-06"
}
```

