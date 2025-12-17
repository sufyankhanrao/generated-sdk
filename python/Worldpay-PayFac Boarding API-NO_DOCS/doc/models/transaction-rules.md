
# Transaction Rules

## Structure

`TransactionRules`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `rule_level` | `str` | Optional | - |
| `group_name` | `str` | Optional | - |
| `description` | `str` | Optional | - |
| `mcc_code` | `int` | Optional | - |
| `fraud_scoring` | `str` | Optional | - |
| `real_time_decision` | `bool` | Optional | - |
| `transaction_type` | `str` | Optional | - |
| `card_presence` | `str` | Optional | - |
| `card_network_type` | `str` | Optional | - |
| `entry_mode` | `str` | Optional | - |
| `e_comm_indicator` | `str` | Optional | - |
| `auto_decline` | `bool` | Optional | - |

## Example (as JSON)

```json
{
  "ruleLevel": "Chain",
  "groupName": "NCNP",
  "description": "This is the Rule Group for NCNP merchants",
  "mccCode": 7372,
  "fraudScoring": "PostNetworkSwitch",
  "realTimeDecision": true,
  "transactionType": "Preauthorization",
  "cardPresence": "CardNotPresent",
  "cardNetworkType": "Credit",
  "entryMode": "Manual",
  "eCommIndicator": "SingleMOTO",
  "autoDecline": true
}
```

