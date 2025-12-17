
# Booking Window

The booking window for registration

## Structure

`BookingWindow`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `start_date_time` | `datetime` | Optional | Date and time that the booking window opens; that is, the first day of sales. |
| `end_date_time` | `datetime` | Optional | Date and time that the booking window closes; that is, the last day of sales. |
| `daily_start_time` | `datetime` | Optional | The time that the booking window opens; that is, the time that the store opens. |
| `daily_end_time` | `datetime` | Optional | The time that the booking window closes; that is, the time that the store closes. |

## Example (as JSON)

```json
{
  "StartDateTime": "2016-03-13T12:52:32.123Z",
  "EndDateTime": "2016-03-13T12:52:32.123Z",
  "DailyStartTime": "2016-03-13T12:52:32.123Z",
  "DailyEndTime": "2016-03-13T12:52:32.123Z"
}
```

