
# Gift Settlement Activity Summary Detail

This object is used to retrieve settlement activity summary

## Structure

`GiftSettlementActivitySummaryDetail`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `returns_count` | `int` | Optional | Returns count refers to the number of returns during a specific reporting period.<br><br>**Constraints**: `>= 0`, `<= 9999999999` |
| `returns_amount` | `float` | Optional | Returns amount refers to the number of returns during a specific reporting period.<br><br>**Constraints**: `>= 0`, `<= 9999999999999.99` |
| `activation_count` | `int` | Optional | Refers to count of activation, charged by the provider.<br><br>**Constraints**: `>= 0`, `<= 9999999999` |
| `activation_amount` | `float` | Optional | Refers to amount of activation, charged by the provider.<br><br>**Constraints**: `>= 0`, `<= 9999999999999.99` |
| `merchant_surcharge_count` | `int` | Optional | Surcharge refers to count of an additional charge, fee, or tax that is added to the cost of a good or service beyond the initially quoted price.<br><br>**Constraints**: `>= 0`, `<= 9999999999` |
| `merchant_surcharge_amount` | `float` | Optional | Surcharge refers to an additional charge, fee, or tax that is added to the cost of a good or service beyond the initially quoted price.<br><br>**Constraints**: `>= 0`, `<= 9999999999999.99` |

## Example (as JSON)

```json
{
  "returnsCount": 4356,
  "returnsAmount": 43848.87,
  "activationCount": 32,
  "activationAmount": 327.97,
  "merchantSurchargeCount": 54,
  "merchantSurchargeAmount": 435.65
}
```

