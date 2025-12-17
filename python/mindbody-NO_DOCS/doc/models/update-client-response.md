
# Update Client Response

## Structure

`UpdateClientResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `client` | [`ClientWithSuspensionInfo`](../../doc/models/client-with-suspension-info.md) | Optional | A Client DTO with Suspension Informatoin |

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
  }
}
```

