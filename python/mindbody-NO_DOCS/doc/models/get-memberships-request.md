
# Get Memberships Request

## Structure

`GetMembershipsRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `membership_ids` | `List[int]` | Optional | The requested membership IDs.<br /><br>Default: **all** IDs that the authenticated user’s access level allows. |

## Example (as JSON)

```json
{
  "MembershipIds": [
    221
  ]
}
```

