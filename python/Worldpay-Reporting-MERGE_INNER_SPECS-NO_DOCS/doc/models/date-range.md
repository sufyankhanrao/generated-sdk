
# Date Range

The From and To Dates are required.  They are used to select all transaction data that fall within and including these dates.

## Structure

`DateRange`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `from_date` | `str` | Required | Start Date<br><br>**Constraints**: *Maximum Length*: `10`, *Pattern*: `[0-9]{4}-[0-9]{2}-[0-9]{2}` |
| `to_date` | `str` | Required | End Date<br><br>**Constraints**: *Maximum Length*: `10`, *Pattern*: `[0-9]{4}-[0-9]{2}-[0-9]{2}` |

## Example (as JSON)

```json
{
  "fromDate": "2019-10-27",
  "toDate": "2019-11-27"
}
```

