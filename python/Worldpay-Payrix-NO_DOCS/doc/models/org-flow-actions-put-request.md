
# Org Flow Actions Put Request

## Structure

`OrgFlowActionsPutRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `org_flow` | `str` | Required | The identifier of the orgFlow resource that this orgFlowActions resource is associated with. |
| `org` | `str` | Required | The identifier of the Org resource that this orgFlowActions resource is associated with. |
| `action` | [`OrgFlowActionEnum`](../../doc/models/org-flow-action-enum.md) | Required | The action to take in relation to the Entity being processed.<br><br><details><br><summary>Valid Values</summary><br>- `add` - **Add the referenced Entity to the referenced Org.**<br>- `remove` - **Remove the referenced Entity from the referenced Org.**<br></details><br> |

## Example (as JSON)

```json
{
  "orgFlow": "t1_ofw_67ed51ece84aae1a7d0783z",
  "org": "t1_org_67c89c538efe67fbf018d00",
  "action": "add"
}
```

