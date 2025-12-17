
# Payment Details

Payment details for some transactions

*This model accepts additional fields of type Any.*

## Structure

`PaymentDetails`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `escrow_amount` | `float` | Optional | The amount of payment applied to escrow |
| `fees_amount` | `float` | Optional | The amount of payment applied to fees |
| `insurance_amount` | `float` | Optional | The amount of payment applied to life/health/accident insurance on the loan |
| `interest_amount` | `float` | Optional | The amount of payment applied to interest |
| `pmi_amount` | `float` | Optional | The amount of payment applied to PMI |
| `principal_amount` | `float` | Optional | The amount of payment applied to principal |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example (as JSON)

```json
{
  "escrowAmount": 171.3,
  "feesAmount": 83.52,
  "insuranceAmount": 63.4,
  "interestAmount": 64.72,
  "pmiAmount": 217.98,
  "exampleAdditionalProperty": {
    "key1": "val1",
    "key2": "val2"
  }
}
```

