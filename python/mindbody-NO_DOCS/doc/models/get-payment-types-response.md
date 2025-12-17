
# Get Payment Types Response

Get Payment Types Response Model

## Structure

`GetPaymentTypesResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `payment_types` | [`List[PaymentType]`](../../doc/models/payment-type.md) | Optional | The requested payment types. |

## Example (as JSON)

```json
{
  "PaymentTypes": [
    {
      "Id": 2,
      "PaymentTypeName": "PaymentTypeName8",
      "Active": false,
      "Fee": 197.82
    },
    {
      "Id": 2,
      "PaymentTypeName": "PaymentTypeName8",
      "Active": false,
      "Fee": 197.82
    },
    {
      "Id": 2,
      "PaymentTypeName": "PaymentTypeName8",
      "Active": false,
      "Fee": 197.82
    }
  ]
}
```

