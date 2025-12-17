
# Offer of Health Insurance Coverage

Health insurance coverage offer for part II of IRS Form 1095-C

*This model accepts additional fields of type Any.*

## Structure

`OfferOfHealthInsuranceCoverage`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `coverage_code` | `str` | Optional | Offer of Coverage (enter required code) |
| `required_contribution` | `float` | Optional | Employee required contribution |
| `section_4980_h_code` | `str` | Optional | Section 4980H Safe Harbor and Other Relief (enter code) |
| `postal_code` | `str` | Optional | Box 17, ZIP Code<br><br>**Constraints**: *Maximum Length*: `10` |
| `month` | [`CoverageMonth`](../../doc/models/coverage-month.md) | Optional | Month |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example (as JSON)

```json
{
  "coverageCode": "coverageCode8",
  "requiredContribution": 234.32,
  "section4980HCode": "section4980HCode4",
  "postalCode": "postalCode2",
  "month": "NOVEMBER",
  "exampleAdditionalProperty": {
    "key1": "val1",
    "key2": "val2"
  }
}
```

