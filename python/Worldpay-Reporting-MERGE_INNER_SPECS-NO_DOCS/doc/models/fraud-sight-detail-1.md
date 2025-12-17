
# Fraud Sight Detail 1

This object holds the fraud score and rule result information

## Structure

`FraudSightDetail1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `fraud_score` | `float` | Optional | Fraud score is a measure that helps gauge risk involved with orders before processing.<br><br>**Constraints**: `>= 0.01`, `<= 100` |
| `fraud_rule` | `str` | Optional | Fraud rule is a condition that helps you decide whether an activity is fraudulent or not.<br><br>**Constraints**: *Maximum Length*: `256` |
| `fraud_response_code` | [`CodeAndDescription4`](../../doc/models/code-and-description-4.md) | Optional | Predefined set of codes that determines various types of fraudulent activities to classify accordingly. |
| `fraud_rule_result` | [`CodeAndDescription4`](../../doc/models/code-and-description-4.md) | Optional | The result of the decision made from the Fraud rule applied for the transaction. |
| `fraud_response_time` | `str` | Optional | Time taken to verify if the transaction was fraudulent.<br><br>**Constraints**: *Maximum Length*: `256` |

## Example (as JSON)

```json
{
  "fraudScore": 100.0,
  "fraudRule": "Fraudlent",
  "fraudResponseTime": "3",
  "fraudResponseCode": {
    "code": "code6",
    "shortDescription": "shortDescription4",
    "longDescription": "longDescription8"
  },
  "fraudRuleResult": {
    "code": "code2",
    "shortDescription": "shortDescription0",
    "longDescription": "longDescription4"
  }
}
```

