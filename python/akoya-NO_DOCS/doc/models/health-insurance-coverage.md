
# Health Insurance Coverage

Used on Form 1095-A Part III

*This model accepts additional fields of type Any.*

## Structure

`HealthInsuranceCoverage`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `enrollment_premium` | `float` | Optional | Monthly enrollment premiums |
| `slcsp_premium` | `float` | Optional | Monthly second lowest cost silver plan (SLCSP) premium |
| `advance_premium_tax_credit_payment` | `float` | Optional | Monthly advance payment of premium tax credit |
| `month` | [`CoverageMonth`](../../doc/models/coverage-month.md) | Optional | Month of coverage |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example (as JSON)

```json
{
  "enrollmentPremium": 139.74,
  "slcspPremium": 163.34,
  "advancePremiumTaxCreditPayment": 197.06,
  "month": "MAY",
  "exampleAdditionalProperty": {
    "key1": "val1",
    "key2": "val2"
  }
}
```

