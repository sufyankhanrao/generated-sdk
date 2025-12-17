
# Card Network Response

Retrieve card network details

## Structure

`CardNetworkResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `summaries` | [`List[Summary7]`](../../doc/models/summary-7.md) | Optional | Summary details |
| `total_gross_revenue` | `float` | Optional | Refers sum of gross revenue. Gross Revenue is the total amount of sales recognized for a reporting period, prior to any deductions.<br><br>**Constraints**: `>= 0`, `<= 9999999999999.99` |
| `total_process_revenue` | `float` | Optional | Sum of Revenue earned in processing the transactions.<br><br>**Constraints**: `>= 0`, `<= 9999999999999.99` |
| `total_settled_amount` | `float` | Optional | Represents the sum of settled amount per the selection criteria.<br><br>**Constraints**: `>= 0`, `<= 9999999999999.99` |
| `total_settled_count` | `int` | Optional | Total number of settled transactions as per the  selection criteria<br><br>**Constraints**: `<= 9999999999` |

## Example (as JSON)

```json
{
  "totalGrossRevenue": 260.88,
  "totalProcessRevenue": 11.69,
  "totalSettledAmount": 541.05,
  "totalSettledCount": 1243,
  "summaries": [
    {
      "cardNetwork": "cardNetwork6",
      "grossRevenue": 21.7,
      "processRevenue": 112.76,
      "settledAmount": 49.76,
      "settledCount": 9999998999
    }
  ]
}
```

