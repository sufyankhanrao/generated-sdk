
# Pick a Spot Class

Contains information about the PickASpot classes.

## Structure

`PickASpotClass`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `site_id` | `int` | Optional | The unique ID of the Site. |
| `location_id` | `int` | Optional | The unique ID of the Location. |
| `class_id` | `str` | Optional | The unique ID of the Class. |
| `class_external_id` | `str` | Optional | The unique Class external ID. |
| `class_name` | `str` | Optional | Contains the class name. |
| `class_start_time` | `datetime` | Optional | Class start time. |
| `class_end_time` | `datetime` | Optional | Class end time. |
| `class_maximum_capacity` | `int` | Optional | Contains information about the Class maximum capacity. |
| `room_id` | `str` | Optional | The unique Room ID. |
| `spots` | [`Spot`](../../doc/models/spot.md) | Optional | Contains information about the spot details. |
| `reservations` | [`List[Reservation]`](../../doc/models/reservation.md) | Optional | Contains information about the reservation collection. |

## Example (as JSON)

```json
{
  "SiteId": 2,
  "LocationId": 144,
  "ClassId": "ClassId0",
  "ClassExternalId": "ClassExternalId0",
  "ClassName": "ClassName6"
}
```

