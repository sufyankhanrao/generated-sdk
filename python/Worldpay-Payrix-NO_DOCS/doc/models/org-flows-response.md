
# Org Flows Response

## Structure

`OrgFlowsResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Optional | The ID of this resource. |
| `created` | `str` | Optional | The date and time at which this resource was created. The format should be YYYY-MM-DD HH:MM:SS.SSSS<br><br>**Constraints**: *Pattern*: `^\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}.\d{4}$` |
| `modified` | `str` | Optional | The date and time at which this resource was modified. The format should be YYYY-MM-DD HH:MM:SS.SSSS<br><br>**Constraints**: *Pattern*: `^\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}.\d{4}$` |
| `creator` | str \| [loginsResponse](../../doc/models/logins-response.md) \| None | Optional | This is a container for any-of cases. |
| `modifier` | `str` | Optional | The identifier of the Login that last modified this resource. |
| `login` | `str` | Optional | The Login that owns this resource. |
| `forlogin` | `str` | Optional | The identifier of the Login resource for which this orgFlows resource is triggered. |
| `team` | `str` | Optional | The identifier of the Team resource for which this orgFlows resource is triggered. |
| `division` | `str` | Optional | The identified of the Division resource for which this orgFlows resource is triggered. |
| `trigger` | [`OrgFlowTriggerEnum`](../../doc/models/org-flow-trigger-enum.md) | Optional | This field sets the trigger that determines when this orgFlow runs.<br><br><details><br><summary>Valid Values</summary><br>- `create` - **Entity creation.**<br>- `low` - **Entity verification through decisions hits a configured low score.**<br>- `high` - **Entity verification through decisions hits a configured high score.**<br>- `board` - **Merchant boarding.**<br></details><br> |
| `partition` | `str` | Optional | The identified of the Partition resource for which this orgFlows resource is triggered. |

## Example (as JSON)

```json
{
  "id": "id6",
  "created": "created6",
  "modified": "modified4",
  "creator": "String5",
  "modifier": "modifier0"
}
```

