
# Entity Returns Payment

The identifier of the Payment that this EntityReturns refers to.

## Structure

`EntityReturnsPayment`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `method` | [`EntityReturnsPaymentMethodEnum`](../../doc/models/entity-returns-payment-method-enum.md) | Optional | The account method used to issue the return.<br><br><details><br><summary>Valid Values</summary><br>- `8` - **Checking account**<br>- `9` - **Savings account**<br>- `10` - **Corporate checking account**<br>- `11` - **Corporate savings account**<br></details><br> |
| `number` | `Any` | Optional | - |
| `routing` | `Any` | Optional | - |

## Example (as JSON)

```json
{
  "method": 10,
  "number": {
    "key1": "val1",
    "key2": "val2"
  },
  "routing": {
    "key1": "val1",
    "key2": "val2"
  }
}
```

