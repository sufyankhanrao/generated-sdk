
# Org Flow Actions Response

## Structure

`OrgFlowActionsResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Optional | The ID of this resource. |
| `created` | `str` | Optional | The date and time at which this resource was created. The format should be YYYY-MM-DD HH:MM:SS.SSSS<br><br>**Constraints**: *Pattern*: `^\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}.\d{4}$` |
| `modified` | `str` | Optional | The date and time at which this resource was modified. The format should be YYYY-MM-DD HH:MM:SS.SSSS<br><br>**Constraints**: *Pattern*: `^\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}.\d{4}$` |
| `creator` | str \| [loginsResponse](../../doc/models/logins-response.md) \| None | Optional | This is a container for any-of cases. |
| `modifier` | `str` | Optional | The identifier of the Login that last modified this resource. |
| `org_flow` | `str` | Optional | The identifier of the orgFlow resource that this orgFlowActions resource is associated with. |
| `org` | `str` | Optional | The identifier of the Org resource that this orgFlowActions resource is associated with. |
| `action` | [`OrgFlowActionEnum`](../../doc/models/org-flow-action-enum.md) | Optional | The action to take in relation to the Entity being processed.<br><br><details><br><summary>Valid Values</summary><br>- `add` - **Add the referenced Entity to the referenced Org.**<br>- `remove` - **Remove the referenced Entity from the referenced Org.**<br></details><br> |

## Example (as JSON)

```json
{
  "id": "id8",
  "created": "created8",
  "modified": "modified6",
  "creator": "String7",
  "modifier": "modifier2"
}
```

