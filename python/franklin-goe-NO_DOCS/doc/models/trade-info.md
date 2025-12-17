
# Trade Info

*This model accepts additional fields of type Any.*

## Structure

`TradeInfo`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `direction` | `str` | Required | “S” indicates sale of the asset while “B” indicated purchase |
| `symbol` | `str` | Required | Identifier associated with an asset class |
| `cusip` | `str` | Required | Cusip associated with an asset class |
| `quantity` | `float` | Required | Refers to the amount of sell associated with a trade |
| `amount` | `float` | Required | Refers to the amount of buy associated with a trade |
| `phase` | `str` | Required | “Rebalance” refers to trades required to move from one portfolio to another.  <br>            “Withdrawal” refers to trades needed to withdraw a goal amount |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example (as JSON)

```json
{
  "direction": "S",
  "symbol": "CASH",
  "cusip": "cusip2",
  "quantity": 29178.0,
  "amount": 10748.399065,
  "phase": "phase6",
  "exampleAdditionalProperty": {
    "key1": "val1",
    "key2": "val2"
  }
}
```

