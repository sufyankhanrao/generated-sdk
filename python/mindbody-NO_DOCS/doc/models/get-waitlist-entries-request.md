
# Get Waitlist Entries Request

## Structure

`GetWaitlistEntriesRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `class_ids` | `List[int]` | Optional | The requested class IDs. If a class ID is present, the request automatically disregards any class schedule IDs in the request. <br /><br>Either `ClassScheduleIds`, `ClientIds`, `WaitlistEntryIds`, or `ClassIds` is required; the others become optional.<br /><br>Default: **all ClassIds** |
| `class_schedule_ids` | `List[int]` | Optional | The requested class schedule IDs. If a class ID is present, the request automatically disregards any class schedule IDs in the request.<br /><br>Either `ClassScheduleIds`, `ClientIds`, `WaitlistEntryIds`, or `ClassIds` is required; the others become optional.<br /><br>Default: **all ClassScheduleIds** |
| `client_ids` | `List[str]` | Optional | The requested client IDs.<br /><br>Either `ClassScheduleIds`, `ClientIds`, `WaitlistEntryIds`, or `ClassIds` is required; the others become optional.<br /><br>Default: **all ClientIds** |
| `hide_past_entries` | `bool` | Optional | When `true`, indicates that past waiting list entries are hidden from clients.<br /><br>When `false`, indicates that past entries are not hidden from clients.<br /><br>Default: **false** |
| `waitlist_entry_ids` | `List[int]` | Optional | The requested waiting list entry IDs.<br /><br>Either `ClassScheduleIds`, `ClientIds`, `WaitlistEntryIds`, or `ClassIds` is required; the others become optional.<br /><br>Default: **all WaitlistEntryIds** |
| `limit` | `int` | Optional | Number of results to include, defaults to 100 |
| `offset` | `int` | Optional | Page offset, defaults to 0. |

## Example (as JSON)

```json
{
  "ClassIds": [
    83,
    84
  ],
  "ClassScheduleIds": [
    92,
    93
  ],
  "ClientIds": [
    "ClientIds7",
    "ClientIds8",
    "ClientIds9"
  ],
  "HidePastEntries": false,
  "WaitlistEntryIds": [
    65,
    66
  ]
}
```

