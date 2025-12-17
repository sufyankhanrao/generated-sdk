
# Contribution Entity

Describes how new contributions are distributed among the available securities.

*This model accepts additional fields of type Any.*

## Structure

`ContributionEntity`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `security_id` | `str` | Optional | Unique identifier of security |
| `security_id_type` | [`SecurityIdType`](../../doc/models/security-id-type.md) | Optional | Security identifier type |
| `employer_match_percentage` | `float` | Optional | Employer contribution match percentage |
| `employer_match_amount` | `float` | Optional | Employer contribution match amount |
| `employee_pre_tax_amount` | `float` | Optional | Employee pre‐tax contribution amount |
| `employee_pre_tax_percentage` | `float` | Optional | Employee pre‐tax contribution percentage |
| `employee_after_tax_amount` | `float` | Optional | Employee after tax contribution amount |
| `employee_after_tax_percentage` | `float` | Optional | Employee after tax contribution percentage |
| `employee_defer_pre_tax_amount` | `float` | Optional | Employee defer pre‐tax contribution match amount |
| `employee_defer_pre_tax_percentage` | `float` | Optional | Employee defer pre‐tax contribution match percentage |
| `employee_year_to_date` | `float` | Optional | Employee total year to date contribution |
| `employer_year_to_date` | `float` | Optional | Employer total year to date contribution |
| `rollover_contribution_percentage` | `float` | Optional | Rollover contribution percentage |
| `rollover_contribution_amount` | `float` | Optional | Rollover contribution Amount |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example (as JSON)

```json
{
  "securityId": "securityId2",
  "securityIdType": "VALOR",
  "employerMatchPercentage": 195.92,
  "employerMatchAmount": 120.16,
  "employeePreTaxAmount": 147.12,
  "exampleAdditionalProperty": {
    "key1": "val1",
    "key2": "val2"
  }
}
```

