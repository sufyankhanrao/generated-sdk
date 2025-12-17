
# Search Settled Transactions Response Settlements

## Structure

`SearchSettledTransactionsResponseSettlements`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `fraud_fields` | [`FraudSightDetail1`](../../doc/models/fraud-sight-detail-1.md) | Optional | Metric indicating transactions potential fraudulent activity level. |

## Example (as JSON)

```json
{
  "fraudFields": {
    "fraudScore": 100.0,
    "fraudRule": "fraudRule2",
    "fraudResponseCode": {
      "code": "code6",
      "shortDescription": "shortDescription4",
      "longDescription": "longDescription8"
    },
    "fraudRuleResult": {
      "code": "code2",
      "shortDescription": "shortDescription0",
      "longDescription": "longDescription4"
    },
    "fraudResponseTime": "fraudResponseTime4"
  }
}
```

