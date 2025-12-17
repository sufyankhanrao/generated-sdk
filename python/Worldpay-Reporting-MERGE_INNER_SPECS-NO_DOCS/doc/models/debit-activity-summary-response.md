
# Debit Activity Summary Response

## Structure

`DebitActivitySummaryResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `authorization_activity` | [`DebitAuthorizationActivitySummaryDetail`](../../doc/models/debit-authorization-activity-summary-detail.md) | Optional | Refers to debit authorization activity |
| `settlement_activity` | [`DebitSettlementActivitySummaryDetail`](../../doc/models/debit-settlement-activity-summary-detail.md) | Optional | Refers to debit settlement activity |
| `other_activity` | [`DebitOtherActivitySummaryDetail`](../../doc/models/debit-other-activity-summary-detail.md) | Optional | Refers to debit other activity |

## Example (as JSON)

```json
{
  "authorizationActivity": {
    "approvedCount": 136,
    "approvedAmount": 5.02,
    "declinedCount": 230,
    "declinedAmount": 90.86
  },
  "settlementActivity": {
    "settledCount": 246,
    "settledAmount": 121.8
  },
  "otherActivity": {
    "reversedCount": 164,
    "reversedAmount": 159.92,
    "inquiryCount": 152,
    "inquiryAmount": 137.04
  }
}
```

