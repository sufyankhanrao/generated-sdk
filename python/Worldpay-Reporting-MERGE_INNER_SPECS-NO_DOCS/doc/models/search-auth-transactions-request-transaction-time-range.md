
# Search Auth Transactions Request Transaction Time Range

Real-Time requests can only search on the current date and time (1 day). The From and To time fields must be set to the same date, to search on transaction details occurring on that day in real-time.

## Structure

`SearchAuthTransactionsRequestTransactionTimeRange`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `from_time` | `str` | Optional | Starting period of time<br><br>**Constraints**: *Maximum Length*: `8` |
| `to_time` | `str` | Optional | Ending period of time<br><br>**Constraints**: *Maximum Length*: `8` |

## Example (as JSON)

```json
{
  "fromTime": "08:59:45",
  "toTime": "39589"
}
```

