
# Devices Published After Date Response

## Structure

`DevicesPublishedAfterDateResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `number_of_devices` | `int` | Optional | The id of a site. |
| `authorized_device_ids` | `List[int]` | Optional | **Constraints**: `>= 1` |

## Example (as JSON)

```json
{
  "numberOfDevices": 204,
  "authorizedDeviceIds": [
    12,
    13
  ]
}
```

