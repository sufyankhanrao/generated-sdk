
# Partners Summary Response

Retrieve summaries for partners

## Structure

`PartnersSummaryResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `summaries` | [`List[PartnerSummaryDetails]`](../../doc/models/partner-summary-details.md) | Optional | Summary details |
| `total_gross_revenue` | `float` | Optional | Refers to sum of gross revenue. Gross Revenue is the total amount of sales recognized for a reporting period, prior to any deductions.<br><br>**Constraints**: `>= 0`, `<= 9999999999999.99` |
| `total_process_revenue` | `float` | Optional | Refers to Sum of Process Revenue. Process Revenue is the revenue earned from processing the transactions.<br><br>**Constraints**: `>= 0`, `<= 9999999999999.99` |
| `total_settled_amount` | `float` | Optional | Sum of settled amount per the  selection criteria.<br><br>**Constraints**: `>= 0`, `<= 9999999999999.99` |
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
      "processMonth": "processMonth8",
      "grossRevenue": 21.7,
      "processRevenue": 112.76,
      "settledAmount": 49.76,
      "settledCount": 9999998999
    },
    {
      "processMonth": "processMonth8",
      "grossRevenue": 21.7,
      "processRevenue": 112.76,
      "settledAmount": 49.76,
      "settledCount": 9999998999
    }
  ]
}
```

