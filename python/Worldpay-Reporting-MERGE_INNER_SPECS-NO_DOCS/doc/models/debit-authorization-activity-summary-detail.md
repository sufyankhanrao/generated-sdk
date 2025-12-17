
# Debit Authorization Activity Summary Detail

This object is used to retrieve authorization activity summary

## Structure

`DebitAuthorizationActivitySummaryDetail`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `approved_count` | `int` | Optional | Count of approved transactions.<br><br>**Constraints**: `>= 0`, `<= 9999999999` |
| `approved_amount` | `float` | Optional | Amount of approved transactions.<br><br>**Constraints**: `>= 0`, `<= 9999999999999.99` |
| `declined_count` | `int` | Optional | Count of declined transactions.<br><br>**Constraints**: `>= 0`, `<= 9999999999` |
| `declined_amount` | `float` | Optional | Amount of declined transactions.<br><br>**Constraints**: `>= 0`, `<= 9999999999999.99` |

## Example (as JSON)

```json
{
  "approvedCount": 6357,
  "approvedAmount": 5374.65,
  "declinedCount": 7564,
  "declinedAmount": 4583.56
}
```

