
# Search Auth Transactions Request Transaction Date Range

Non-Real-Time requests allow for multiple day searches and will search for all transactions that occur on or between the dates given.

## Structure

`SearchAuthTransactionsRequestTransactionDateRange`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `from_date` | `str` | Optional | Start date<br><br>**Constraints**: *Minimum Length*: `10`, *Maximum Length*: `10`, *Pattern*: `^[0-9]{4}-[0-9]{2}-[0-9]{2}$` |
| `to_date` | `str` | Optional | End date<br><br>**Constraints**: *Minimum Length*: `10`, *Maximum Length*: `10`, *Pattern*: `^[0-9]{4}-[0-9]{2}-[0-9]{2}$` |

## Example (as JSON)

```json
{
  "fromDate": "2021-12-01",
  "toDate": "2022-01-01"
}
```

