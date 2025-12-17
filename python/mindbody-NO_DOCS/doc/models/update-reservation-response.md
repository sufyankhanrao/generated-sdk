
# Update Reservation Response

Contains information about the update reservation response.

## Structure

`UpdateReservationResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `reservation` | [`Reservation`](../../doc/models/reservation.md) | Optional | Contains information about the reservation. |
| `response_details` | [`ResponseDetails`](../../doc/models/response-details.md) | Optional | Contains information about the response message detail. |

## Example (as JSON)

```json
{
  "Reservation": {
    "ReservationId": "ReservationId2",
    "ReservationExternalId": "ReservationExternalId4",
    "ClassId": "ClassId4",
    "ClassExternalId": "ClassExternalId6",
    "MemberExternalId": "MemberExternalId4"
  },
  "ResponseDetails": {
    "Status": "Status2",
    "TransactionId": "TransactionId4",
    "Message": "Message0"
  }
}
```

