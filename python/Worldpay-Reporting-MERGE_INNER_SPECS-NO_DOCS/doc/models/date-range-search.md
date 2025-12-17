
# Date Range Search

Specify the date range for search. Consumer can search upto 60 days of data in a single request.

## Structure

`DateRangeSearch`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `from_date` | `str` | Required | Refer to the starting date of a particular period<br><br>**Constraints**: *Minimum Length*: `10`, *Maximum Length*: `10`, *Pattern*: `^[0-9]{4}-[0-9]{2}-[0-9]{2}$` |
| `to_date` | `str` | Required | Refer to the period of time up until the current date<br><br>**Constraints**: *Minimum Length*: `10`, *Maximum Length*: `10`, *Pattern*: `^[0-9]{4}-[0-9]{2}-[0-9]{2}$` |

## Example (as JSON)

```json
{
  "fromDate": "2021-12-01",
  "toDate": "2021-12-01"
}
```

