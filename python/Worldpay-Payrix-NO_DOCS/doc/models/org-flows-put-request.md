
# Org Flows Put Request

## Structure

`OrgFlowsPutRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `login` | `str` | Required | The Login that owns this resource. |
| `forlogin` | `str` | Optional | The identifier of the Login resource for which this orgFlows resource is triggered. |
| `team` | `str` | Optional | The identifier of the Team resource for which this orgFlows resource is triggered. |
| `division` | `str` | Optional | The identified of the Division resource for which this orgFlows resource is triggered. |
| `trigger` | [`OrgFlowTriggerEnum`](../../doc/models/org-flow-trigger-enum.md) | Required | This field sets the trigger that determines when this orgFlow runs.<br><br><details><br><summary>Valid Values</summary><br>- `create` - **Entity creation.**<br>- `low` - **Entity verification through decisions hits a configured low score.**<br>- `high` - **Entity verification through decisions hits a configured high score.**<br>- `board` - **Merchant boarding.**<br></details><br> |
| `partition` | `str` | Optional | The identified of the Partition resource for which this orgFlows resource is triggered. |

## Example (as JSON)

```json
{
  "login": "g1577139c2304b7",
  "forlogin": "t1_log_67c203583fbd0a4437d1332",
  "team": "t1_tem_67c202b908935b505104500",
  "division": "t1_div_67c56806728fbbf0bae0b10",
  "trigger": "create",
  "partition": "t1_ptn_666834d4d504f21414978f5"
}
```

