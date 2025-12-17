
# Fraud Sight Response

## Structure

`FraudSightResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `correlation_id` | `str` | Optional | guid sent in the httpheader v-correlation-id |
| `http_status_code` | `str` | Optional | - |
| `http_status_message` | `str` | Optional | - |
| `transaction_rules` | [`List[TransactionRules]`](../../doc/models/transaction-rules.md) | Optional | - |

## Example (as JSON)

```json
{
  "correlationId": "0acfc8fe1816421ab7376337d5729b94",
  "httpStatusCode": "200",
  "httpStatusMessage": "Success",
  "transactionRules": [
    {
      "ruleLevel": "ruleLevel4",
      "groupName": "groupName8",
      "description": "description8",
      "mccCode": 64,
      "fraudScoring": "fraudScoring0"
    },
    {
      "ruleLevel": "ruleLevel4",
      "groupName": "groupName8",
      "description": "description8",
      "mccCode": 64,
      "fraudScoring": "fraudScoring0"
    }
  ]
}
```

