
# Generate Signed Live Stream Url Request

Request to create an encrypted live stream url

## Structure

`GenerateSignedLiveStreamUrlRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `client_id` | `int` | Optional | Id of client at the studio |
| `subscriber_id` | `int` | Optional | Id of studio aka studioId/siteId |
| `user_display_name` | `str` | Optional | User name displayed in VWP live stream |
| `service_id` | `int` | Optional | Id of class instance at studio on given date/time right now since it only supports classes (different from class id) |
| `api_user` | `str` | Optional | Identification of 3rd party integrator |
| `service_type` | `str` | Optional | Possible values are: "class", "appointment" |

## Example (as JSON)

```json
{
  "ClientId": 244,
  "SubscriberId": 88,
  "UserDisplayName": "UserDisplayName8",
  "ServiceId": 236,
  "ApiUser": "ApiUser8"
}
```

