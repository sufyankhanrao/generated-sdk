
# Get Client Visits Response

## Structure

`GetClientVisitsResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `pagination_response` | [`PaginationResponse`](../../doc/models/pagination-response.md) | Optional | Contains information about the pagination to use. |
| `visits` | [`List[Visit]`](../../doc/models/visit.md) | Optional | Contains information about client visits. |

## Example (as JSON)

```json
{
  "PaginationResponse": {
    "RequestedLimit": 22,
    "RequestedOffset": 0,
    "PageSize": 172,
    "TotalResults": 112
  },
  "Visits": [
    {
      "AppointmentId": 196,
      "AppointmentGenderPreference": "Male",
      "AppointmentStatus": "Booked",
      "ClassId": 140,
      "ClientId": "ClientId4"
    },
    {
      "AppointmentId": 196,
      "AppointmentGenderPreference": "Male",
      "AppointmentStatus": "Booked",
      "ClassId": 140,
      "ClientId": "ClientId4"
    }
  ]
}
```

