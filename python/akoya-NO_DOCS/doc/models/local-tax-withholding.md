
# Local Tax Withholding

Amount of local income tax withheld, if any

*This model accepts additional fields of type Any.*

## Structure

`LocalTaxWithholding`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `tax_withheld` | `float` | Optional | Amount of local income tax withheld |
| `locality_name` | `str` | Optional | Locality name |
| `income` | `float` | Optional | Income amount for local tax purposes |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example (as JSON)

```json
{
  "taxWithheld": 97.82,
  "localityName": "localityName0",
  "income": 162.16,
  "exampleAdditionalProperty": {
    "key1": "val1",
    "key2": "val2"
  }
}
```

