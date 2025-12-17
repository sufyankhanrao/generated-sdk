
# Fraudfields

Metric indicating transactions potential fraudulent activity level.

## Structure

`Fraudfields`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `fraud_score` | [`SearchAuthRealTransactionsRequestFraudScore`](../../doc/models/search-auth-real-transactions-request-fraud-score.md) | Optional | Fraud score is a measure that helps gauge risk involved with orders before processing. |
| `fraud_response_code` | [`FraudResponseCodeEnum`](../../doc/models/fraud-response-code-enum.md) | Optional | Predefined set of codes that determines various types of fraudulent activities to classify accordingly.<br><br>**Constraints**: *Maximum Length*: `256` |
| `fraud_rule_result` | [`FraudRuleResultEnum`](../../doc/models/fraud-rule-result-enum.md) | Optional | The result of the decision made from the Fraud rule applied for the transaction.<br><br>**Constraints**: *Maximum Length*: `256` |

## Example (as JSON)

```json
{
  "fraudResponseCode": "FRAUD_SYSTEM_APPROVED",
  "fraudRuleResult": "MANUAL_REVIEW",
  "fraudScore": {
    "fromScore": 100.0,
    "toScore": 100.0
  }
}
```

