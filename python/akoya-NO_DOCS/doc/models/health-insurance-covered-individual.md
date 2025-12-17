
# Health Insurance Covered Individual

Used on Form 1095-B Part IV and Form 1095-C Part III

*This model accepts additional fields of type Any.*

## Structure

`HealthInsuranceCoveredIndividual`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `name` | [`IndividualName`](../../doc/models/individual-name.md) | Optional | Name of responsible individual |
| `tin` | `str` | Optional | Social security number or other TIN |
| `date_of_birth` | `date` | Optional | Date of birth |
| `covered_all_12_months` | `bool` | Optional | Covered all 12 months |
| `covered_months` | [`List[MonthAbbreviation]`](../../doc/models/month-abbreviation.md) | Optional | Months covered |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example (as JSON)

```json
{
  "dateOfBirth": "2021-07-15",
  "name": {
    "first": "first6",
    "middle": "middle6",
    "last": "last0",
    "suffix": "suffix0",
    "exampleAdditionalProperty": {
      "key1": "val1",
      "key2": "val2"
    }
  },
  "tin": "tin4",
  "coveredAll12Months": false,
  "coveredMonths": [
    "FEB",
    "MAR"
  ],
  "exampleAdditionalProperty": {
    "key1": "val1",
    "key2": "val2"
  }
}
```

