
# Sweep Security Entity

Information about the sweep security specific to the type of security

*This model accepts additional fields of type Any.*

## Structure

`SweepSecurityEntity`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `current_balance` | `float` | Optional | Balance of funds in account |
| `available_balance` | `float` | Optional | Balance of funds available for use |
| `balance_as_of` | `datetime` | Optional | As-of date of balances |
| `checks` | `bool` | Optional | Whether or not checks can be written on the account |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example (as JSON)

```json
{
  "currentBalance": 188.98,
  "availableBalance": 101.4,
  "balanceAsOf": "2016-03-13T12:52:32.123Z",
  "checks": false,
  "exampleAdditionalProperty": {
    "key1": "val1",
    "key2": "val2"
  }
}
```

