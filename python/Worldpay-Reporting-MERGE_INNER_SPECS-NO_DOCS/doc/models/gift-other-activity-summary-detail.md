
# Gift Other Activity Summary Detail

This object is used to retrieve Gift settlement activity summary

## Structure

`GiftOtherActivitySummaryDetail`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `count` | `int` | Optional | Refers to the count of all transaction type.<br><br>**Constraints**: `>= 0`, `<= 9999999999` |
| `amount` | `float` | Optional | Refers to the amount of all transaction type.<br><br>**Constraints**: `>= 0`, `<= 9999999999999.99` |
| `in_activity_count` | `int` | Optional | Refers to the count of transactions type as G1 for the account during a specific reporting period.<br><br>**Constraints**: `>= 0`, `<= 9999999999` |
| `in_activity_amount` | `float` | Optional | Refers to the amount of transactions type as G1 for the account during a specific reporting period.<br><br>**Constraints**: `>= 0`, `<= 9999999999999.99` |
| `status_count` | `int` | Optional | Refers to the count of transactions type as GS for the account during a specific reporting period.<br><br>**Constraints**: `>= 0`, `<= 9999999999` |
| `status_amount` | `float` | Optional | Refers to the amount of transactions type as GS for the account during a specific reporting period.<br><br>**Constraints**: `>= 0`, `<= 9999999999999.99` |

## Example (as JSON)

```json
{
  "count": 453,
  "amount": 756.98,
  "inActivityCount": 78,
  "inActivityAmount": 675.34,
  "statusCount": 45,
  "statusAmount": 876.87
}
```

