
# Get Reservation Response

Contains information about the get reservation response

## Structure

`GetReservationResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `reservations` | [`List[Reservation]`](../../doc/models/reservation.md) | Optional | Contains information about the reservation details. |
| `pagination` | [`Pagination`](../../doc/models/pagination.md) | Optional | Contains information about the pagination used. |
| `response_details` | [`ResponseDetails`](../../doc/models/response-details.md) | Optional | Contains information about the response message detail. |

## Example (as JSON)

```json
{
  "Reservations": [
    {
      "ReservationId": "ReservationId0",
      "ReservationExternalId": "ReservationExternalId6",
      "ClassId": "ClassId6",
      "ClassExternalId": "ClassExternalId6",
      "MemberExternalId": "MemberExternalId6"
    }
  ],
  "Pagination": {
    "PageNumber": 54,
    "PageSize": 136,
    "TotalResultCount": 152,
    "TotalPageCount": 222
  },
  "ResponseDetails": {
    "Status": "Status2",
    "TransactionId": "TransactionId4",
    "Message": "Message0"
  }
}
```

