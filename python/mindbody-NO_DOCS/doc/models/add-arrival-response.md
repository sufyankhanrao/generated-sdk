
# Add Arrival Response

## Structure

`AddArrivalResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `arrival_added` | `bool` | Optional | When `true`, indicates that the arrival was added to the database. |
| `client_service` | [`ClientService`](../../doc/models/client-service.md) | Optional | A service that is on a client's account. |

## Example (as JSON)

```json
{
  "ArrivalAdded": false,
  "ClientService": {
    "ActiveDate": "2016-03-13T12:52:32.123Z",
    "Count": 70,
    "Current": false,
    "ExpirationDate": "2016-03-13T12:52:32.123Z",
    "Id": 6
  }
}
```

