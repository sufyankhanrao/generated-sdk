
# Search Auth Transactions Request Real Time Transaction Date Range

Real-Time requests can only search on the current date (1 day). The From and To Date fields must be set to the same date, to search on transaction details occurring on that day in real-time.

## Structure

`SearchAuthTransactionsRequestRealTimeTransactionDateRange`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `from_date` | `str` | Optional | Start date<br><br>**Constraints**: *Minimum Length*: `10`, *Maximum Length*: `10`, *Pattern*: `^[0-9]{4}-[0-9]{2}-[0-9]{2}$` |
| `to_date` | `str` | Optional | End date<br><br>**Constraints**: *Minimum Length*: `10`, *Maximum Length*: `10`, *Pattern*: `^[0-9]{4}-[0-9]{2}-[0-9]{2}$` |

## Example (as JSON)

```json
{
  "fromDate": "2021-12-01",
  "toDate": "2021-12-01"
}
```

