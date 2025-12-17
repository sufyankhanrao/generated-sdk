
# Get Staff Appointments Response

Get Staff Appointments Response Model

## Structure

`GetStaffAppointmentsResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `pagination_response` | [`PaginationResponse`](../../doc/models/pagination-response.md) | Optional | Contains information about the pagination to use. |
| `appointments` | [`List[Appointment]`](../../doc/models/appointment.md) | Optional | Contains information about appointments and their details. |

## Example (as JSON)

```json
{
  "PaginationResponse": {
    "RequestedLimit": 22,
    "RequestedOffset": 0,
    "PageSize": 172,
    "TotalResults": 112
  },
  "Appointments": [
    {
      "GenderPreference": "None",
      "Duration": 20,
      "ProviderId": "ProviderId8",
      "Id": 230,
      "Status": "Completed"
    },
    {
      "GenderPreference": "None",
      "Duration": 20,
      "ProviderId": "ProviderId8",
      "Id": 230,
      "Status": "Completed"
    },
    {
      "GenderPreference": "None",
      "Duration": 20,
      "ProviderId": "ProviderId8",
      "Id": 230,
      "Status": "Completed"
    }
  ]
}
```

