
# Debit Settlement Activity Summary Detail

This object is used to retrieve settlement activity summary

## Structure

`DebitSettlementActivitySummaryDetail`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `settled_count` | `int` | Optional | Settled count refers to the number of items is settled during a specific reporting period.<br><br>**Constraints**: `>= 0`, `<= 9999999999` |
| `settled_amount` | `float` | Optional | Settled amount refers to the number of items is settled during a specific reporting period.<br><br>**Constraints**: `>= 0`, `<= 9999999999999.99` |

## Example (as JSON)

```json
{
  "settledCount": 84532,
  "settledAmount": 93657.54
}
```

