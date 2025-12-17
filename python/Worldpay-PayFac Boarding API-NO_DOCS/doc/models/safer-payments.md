
# Safer Payments

## Structure

`SaferPayments`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `program` | [`ProgramEnum`](../../doc/models/program-enum.md) | Required | Required. Safer Payments program that the submerchant wants to enroll |
| `non_validation_fee_enabled` | `bool` | Optional | Indicates if merchant will be charged for non-validation fee |

## Example (as JSON)

```json
{
  "program": "Basic",
  "nonValidationFeeEnabled": true
}
```

