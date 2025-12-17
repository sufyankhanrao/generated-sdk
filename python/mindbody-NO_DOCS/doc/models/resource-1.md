
# Resource 1

## Structure

`Resource1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `int` | Optional | - |
| `name` | `str` | Optional | - |
| `location_id` | `int` | Optional | - |
| `is_active` | `bool` | Optional | - |
| `schedule_types` | [`List[ScheduleType4Enum]`](../../doc/models/schedule-type-4-enum.md) | Optional | - |
| `program_ids` | `List[int]` | Optional | - |

## Example (as JSON)

```json
{
  "Id": 168,
  "Name": "Name8",
  "LocationId": 28,
  "IsActive": false,
  "ScheduleTypes": [
    "Media",
    "Resource",
    "Appointment"
  ]
}
```

