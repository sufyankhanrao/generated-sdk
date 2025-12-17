
# Add Client to Enrollment Request

Add Client To Enrollment Request Model

## Structure

`AddClientToEnrollmentRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `client_id` | `str` | Required | The client IDs of the clients to add to the specified enrollments. |
| `class_schedule_id` | `int` | Required | The class schedule IDs of the enrollments to add the clients to. The ClassScheduleId can be found in GetEnrollments as the EnrollmentId. |
| `enroll_date_forward` | `datetime` | Optional | Enroll the clients from this date forward. `EnrollDateForward` takes priority over open enrollment.<br>Default: **null** |
| `enroll_open` | `List[datetime]` | Optional | Enroll for selected dates. |
| `test` | `bool` | Optional | When `true`, input information is validated, but not committed.<br /><br>Default: **false** |
| `send_email` | `bool` | Optional | When `true`, indicates that the client should be sent an email. An email is only sent if the client has an email address and automatic emails have been set up. <br /><br>Default: **false** |
| `waitlist` | `bool` | Optional | When `true`, the client is added to a specific enrollments waiting list.<br>Default: **false** |
| `waitlist_entry_id` | `int` | Optional | The waiting list entry to add. Used to add a client to an enrollment from a waiting list entry. |

## Example (as JSON)

```json
{
  "ClientId": "ClientId4",
  "ClassScheduleId": 238,
  "EnrollDateForward": "2016-03-13T12:52:32.123Z",
  "EnrollOpen": [
    "2016-03-13T12:52:32.123Z",
    "2016-03-13T12:52:32.123Z"
  ],
  "Test": false,
  "SendEmail": false,
  "Waitlist": false
}
```

