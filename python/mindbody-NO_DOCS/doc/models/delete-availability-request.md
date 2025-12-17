
# Delete Availability Request

This is the delete availability request coming DTO

## Structure

`DeleteAvailabilityRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `availability_id` | `int` | Optional | The ID of the availability or unavailability. |
| `test` | `bool` | Optional | When `true`, indicates that this is a test request and no data is deleted from the subscriber’s database.<br>When `false`, the record will be deleted.<br>Default: **false** |

## Example (as JSON)

```json
{
  "AvailabilityId": 36,
  "Test": false
}
```

