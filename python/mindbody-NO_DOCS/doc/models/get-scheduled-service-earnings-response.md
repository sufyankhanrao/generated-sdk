
# Get Scheduled Service Earnings Response

## Structure

`GetScheduledServiceEarningsResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `pagination_response` | [`PaginationResponse`](../../doc/models/pagination-response.md) | Optional | Contains information about the pagination to use. |
| `scheduled_service_earnings` | [`List[ScheduledServiceEarningsEvent]`](../../doc/models/scheduled-service-earnings-event.md) | Optional | Contains the class payroll events. |

## Example (as JSON)

```json
{
  "PaginationResponse": {
    "RequestedLimit": 22,
    "RequestedOffset": 0,
    "PageSize": 172,
    "TotalResults": 112
  },
  "ScheduledServiceEarnings": [
    {
      "StaffId": 166,
      "ScheduledServiceId": 250,
      "ScheduledServiceType": "Enrollment",
      "Earnings": 69.78,
      "DateTime": "2016-03-13T12:52:32.123Z"
    },
    {
      "StaffId": 166,
      "ScheduledServiceId": 250,
      "ScheduledServiceType": "Enrollment",
      "Earnings": 69.78,
      "DateTime": "2016-03-13T12:52:32.123Z"
    },
    {
      "StaffId": 166,
      "ScheduledServiceId": 250,
      "ScheduledServiceType": "Enrollment",
      "Earnings": 69.78,
      "DateTime": "2016-03-13T12:52:32.123Z"
    }
  ]
}
```

