
# Terminal Txns Payment

The payment method associated with this Transaction, including the card details.

## Structure

`TerminalTxnsPayment`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `method` | [`TerminalTxnPaymentMethodEnum`](../../doc/models/terminal-txn-payment-method-enum.md) | Optional | The payment method for this Transaction. |
| `number` | `str` | Optional | The last four numbers of the credit card associated with this Transaction. |
| `routing` | `str` | Optional | The routing code for the eCheck or bank account payment associated with this Transaction. |
| `expiration` | `str` | Optional | The expiration date of the credit card associated with this Transaction. This field is stored as a text string in 'MMYY' format, where 'MM' is the number of a month and 'YY' is the last two digits of a year. For example, '0623' for June 2023. |
| `cvv` | `int` | Optional | The Card Verification Value (CVV) number of the credit card associated with this Transaction. This field is expressed as an integer. |
| `track` | `str` | Optional | The 'Track' data (either Track 1, Track 2, or both) of the card associated with this Transaction. This field is stored as a text string. |

## Example (as JSON)

```json
{
  "method": 1,
  "number": "number0",
  "routing": "routing8",
  "expiration": "expiration4",
  "cvv": 46
}
```

