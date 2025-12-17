
# Verticals Response

Verticals response.

## Structure

`VerticalsResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `summaries` | [`List[Summary11]`](../../doc/models/summary-11.md) | Optional | Summary details |
| `total_gross_revenue` | `float` | Optional | Total overall cost incurred by the merchant across verticals for the selected month range.<br><br>**Constraints**: `>= 0`, `<= 9999999999999.99` |
| `total_process_revenue` | `float` | Optional | Total Revenue earned from processing the transactions across verticals for the selected month range.<br><br>**Constraints**: `>= 0`, `<= 9999999999999.99` |
| `total_settled_amount` | `float` | Optional | Total sum of settled amount across verticals for the selected month range.<br><br>**Constraints**: `>= 0`, `<= 9999999999999.99` |
| `total_settled_count` | `int` | Optional | Total number of settled transactions as per the  selection criteria<br><br>**Constraints**: `<= 9999999999` |

## Example (as JSON)

```json
{
  "totalGrossRevenue": 260.88,
  "totalProcessRevenue": 11.69,
  "totalSettledAmount": 541.05,
  "totalSettledCount": 1354,
  "summaries": [
    {
      "vertical": "vertical6",
      "grossRevenue": 21.7,
      "processRevenue": 112.76,
      "settledAmount": 49.76,
      "settledCount": 9999998999
    }
  ]
}
```

