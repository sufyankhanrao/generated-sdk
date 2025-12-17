
# Update Client Request

## Structure

`UpdateClientRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `client` | [`ClientWithSuspensionInfo`](../../doc/models/client-with-suspension-info.md) | Required | A Client DTO with Suspension Informatoin |
| `test` | `bool` | Optional | When `true`, indicates that test mode is enabled. The method is validated, but no client data is added or updated.<br /><br>Default: **false** |
| `cross_regional_update` | `bool` | Optional | When `true`, the updated information is propagated to all of the region’s sites where the client has a profile.<br /><br>When `false`, only the local client is updated.<br /><br>Default: **true** |
| `new_id` | `str` | Optional | The new RSSID to be used for the client. Use `NewId` to assign a specific number to be a client’s ID. If that number is not available, the call returns an error. This RSSID must be unique within the subscriber’s site. If this is a cross-regional update, the RSSID must be unique across the region. If the requested number is already in use, an error is returned. |
| `lead_channel_id` | `int` | Optional | The ID of the Lead Channel ID from lead management. If this is supplied then it will map lead channel on the lead management.<br>If this is not supplied then it will have Publicapi LeadChannelId.<br>This parameters required to track the lead channel if new client added to the location. |

## Example (as JSON)

```json
{
  "Client": {
    "SuspensionInfo": {
      "BookingSuspended": false,
      "SuspensionStartDate": "SuspensionStartDate8",
      "SuspensionEndDate": "SuspensionEndDate2"
    },
    "AppointmentGenderPreference": "None",
    "BirthDate": "2016-03-13T12:52:32.123Z",
    "Country": "Country8",
    "CreationDate": "2016-03-13T12:52:32.123Z"
  },
  "Test": false,
  "CrossRegionalUpdate": false,
  "NewId": "NewId0",
  "LeadChannelId": 72
}
```

