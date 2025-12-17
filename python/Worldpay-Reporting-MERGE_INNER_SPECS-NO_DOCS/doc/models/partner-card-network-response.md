
# Partner Card Network Response

Card network response for partners.

## Structure

`PartnerCardNetworkResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
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
  "totalSettledCount": 1243
}
```

