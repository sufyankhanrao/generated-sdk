
# Scheduled Service Earnings Event

## Structure

`ScheduledServiceEarningsEvent`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `staff_id` | `int` | Optional | The ID of the staff member who taught the class. |
| `scheduled_service_id` | `int` | Optional | The class' ID. |
| `scheduled_service_type` | [`ScheduledServiceTypeEnum`](../../doc/models/scheduled-service-type-enum.md) | Optional | The type of the scheduled service; i.e, a class, appointment, or enrollment. |
| `earnings` | `float` | Optional | The total monetary amount the staff is to be paid for this class. |
| `date_time` | `datetime` | Optional | - |

## Example (as JSON)

```json
{
  "StaffId": 110,
  "ScheduledServiceId": 194,
  "ScheduledServiceType": "Enrollment",
  "Earnings": 215.14,
  "DateTime": "2016-03-13T12:52:32.123Z"
}
```

