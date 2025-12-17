
# Update Client Rewards Request

Request object for using the API to Earn or Redeem reward points

## Structure

`UpdateClientRewardsRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `client_id` | `str` | Required | The ID of the client that is getting rewards earned or redeemed. |
| `points` | `int` | Required | The amount of points the client is getting earned or redeemed, must be a positive number.<br><br>**Constraints**: `>= 1` |
| `source` | `str` | Optional | If Action passed as **Earned**,<br><br>possible values are:<br><br>* Appointment Booking<br>* Class Booking<br>* Referral<br>* Sale<br><br><br />Omit if Action passed as **Redeemed**. |
| `source_id` | `int` | Optional | The unique identifier in the MINDBODY system for the **Source**. If Action is **Earned**, and an optional SourceID is provided, it is validated as follows:<br><br>* If Source is Appointment Booking, then a provided SourceID must be a valid Visit.AppointmentId for the indicated Client.<br>* If Source is **Class Booking**, then a provided SourceID must be a valid Visit.Id for the indicated client.<br>* If Source is **Sale**, then a provided SourceID must be a valid Sale.Id for the indicated client.<br>* If Source is **Referral**, then a provided SourceID must be a valid Client.Id (RelatedClientId) and have been referred by the indicated client (ClientRelationship.Id = -1).<br>  If Action is **Redeemed**, and an optional SourceID is provided, then SourceID must be a valid Sale.Id for the indicated client, and refers to the sale where the indicated points were redeemed. |
| `action` | `str` | Required | Indicates if rewards are getting earned or redeemed.<br><br>Possible values are:<br>*Earned<br>*Redeemed |
| `action_date_time` | `datetime` | Optional | The date and time when the points were earned or redeemed in UTC format. This date may be in the past, however it may not be in the future.<br>Default: **current date/time** |

## Example (as JSON)

```json
{
  "ClientId": "ClientId6",
  "Points": 136,
  "Source": "Source2",
  "SourceId": 238,
  "Action": "Action2",
  "ActionDateTime": "2016-03-13T12:52:32.123Z"
}
```

