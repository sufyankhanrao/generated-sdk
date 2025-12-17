
# Summary Inner

Summary.

## Structure

`SummaryInner`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `vertical` | [`Vertical3Enum`](../../doc/models/vertical-3-enum.md) | Optional | Indicates a specific industry or market carried out by the Organization<br><br>**Constraints**: *Maximum Length*: `15` |
| `process_month` | `str` | Optional | Month for which the transactions are processed.<br><br>**Constraints**: *Minimum Length*: `7`, *Maximum Length*: `7`, *Pattern*: `^[0-9]{4}-[0-9]{2}$` |
| `number_of_chains` | `int` | Optional | Number of chains associated with top hierarchy level.<br><br>**Constraints**: `>= 0`, `<= 9999999999` |
| `number_of_merchants` | `int` | Optional | Number of merchants associated with top hierarchy level.<br><br>**Constraints**: `>= 0`, `<= 9999999999` |
| `gross_revenue` | `float` | Optional | Total Sum of Transaction Amount split by Vertical and Month.<br><br>**Constraints**: `>= 0`, `<= 9999999999999.99` |
| `process_revenue` | `float` | Optional | Total Sum of Revenue earned from processing the transactions split by Vertical and Month.<br><br>**Constraints**: `>= 0`, `<= 9999999999999.99` |
| `settled_transaction_amount` | `float` | Optional | Total Sum of Settlement Amount split by Vertical and Month.<br><br>**Constraints**: `>= 0`, `<= 9999999999999.99` |
| `settled_transaction_count` | `float` | Optional | Number of Settled Transactions split by vertical and Month.<br><br>**Constraints**: `>= 0`, `<= 9999999999999.99` |
| `settled_average_ticket` | `float` | Optional | Average Settled Amount by Transaction split by Vertical and Month<br><br>**Constraints**: `>= 0`, `<= 9999999999999.99` |
| `total_effective_rate` | `float` | Optional | The effective rate is that rate of interest actually earned on over the months.<br><br>**Constraints**: `>= 0`, `<= 9999999999999.99` |

## Example (as JSON)

```json
{
  "vertical": "B2B",
  "processMonth": "2022-01",
  "numberOfChains": 6500,
  "numberOfMerchants": 5500,
  "grossRevenue": 500.87,
  "processRevenue": 200.09,
  "settledTransactionAmount": 6579.98,
  "settledTransactionCount": 500,
  "settledAverageTicket": 23.87,
  "totalEffectiveRate": 4.67
}
```

