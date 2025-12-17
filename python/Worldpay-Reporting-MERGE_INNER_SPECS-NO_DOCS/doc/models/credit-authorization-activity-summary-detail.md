
# Credit Authorization Activity Summary Detail

This object is used to retrieve authorization activity summary

## Structure

`CreditAuthorizationActivitySummaryDetail`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `authorization_count` | `int` | Optional | Count of authorization.<br><br>**Constraints**: `>= 0`, `<= 9999999999` |
| `authorization_amount` | `float` | Optional | Amount of authorization.<br><br>**Constraints**: `>= 0`, `<= 9999999999999.99` |
| `approved_count` | `int` | Optional | Count of approved transactions.<br><br>**Constraints**: `>= 0`, `<= 9999999999` |
| `approved_amount` | `float` | Optional | Amount of approved transactions.<br><br>**Constraints**: `>= 0`, `<= 9999999999999.99` |
| `declined_count` | `int` | Optional | Count of declined transactions.<br><br>**Constraints**: `>= 0`, `<= 9999999999` |
| `declined_amount` | `float` | Optional | Amount of declined transactions.<br><br>**Constraints**: `>= 0`, `<= 9999999999999.99` |
| `merchant_surcharge_count` | `int` | Optional | Refers to count of an additional charge, fee, or tax that is added to the cost of a good or service beyond the initially quoted price.<br><br>**Constraints**: `>= 0`, `<= 9999999999` |
| `merchant_surcharge_amount` | `float` | Optional | Refers to count of an additional charge, fee, or tax that is added to the cost of a good or service beyond the initially quoted price.<br><br>**Constraints**: `>= 0`, `<= 9999999999999.99` |

## Example (as JSON)

```json
{
  "authorizationCount": 335594,
  "authorizationAmount": 96295675.24,
  "approvedCount": 6357,
  "approvedAmount": 5374.65,
  "declinedCount": 7564,
  "declinedAmount": 4583.56,
  "merchantSurchargeCount": 32,
  "merchantSurchargeAmount": 327.97
}
```

