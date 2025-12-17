
# Gift Authorization Activity Summary Detail

This object is used to retrieve authorization activity summary

## Structure

`GiftAuthorizationActivitySummaryDetail`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `authorization_count` | `int` | Optional | Refers to count of authorization.<br><br>**Constraints**: `>= 0`, `<= 9999999999` |
| `authorization_amount` | `float` | Optional | Refers to amount of authorization.<br><br>**Constraints**: `>= 0`, `<= 99999` |
| `approved_count` | `int` | Optional | Refers to count of approved transactions.<br><br>**Constraints**: `>= 0`, `<= 9999999999` |
| `approved_amount` | `float` | Optional | Refers to amount of approved transactions.<br><br>**Constraints**: `>= 0`, `<= 9999999999999.99` |
| `declined_count` | `int` | Optional | Refers to count of declined transactions.<br><br>**Constraints**: `>= 0`, `<= 9999999999` |
| `declined_amount` | `float` | Optional | Refers to amount of declined transactions.<br><br>**Constraints**: `>= 0`, `<= 9999999999999.99` |
| `reload_count` | `int` | Optional | Refers to count of an additional charge, fee, or tax that is added to the cost of a good or service beyond the initially quoted price.<br><br>**Constraints**: `>= 0`, `<= 9999999999` |
| `reload_amount` | `float` | Optional | Refers to amount of an additional charge, fee, or tax that is added to the cost of a good or service beyond the initially quoted price.<br><br>**Constraints**: `>= 0`, `<= 9999999999999.99` |
| `redemption_count` | `int` | Optional | Refers to count of gift redemption.<br><br>**Constraints**: `>= 0`, `<= 9999999999` |
| `redemption_amount` | `float` | Optional | Refers to amount of gift redemption.<br><br>**Constraints**: `>= 0`, `<= 9999999999999.99` |
| `pre_authorization_request_count` | `int` | Optional | Refers to count of pre authorization request.<br><br>**Constraints**: `>= 0`, `<= 9999999999` |
| `pre_authorization_request_amount` | `float` | Optional | Refers to amount of pre authorization request<br><br>**Constraints**: `>= 0`, `<= 9999999999999.99` |
| `pre_authorization_request_reversal_count` | `int` | Optional | Refers to count of pre authorization reversal request.<br><br>**Constraints**: `>= 0`, `<= 9999999999` |
| `pre_authorization_request_reversal_amount` | `float` | Optional | Refers to amount of pre authorization reversal request.<br><br>**Constraints**: `>= 0`, `<= 9999999999999.99` |
| `merchant_surcharge_count` | `int` | Optional | Surcharge refers to count of an additional charge, fee, or tax that is added to the cost of a good or service beyond the initially quoted price.<br><br>**Constraints**: `>= 0`, `<= 9999999999` |
| `merchant_surcharge_amount` | `float` | Optional | Surcharge refers to an additional charge, fee, or tax that is added to the cost of a good or service beyond the initially quoted price.<br><br>**Constraints**: `>= 0`, `<= 9999999999999.99` |

## Example (as JSON)

```json
{
  "authorizationCount": 335594,
  "approvedCount": 6357,
  "approvedAmount": 5374.65,
  "declinedCount": 7564,
  "declinedAmount": 4583.56,
  "reloadCount": 32,
  "reloadAmount": 4583.56,
  "redemptionCount": 32,
  "redemptionAmount": 4583.56,
  "preAuthorizationRequestCount": 32,
  "preAuthorizationRequestAmount": 4583.56,
  "preAuthorizationRequestReversalCount": 32,
  "preAuthorizationRequestReversalAmount": 4583.56,
  "merchantSurchargeCount": 32,
  "merchantSurchargeAmount": 327.97,
  "authorizationAmount": 94.32
}
```

