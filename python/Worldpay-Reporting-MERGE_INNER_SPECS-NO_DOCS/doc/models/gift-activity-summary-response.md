
# Gift Activity Summary Response

## Structure

`GiftActivitySummaryResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `authorization_activity` | [`GiftAuthorizationActivitySummaryDetail`](../../doc/models/gift-authorization-activity-summary-detail.md) | Optional | Refers to gift authorization activity |
| `settlement_activity` | [`GiftSettlementActivitySummaryDetail`](../../doc/models/gift-settlement-activity-summary-detail.md) | Optional | Refers to gift settlement activity |
| `other_activity` | [`GiftOtherActivitySummaryDetail`](../../doc/models/gift-other-activity-summary-detail.md) | Optional | Refers to gift other activity |

## Example (as JSON)

```json
{
  "authorizationActivity": {
    "authorizationCount": 158,
    "authorizationAmount": 79.28,
    "approvedCount": 136,
    "approvedAmount": 5.02,
    "declinedCount": 230
  },
  "settlementActivity": {
    "returnsCount": 224,
    "returnsAmount": 127.24,
    "activationCount": 40,
    "activationAmount": 17.5,
    "merchantSurchargeCount": 136
  },
  "otherActivity": {
    "count": 44,
    "amount": 73.94,
    "inActivityCount": 10,
    "inActivityAmount": 73.48,
    "statusCount": 140
  }
}
```

