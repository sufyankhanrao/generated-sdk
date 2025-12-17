
# State Tax Withholding

Amount of state income tax withheld

*This model accepts additional fields of type Any.*

## Structure

`StateTaxWithholding`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `tax_withheld` | `float` | Optional | Amount of state income tax withheld |
| `tax_id` | `str` | Optional | Filer's state tax id |
| `income` | `float` | Optional | Income amount for state tax purposes |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example (as JSON)

```json
{
  "taxWithheld": 48.38,
  "taxId": "taxId0",
  "income": 15.96,
  "exampleAdditionalProperty": {
    "key1": "val1",
    "key2": "val2"
  }
}
```

