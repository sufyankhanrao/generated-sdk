
# Add Arrival Request

## Structure

`AddArrivalRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `client_id` | `str` | Required | The ID of the requested client. |
| `location_id` | `int` | Required | The ID of the location for the requested arrival. |
| `arrival_type_id` | `int` | Optional | The ID of the arrival program (service category) under which this arrival is to be logged. If this is not provided, the program ID of the first arrival pricing option found will be used.<br>OPTIONAL: will take first payment found if not provided<br>Default: **null** |
| `lead_channel_id` | `int` | Optional | The ID of the Lead Channel ID from lead management. If this is supplied then it will map lead channel on the lead management.<br>If this is not supplied then it wont save anything.<br>This parameters required to track the lead channel if new client added while adding arrival of client on non home location. |
| `test` | `bool` | Optional | When `true`, indicates that the arrival log is to be validated, but no new arrival data is added. When `false`, the arrival is logged and the database is affected.<br>Default: **false** |

## Example (as JSON)

```json
{
  "ClientId": "ClientId2",
  "LocationId": 236,
  "ArrivalTypeId": 158,
  "LeadChannelId": 254,
  "Test": false
}
```

