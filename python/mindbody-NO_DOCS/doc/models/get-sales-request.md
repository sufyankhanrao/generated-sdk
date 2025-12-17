
# Get Sales Request

## Structure

`GetSalesRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `sale_id` | `int` | Optional | The sale ID associated with the particular item. It Filters results to the requested sale ID. |
| `start_sale_date_time` | `datetime` | Optional | Filters results to sales that happened after this date and time. |
| `end_sale_date_time` | `datetime` | Optional | Filters results to sales that happened before this date and time. |
| `payment_method_id` | `int` | Optional | Filters results to sales paid for by the given payment method ID which indicates payment method(s) (i.e. cash, VISA, AMEX, Check, etc.). |
| `limit` | `int` | Optional | Number of results to include, defaults to 100 |
| `offset` | `int` | Optional | Page offset, defaults to 0. |

## Example (as JSON)

```json
{
  "SaleId": 234,
  "StartSaleDateTime": "2016-03-13T12:52:32.123Z",
  "EndSaleDateTime": "2016-03-13T12:52:32.123Z",
  "PaymentMethodId": 180,
  "Limit": 84
}
```

