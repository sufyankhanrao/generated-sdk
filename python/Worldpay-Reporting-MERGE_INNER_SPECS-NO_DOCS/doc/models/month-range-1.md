
# Month Range 1

Month range for which data is to be retrieved. Maximum month range supported is 13 months.

## Structure

`MonthRange1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `start_month` | `str` | Optional | Start month<br><br>**Constraints**: *Maximum Length*: `7`, *Pattern*: `^[0-9]{4}-[0-9]{2}$` |
| `end_month` | `str` | Optional | End month. Maximum month range supported is 13 months.<br><br>**Constraints**: *Maximum Length*: `7`, *Pattern*: `^[0-9]{4}-[0-9]{2}$` |

## Example (as JSON)

```json
{
  "startMonth": "2022-01",
  "endMonth": "2022-06"
}
```

