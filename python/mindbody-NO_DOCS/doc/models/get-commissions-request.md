
# Get Commissions Request

## Structure

`GetCommissionsRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `staff_id` | `int` | Optional | A list of staff IDs that you want to retrieve payroll information for. If you do not supply a `StaffId`, all active staff members return, ordered by staff ID. |
| `start_date_time` | `datetime` | Optional | The beginning of the date range for the payroll information to be returned. The maximum allowed date range is 14 days.<br><br>* If you do not supply a `StartDateTime`, data returns for the seven days prior to the `EndDateTime` that you supply.<br>* If you do not supply either a `StartDateTime` or an `EndDateTime`, the data returns for seven days prior to today’s date. |
| `end_date_time` | `datetime` | Optional | The end of the date range for the payroll information to be returned. The maximum allowed date range is 14 days.<br /><br>Default: **Today’s date**<br><br>* If you do not supply an `EndDateTime`, the data returns for the period from the `StartDateTime` that you supply to today’s date.<br>* If you do not supply an `EndDateTime` or a `StartDateTime`, data returns for the seven days prior to today’s date. |
| `location_id` | `int` | Optional | A LocationId that you want to retrieve payroll information for. If you do not supply a `LocationId`, data from all locations is returned. |
| `limit` | `int` | Optional | Number of results to include, defaults to 100 |
| `offset` | `int` | Optional | Page offset, defaults to 0. |

## Example (as JSON)

```json
{
  "StaffId": 28,
  "StartDateTime": "2016-03-13T12:52:32.123Z",
  "EndDateTime": "2016-03-13T12:52:32.123Z",
  "LocationId": 178,
  "Limit": 128
}
```

