
# Transaction

## Structure

`Transaction`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `transaction_id` | `int` | Optional | The transaction ID. |
| `sale_id` | `int` | Optional | The sale ID. |
| `client_id` | `int` | Optional | The ID of the client who made the purchase. |
| `amount` | `float` | Optional | The amount charged on the card |
| `settled` | `bool` | Optional | Whether it is settled or not |
| `status` | `str` | Optional | Status of the transaction |
| `transaction_time` | `datetime` | Optional | Time of card swiped |
| `auth_time` | `datetime` | Optional | Time of card authorized |
| `location_id` | `int` | Optional | The ID of the location where the sale takes place. |
| `merchant_id` | `str` | Optional | Merchant ID of the studio |
| `terminal_id` | `str` | Optional | Terminal ID used for payment. Not applicable for CNP/Bank |
| `card_expiration_month` | `str` | Optional | Expiry month of the card |
| `card_expiration_year` | `str` | Optional | Expiry year of the card |
| `cc_last_four` | `str` | Optional | Last 4 digits of CC |
| `card_type` | `str` | Optional | Type of the card |
| `cc_swiped` | `bool` | Optional | Whether card is swiped or not |
| `ach_last_four` | `str` | Optional | Customer’s ACH last 4 digits |

## Example (as JSON)

```json
{
  "TransactionId": 78,
  "SaleId": 116,
  "ClientId": 136,
  "Amount": 19.46,
  "Settled": false
}
```

