
# Assign Staff Session Type Response

## Structure

`AssignStaffSessionTypeResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `staff_id` | `int` | Optional | Staff member assigned to the session type |
| `session_type_id` | `int` | Optional | The session type the staff member is assigned to |
| `pay_rate_type` | `str` | Optional | The pay rate type name<br>Can be: "Flat", "Percent", or "No Pay" |
| `pay_rate_amount` | `float` | Optional | The pay rate amount. It is interpreted based on the value of PayRateTypeId |
| `time_length` | `int` | Optional | The staff specific amount of time that a session of this type typically lasts. |
| `prep_time` | `int` | Optional | Prep time in minutes |
| `finish_time` | `int` | Optional | Finish time in minutes |
| `active` | `bool` | Optional | Whether this association is active |

## Example (as JSON)

```json
{
  "StaffId": 148,
  "SessionTypeId": 42,
  "PayRateType": "PayRateType0",
  "PayRateAmount": 87.3,
  "TimeLength": 182
}
```

