
# Partner Vertical Details

Partner verticals details.

## Structure

`PartnerVerticalDetails`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `gross_revenue` | `float` | Optional | Gross Revenue is the total amount of sales recognized for a reporting period, prior to any deductions.<br><br>**Constraints**: `>= 0`, `<= 9999999999999.99` |
| `process_revenue` | `float` | Optional | Revenue earned from processing the transactions for a specific vertical for the selected month range.<br><br>**Constraints**: `>= 0`, `<= 9999999999999.99` |
| `settled_amount` | `float` | Optional | Total settled amount for a specific vertical for the selected month range.<br><br>**Constraints**: `>= 0`, `<= 9999999999999.99` |
| `settled_count` | `int` | Optional | Total settled transaction count for a specific vertical for the selected month range.<br><br>**Constraints**: `<= 9999999999` |

## Example (as JSON)

```json
{
  "grossRevenue": 500.87,
  "processRevenue": 200.09,
  "settledAmount": 279.98,
  "settledCount": 500
}
```

