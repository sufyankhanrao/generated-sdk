
# Recent Transactions Response

## Structure

`RecentTransactionsResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `request_id` | `str` | Optional | RequestID is unique identifier value that is attached to requests and messages that allow reference to a particular transaction or event chain. |
| `status` | `str` | Optional | status of the API call |
| `page` | `int` | Optional | CurrentPage |
| `row_count` | `int` | Optional | RowCount |
| `total_pages` | `int` | Optional | TotalPages |
| `data` | [`List[RecentTransactions]`](../../doc/models/recent-transactions.md) | Optional | API Response |

## Example (as JSON)

```json
{
  "RequestId": "9d2dee33-7803-485a-a2b1-2c7538e597ee",
  "Status": "SUCCESS",
  "Page": 1,
  "RowCount": 2,
  "TotalPages": 1
}
```

