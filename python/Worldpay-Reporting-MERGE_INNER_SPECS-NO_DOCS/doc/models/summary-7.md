
# Summary 7

## Structure

`Summary7`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `card_network` | `str` | Optional | Brand or Network to which the card is associated.<br><br>**Constraints**: *Maximum Length*: `19` |
| `gross_revenue` | `float` | Optional | Gross Revenue is the total amount of sales recognized for a reporting period, prior to any deductions.<br><br>**Constraints**: `>= 0`, `<= 9999999999999.99` |
| `process_revenue` | `float` | Optional | Revenue earned from processing the transactions.<br><br>**Constraints**: `>= 0`, `<= 9999999999999.99` |
| `settled_amount` | `float` | Optional | Total amount settled per the  selection criteria.<br><br>**Constraints**: `>= 0`, `<= 9999999999999.99` |
| `settled_count` | `int` | Optional | Total number of settled transactions as per the  selection criteria<br><br>**Constraints**: `<= 9999999999` |

## Example (as JSON)

```json
{
  "cardNetwork": "VISA",
  "grossRevenue": 500.87,
  "processRevenue": 200.09,
  "settledAmount": 6579.98,
  "settledCount": 500
}
```

