
# Credit Activity Summary Response

## Structure

`CreditActivitySummaryResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `authorization_activity` | [`CreditAuthorizationActivitySummaryDetail`](../../doc/models/credit-authorization-activity-summary-detail.md) | Optional | Refers to credit authorization activity |
| `settlement_activity` | [`CreditSettlementActivitySummaryDetail`](../../doc/models/credit-settlement-activity-summary-detail.md) | Optional | Refers to credit settlement activity |
| `dispute_activity` | [`CreditDisputeActivitySummaryDetail`](../../doc/models/credit-dispute-activity-summary-detail.md) | Optional | Refers to credit dispute activity |

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
    "settledCount": 246,
    "settledAmount": 121.8,
    "salesCount": 252,
    "salesAmount": 131.16,
    "returnsCount": 224
  },
  "disputeActivity": {
    "retrievalsCount": 32,
    "retrievalsAmount": 6.74,
    "chargebacksCount": 66,
    "chargebacksAmount": 5.46
  }
}
```

