
# Net Settled Amount Card Type Response

Results for net settlement amount by card type.

## Structure

`NetSettledAmountCardTypeResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `summaries` | [`List[Summary21]`](../../doc/models/summary-21.md) | Optional | Summary details |
| `total_settled_gross_amount` | `float` | Optional | Sum of Settled Gross Amount.<br><br>**Constraints**: `>= 0`, `<= 9999999999999.99` |
| `total_settled_gross_count` | `int` | Optional | Total number of transactions with gross settled amount.<br><br>**Constraints**: `>= 0`, `<= 9999999999999` |
| `total_settled_net_amount` | `float` | Optional | Sum of Settled Net Amount.<br><br>**Constraints**: `>= 0`, `<= 9999999999999.99` |
| `total_settled_net_count` | `int` | Optional | Total number of transactions with net settled amount.<br><br>**Constraints**: `>= 0`, `<= 9999999999999` |

## Example (as JSON)

```json
{
  "totalSettledGrossAmount": 120.01,
  "totalSettledGrossCount": 10,
  "totalSettledNetAmount": 20.02,
  "totalSettledNetCount": 156475,
  "summaries": [
    {
      "settledGrossAmount": 140.36,
      "settledGrossCount": 4,
      "settledNetAmount": 78.04,
      "settledNetCount": 238,
      "processMonth": "processMonth8"
    }
  ]
}
```

