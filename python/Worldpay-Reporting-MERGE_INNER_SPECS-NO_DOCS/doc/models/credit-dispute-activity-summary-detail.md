
# Credit Dispute Activity Summary Detail

This object is used to retrieve dispute activity summary

## Structure

`CreditDisputeActivitySummaryDetail`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `retrievals_count` | `int` | Optional | Retrievals count refers to the number of returns during a specific reporting period.<br><br>**Constraints**: `>= 0`, `<= 9999999999` |
| `retrievals_amount` | `float` | Optional | Retrievals amount refers to the number of returns during a specific reporting period.<br><br>**Constraints**: `>= 0`, `<= 9999999999999.99` |
| `chargebacks_count` | `int` | Optional | Chargebacks count refers to the number of returns during a specific reporting period.<br><br>**Constraints**: `>= 0`, `<= 9999999999` |
| `chargebacks_amount` | `float` | Optional | Chargebacks amount refers to the number of returns during a specific reporting period.<br><br>**Constraints**: `>= 0`, `<= 9999999999999.99` |

## Example (as JSON)

```json
{
  "retrievalsCount": 7453,
  "retrievalsAmount": 7543725.34,
  "chargebacksCount": 38465,
  "chargebacksAmount": 933748.56
}
```

