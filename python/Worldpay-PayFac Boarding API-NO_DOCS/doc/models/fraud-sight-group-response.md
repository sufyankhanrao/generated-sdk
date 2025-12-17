
# Fraud Sight Group Response

## Structure

`FraudSightGroupResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `correlation_id` | `str` | Optional | guid sent in the httpheader v-correlation-id |
| `http_status_code` | `str` | Optional | - |
| `http_status_message` | `str` | Optional | - |
| `rule_groups` | [`List[RuleGroups]`](../../doc/models/rule-groups.md) | Optional | - |

## Example (as JSON)

```json
{
  "correlationId": "0acfc8fe1816421ab7376337d5729b94",
  "httpStatusCode": "200",
  "httpStatusMessage": "Success",
  "ruleGroups": [
    {
      "groupName": "groupName8",
      "description": "description8"
    },
    {
      "groupName": "groupName8",
      "description": "description8"
    },
    {
      "groupName": "groupName8",
      "description": "description8"
    }
  ]
}
```

