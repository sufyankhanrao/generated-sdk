
# Txns Payment

The payment method associated with this Transaction, including the card details.

## Structure

`TxnsPayment`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `method` | [`TxnPaymentMethodEnum`](../../doc/models/txn-payment-method-enum.md) | Required | The payment method for this Transaction. |
| `number` | `str` | Required | For credit payment method, the card number of the credit card associated with this Transaction.<br>For eCheck payment method, the bank account number associated with this Transaction. |
| `routing` | `str` | Optional | The routing code for the eCheck or bank account payment associated with this Transaction. |
| `expiration` | `str` | Optional | The expiration date of the credit card associated with this Transaction.<br>This field is stored as a text string in 'MMYY' format, where 'MM' is the number of a month and 'YY' is the last two digits of a year. For example, '0623' for June 2023. |
| `cvv` | `int` | Optional | The Card Verification Value (CVV) number of the credit card associated with this Transaction.<br>This field is expressed as an integer.<br><br>**Default**: `0` |
| `track` | `Any` | Optional | The 'Track' data (either Track 1, Track 2, or both) of the card associated with this Transaction.<br>This field is stored as a text string. |

## Example (as JSON)

```json
{
  "method": 15,
  "number": "number4",
  "cvv": 0,
  "routing": "routing2",
  "expiration": "expiration0",
  "track": {
    "key1": "val1",
    "key2": "val2"
  }
}
```

