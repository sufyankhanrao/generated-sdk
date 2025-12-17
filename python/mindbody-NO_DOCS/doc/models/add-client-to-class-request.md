
# Add Client to Class Request

## Structure

`AddClientToClassRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `client_id` | `str` | Required | The ID of the client who is being booked into the class |
| `class_id` | `int` | Required | The ID of the class into which the client is being booked |
| `test` | `bool` | Optional | When `true`, indicates that input information is validated, but not committed.<br /><br>When `false`, the information is committed and the database is affected.<br /><br>Default: **false** |
| `require_payment` | `bool` | Optional | When `true`, the client must have an active, usable pricing option on their account.<br /><br>When `false` or omitted, an active pricing option is not required to complete the client’s booking. |
| `waitlist` | `bool` | Optional | When `true`, indicates that the client should be added to a specific class waiting list.<br /><br>When `false`, the client should not be added to the waiting list. |
| `send_email` | `bool` | Optional | When `true`, the subscriber’s configured Booking Confirmation automatic email is sent to the client. Note that an email is sent only if the client has an email address and automatic emails have been set up.<br /><br>When `false`, indicates that the client does not receive emails.<br /><br>Default: **false**<br>**Note**: When the Authorization header is passed and the SendEmail is set to `true`, then an email will be sent.<br>When the Authorization header is passed and the SendEmail is set to `false`, then an email will not be sent.<br>When the Authorization header is not passed and the SendEmail is set to either `true` or `false`, then an email will not be sent. |
| `waitlist_entry_id` | `int` | Optional | The ID of the waiting list entry from which you are moving a client into a class. |
| `client_service_id` | `int` | Optional | The ID of the pricing option on the client’s account that you want to use to pay for this booking, if payment is required at the time of the update. |
| `cross_regional_booking` | `bool` | Optional | When `true`, cross regional series are checked and used if applicable. |
| `cross_regional_booking_client_service_site_id` | `int` | Optional | If the request is cross regional, use a purchased pricing option from this specified site. If omitted, an attempt is made to use an applicable pricing option from the local site. |
| `unique_id` | `int` | Optional | The UniqueID of the client who is being booked into the class |

## Example (as JSON)

```json
{
  "ClientId": "ClientId6",
  "ClassId": 26,
  "Test": false,
  "RequirePayment": false,
  "Waitlist": false,
  "SendEmail": false,
  "WaitlistEntryId": 246
}
```

