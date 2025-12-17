
# Sale Payment

## Structure

`SalePayment`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `int` | Optional | A unique identifier for this payment. |
| `amount` | `float` | Optional | The total amount of sales that were made on the sale date, including all payment methods that were used and taxes that were collected. |
| `method` | `int` | Optional | The method used to make this payment. |
| `mtype` | `str` | Optional | The payment method type used for the client’s purchase. |
| `notes` | `str` | Optional | Payment notes that are entered under the selected payment method in the Retail screen before completing the sale. |
| `transaction_id` | `int` | Optional | The ID of transaction. Use this ID when calling the GET Transactions endpoint. |

## Example (as JSON)

```json
{
  "Id": 138,
  "Amount": 228.76,
  "Method": 144,
  "Type": "Type4",
  "Notes": "Notes4"
}
```

