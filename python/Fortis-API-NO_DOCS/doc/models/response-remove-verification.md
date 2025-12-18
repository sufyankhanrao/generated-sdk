
# Response Remove Verification

## Structure

`ResponseRemoveVerification`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `mtype` | [`Type115Enum`](../../doc/models/type-115-enum.md) | Optional | Resource Type<br><br>**Default**: `'RemoveVerification'` |
| `data` | [`Data27`](../../doc/models/data-27.md) | Optional | - |

## Example (as JSON)

```json
{
  "type": "RemoveVerification",
  "data": {
    "id": "id0",
    "user_id": "user_id8",
    "hash": "hash6",
    "created_ts": 114
  }
}
```

