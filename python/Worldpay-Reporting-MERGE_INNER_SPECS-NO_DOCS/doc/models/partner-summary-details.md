
# Partner Summary Details

Partner summary details.

## Structure

`PartnerSummaryDetails`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `process_month` | `str` | Optional | Month for which the transactions are processed.<br><br>**Constraints**: *Minimum Length*: `7`, *Maximum Length*: `7`, *Pattern*: `^[0-9]{4}-[0-9]{2}$` |
| `gross_revenue` | `float` | Optional | Gross Revenue is the total amount of sales recognized for a reporting period, prior to any deductions.<br><br>**Constraints**: `>= 0`, `<= 9999999999999.99` |
| `process_revenue` | `float` | Optional | Revenue earned in processing the transactions.<br><br>**Constraints**: `>= 0`, `<= 9999999999999.99` |
| `settled_amount` | `float` | Optional | Total settled amount per the  selection criteria<br><br>**Constraints**: `>= 0`, `<= 9999999999999.99` |
| `settled_count` | `int` | Optional | Total number of settled transactions as per the  selection criteria<br><br>**Constraints**: `<= 9999999999` |
| `settled_average_ticket` | `float` | Optional | Average amount generated per transaction for a selected ISC and for selected month range.<br><br>**Constraints**: `>= 0`, `<= 9999999999999.99` |
| `total_effective_rate` | `float` | Optional | The effective rate is that rate of interest actually earned on over the months.<br><br>**Constraints**: `>= 0`, `<= 9999999999999.99` |

## Example (as JSON)

```json
{
  "processMonth": "2022-01",
  "grossRevenue": 500.87,
  "processRevenue": 200.09,
  "settledAmount": 6579.98,
  "settledCount": 500,
  "settledAverageTicket": 23.87,
  "totalEffectiveRate": 4.67
}
```

