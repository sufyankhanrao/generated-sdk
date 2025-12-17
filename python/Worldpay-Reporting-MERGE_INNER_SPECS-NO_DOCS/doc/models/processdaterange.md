
# Processdaterange

Refers to number of dates that includes a particular start and end date and all dates in between specific periods of time.

## Structure

`Processdaterange`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `from_date` | `str` | Optional | Start Date<br><br>**Constraints**: *Maximum Length*: `10`, *Pattern*: `[0-9]{4}-[0-9]{2}-[0-9]{2}` |
| `to_date` | `str` | Optional | End Date<br><br>**Constraints**: *Maximum Length*: `10`, *Pattern*: `[0-9]{4}-[0-9]{2}-[0-9]{2}` |

## Example (as JSON)

```json
{
  "fromDate": "2021-12-01",
  "toDate": "2021-12-01"
}
```

