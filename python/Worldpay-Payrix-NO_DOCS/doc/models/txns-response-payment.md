
# Txns Response Payment

The payment method associated with this Transaction, including the card details.

## Structure

`TxnsResponsePayment`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Optional | - |
| `method` | [`TxnPaymentMethodEnum`](../../doc/models/txn-payment-method-enum.md) | Optional | The payment method for this Transaction. |
| `number` | `str` | Optional | For credit payment method, the card number of the credit card associated with this Transaction.<br>For eCheck payment method, the bank account number associated with this Transaction. |
| `last_4` | `str` | Optional | - |
| `routing` | `str` | Optional | The routing code for the eCheck or bank account payment associated with this Transaction. |
| `bin` | `str` | Optional | - |
| `payment` | `str` | Optional | - |
| `last_checked` | `str` | Optional | - |
| `mask` | `str` | Optional | - |

## Example (as JSON)

```json
{
  "id": "id6",
  "method": 18,
  "number": "number4",
  "last4": "last42",
  "routing": "routing2"
}
```

