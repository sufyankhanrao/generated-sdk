
# Remove From Waitlist Request

## Structure

`RemoveFromWaitlistRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `waitlist_entry_ids` | `List[int]` | Required | A list of `WaitlistEntryIds` to remove from the waiting list. |

## Example (as JSON)

```json
{
  "WaitlistEntryIds": [
    237,
    238
  ]
}
```

