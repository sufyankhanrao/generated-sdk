
# Txn Sessions Configurations

Configurable data to be used to enhance security.

## Structure

`TxnSessionsConfigurations`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `duration` | `int` | Optional | duration refers to How many minutes this key should live (automated voided when tried to use after expired). |
| `max_times_approved` | `int` | Optional | maxTimesApproved refers to how many approved transactions related it can be used. |
| `max_times_use` | `int` | Optional | maxTimesUse refers to how many times we can make request with this key. |

## Example (as JSON)

```json
{
  "duration": 112,
  "maxTimesApproved": 32,
  "maxTimesUse": 34
}
```

