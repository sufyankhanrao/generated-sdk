
# Reservation

Contains information about the reservation.

## Structure

`Reservation`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `reservation_id` | `str` | Optional | The unique reservation ID. |
| `reservation_external_id` | `str` | Optional | The unique reservation external ID. |
| `class_id` | `str` | Optional | The unique class ID. |
| `class_external_id` | `str` | Optional | The unique class external ID. |
| `member_external_id` | `str` | Optional | The unique member external ID. |
| `reservation_type` | `str` | Optional | Contains information about the reservation type. |
| `spots` | [`Spot`](../../doc/models/spot.md) | Optional | Contains information about the spot details. |
| `is_confirmed` | `bool` | Optional | Boolean value whether it is confirmed. |
| `confirmation_date` | `datetime` | Optional | Contains information about the confirmation date. |

## Example (as JSON)

```json
{
  "ReservationId": "ReservationId2",
  "ReservationExternalId": "ReservationExternalId4",
  "ClassId": "ClassId4",
  "ClassExternalId": "ClassExternalId6",
  "MemberExternalId": "MemberExternalId4"
}
```

