
# Business Security Products Safer Payments

This aggregate field includes details of Saferpayment Security product

## Structure

`BusinessSecurityProductsSaferPayments`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `enabled` | `bool` | Optional | Indicator for Safer Payments Enablement |
| `program` | [`ProgramEnum`](../../doc/models/program-enum.md) | Optional | Name of the Program<br><br>**Constraints**: *Maximum Length*: `35` |
| `program_code` | [`ProgramCodeEnum`](../../doc/models/program-code-enum.md) | Optional | Identifier code of the program<br><br>**Constraints**: *Maximum Length*: `1` |

## Example (as JSON)

```json
{
  "enabled": true,
  "program": "SaferPayments Basic",
  "programCode": "Y"
}
```

