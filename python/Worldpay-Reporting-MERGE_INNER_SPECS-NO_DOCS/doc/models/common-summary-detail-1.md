
# Common Summary Detail 1

Common summary details.

## Structure

`CommonSummaryDetail1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `settled_gross_amount` | `float` | Optional | Gross amount settled as per the selection criteria.<br><br>**Constraints**: `>= 0`, `<= 9999999999999.99` |
| `settled_gross_count` | `int` | Optional | Number of transactions settled as Gross amount as per the selection criteria.<br><br>**Constraints**: `>= 0`, `<= 9999999999999` |
| `settled_net_amount` | `float` | Optional | Amount settled after deduction of fees as per the selection criteria.<br><br>**Constraints**: `>= 0`, `<= 9999999999999.99` |
| `settled_net_count` | `int` | Optional | Number of transactions with settled as Net Amount as per the selection criteria.<br><br>**Constraints**: `>= 0`, `<= 9999999999999` |

## Example (as JSON)

```json
{
  "settledGrossAmount": 646.5,
  "settledGrossCount": 11700,
  "settledNetAmount": 5496.876,
  "settledNetCount": 13500
}
```

