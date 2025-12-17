
# Get Transactions Request

Transactions Request

## Structure

`GetTransactionsRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `sale_id` | `int` | Optional | Filters the transaction results with the ID number associated with the sale. |
| `transaction_id` | `int` | Optional | Filters the transaction results with the ID number generated when the sale is processed. |
| `client_id` | `int` | Optional | Filters results to the requested client ID. |
| `location_id` | `int` | Optional | Filters the transaction results with the ID number associated with the location of the sale. |
| `status` | `str` | Optional | Filters the transaction results by the estimated transaction status. |
| `transaction_start_date_time` | `datetime` | Optional | Filters the transaction results that happpened after this date and time.<br>Default: **today’s date** |
| `transaction_end_date_time` | `datetime` | Optional | Filters the transaction results that happpened before this date and time.<br>Default: **today’s date** |
| `limit` | `int` | Optional | Number of results to include, defaults to 100 |
| `offset` | `int` | Optional | Page offset, defaults to 0. |

## Example (as JSON)

```json
{
  "SaleId": 2,
  "TransactionId": 192,
  "ClientId": 6,
  "LocationId": 146,
  "Status": "Status0"
}
```

