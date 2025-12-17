
# Option Security Entity

Information about the option security specific to the type of security

*This model accepts additional fields of type Any.*

## Structure

`OptionSecurityEntity`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `secured` | [`Secured`](../../doc/models/secured.md) | Optional | How the option is secured |
| `option_type` | [`OptionType`](../../doc/models/option-type.md) | Optional | - |
| `strike_price` | `float` | Optional | Strike price / Unit price |
| `expire_date` | `datetime` | Optional | Expiration date of option |
| `shares_per_contract` | `float` | Optional | Shares per contract |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example (as JSON)

```json
{
  "secured": "COVERED",
  "optionType": "CALL",
  "strikePrice": 0.6,
  "expireDate": "2016-03-13T12:52:32.123Z",
  "sharesPerContract": 217.4,
  "exampleAdditionalProperty": {
    "key1": "val1",
    "key2": "val2"
  }
}
```

