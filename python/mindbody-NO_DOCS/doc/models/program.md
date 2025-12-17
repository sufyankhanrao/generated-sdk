
# Program

## Structure

`Program`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `int` | Optional | The service category’s ID. |
| `name` | `str` | Optional | The name of this service category. |
| `schedule_type` | [`ScheduleTypeEnum`](../../doc/models/schedule-type-enum.md) | Optional | The service category’s schedule type. Possible values are:<br><br>* All<br>* Class<br>* Enrollment<br>* Appointment<br>* Resource<br>* Arrival |
| `cancel_offset` | `int` | Optional | The offset to use for the service category. |
| `content_formats` | `List[str]` | Optional | The content delivery platform(s) used by the service category. Possible values are:<br><br>* InPerson<br>* Livestream:Mindbody<br>* Livestream:Other |
| `schedule_offset` | `int` | Optional | Scheduling window offset |
| `schedule_offset_end` | `int` | Optional | Scheduling window offset end |
| `pricing_relationships` | [`PricingRelationships`](../../doc/models/pricing-relationships.md) | Optional | - |

## Example (as JSON)

```json
{
  "Id": 104,
  "Name": "Name0",
  "ScheduleType": "Arrival",
  "CancelOffset": 94,
  "ContentFormats": [
    "ContentFormats1",
    "ContentFormats2"
  ]
}
```

