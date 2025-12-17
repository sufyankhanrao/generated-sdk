
# Assign Staff Session Type Request

## Structure

`AssignStaffSessionTypeRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `staff_id` | `int` | Required | The ID of the staff member session type is getting assigned to. The staff member must be assignable to appointments or already be assigned to the session type in the request.<br><br>**Constraints**: `>= 1` |
| `session_type_id` | `int` | Required | The ID of the session type that is getting assigned to the staff member. The session type must be an appointment.<br><br>**Constraints**: `>= 1`, `<= 2147483647` |
| `active` | `bool` | Required | Indicates if assignment is active. Passing `false` is equivalent to deleting the assignment. |
| `time_length` | `int` | Optional | The staff specific amount of time that a session of this type typically lasts. |
| `prep_time` | `int` | Optional | Prep time in minutes |
| `finish_time` | `int` | Optional | Finish time in minutes |
| `pay_rate_type` | `str` | Optional | The pay rate type. Can be one of the following (case insensitive):<br>Percent<br>Flat<br>No Pay<br>If PayRateType is not provided in the request and the request is creating a completely new assignment (not editing an existing active or inactive assignment), then the staff member default pay rate and pay rate amount are used to create the assignment. Otherwise, the existing assignment values are used for any optional request parameters not included in the request. |
| `pay_rate_amount` | `float` | Optional | The pay rate amount for the specific staff member. It is parsed according to the PayRateType. |

## Example (as JSON)

```json
{
  "StaffId": 226,
  "SessionTypeId": 120,
  "Active": false,
  "TimeLength": 4,
  "PrepTime": 52,
  "FinishTime": 28,
  "PayRateType": "PayRateType6",
  "PayRateAmount": 65.04
}
```

