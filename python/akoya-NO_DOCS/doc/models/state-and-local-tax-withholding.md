
# State and Local Tax Withholding

Income in a state and/or locality and its or their tax withholding

*This model accepts additional fields of type Any.*

## Structure

`StateAndLocalTaxWithholding`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `state_code` | [`StateCode`](../../doc/models/state-code.md) | Optional | State two-digit code |
| `state` | [`StateTaxWithholding`](../../doc/models/state-tax-withholding.md) | Optional | Amount of state income tax withheld |
| `local` | [`LocalTaxWithholding`](../../doc/models/local-tax-withholding.md) | Optional | Amount of local income tax withheld, if any |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example (as JSON)

```json
{
  "stateCode": "IL",
  "state": {
    "taxWithheld": 128.78,
    "taxId": "taxId0",
    "income": 191.56,
    "exampleAdditionalProperty": {
      "key1": "val1",
      "key2": "val2"
    }
  },
  "local": {
    "taxWithheld": 75.84,
    "localityName": "localityName6",
    "income": 244.5,
    "exampleAdditionalProperty": {
      "key1": "val1",
      "key2": "val2"
    }
  },
  "exampleAdditionalProperty": {
    "key1": "val1",
    "key2": "val2"
  }
}
```

