
# Credit Settlement Activity Summary Detail

This object is used to retrieve settlement activity summary

## Structure

`CreditSettlementActivitySummaryDetail`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `settled_count` | `int` | Optional | Settled count refers to the number of items is settled during a specific reporting period.<br><br>**Constraints**: `>= 0`, `<= 9999999999` |
| `settled_amount` | `float` | Optional | Settled amount refers to the number of items is settled during a specific reporting period.<br><br>**Constraints**: `>= 0`, `<= 9999999999999.99` |
| `sales_count` | `int` | Optional | Sales count refers to the number of sells during a specific reporting period.<br><br>**Constraints**: `>= 0`, `<= 9999999999` |
| `sales_amount` | `float` | Optional | Sales amount refers to the number of sells during a specific reporting period.<br><br>**Constraints**: `>= 0`, `<= 9999999999999.99` |
| `returns_count` | `int` | Optional | Returns count refers to the number of returns during a specific reporting period.<br><br>**Constraints**: `>= 0`, `<= 9999999999` |
| `returns_amount` | `float` | Optional | Returns amount refers to the number of returns during a specific reporting period.<br><br>**Constraints**: `>= 0`, `<= 9999999999999.99` |
| `merchant_surcharge_count` | `int` | Optional | Refers to count of an additional charge, fee, or tax that is added to the cost of a good or service beyond the initially quoted price.<br><br>**Constraints**: `>= 0`, `<= 9999999999` |
| `merchant_surcharge_amount` | `float` | Optional | Refers to count of an additional charge, fee, or tax that is added to the cost of a good or service beyond the initially quoted price.<br><br>**Constraints**: `>= 0`, `<= 9999999999999.99` |

## Example (as JSON)

```json
{
  "settledCount": 84532,
  "settledAmount": 93657.54,
  "salesCount": 84532,
  "salesAmount": 93657.54,
  "returnsCount": 4356,
  "returnsAmount": 43848.87,
  "merchantSurchargeCount": 32,
  "merchantSurchargeAmount": 327.97
}
```

