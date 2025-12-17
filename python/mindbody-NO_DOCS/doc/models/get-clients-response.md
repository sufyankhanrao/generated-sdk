
# Get Clients Response

## Structure

`GetClientsResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `pagination_response` | [`PaginationResponse`](../../doc/models/pagination-response.md) | Optional | Contains information about the pagination to use. |
| `clients` | [`List[ClientWithSuspensionInfo]`](../../doc/models/client-with-suspension-info.md) | Optional | The requested clients. |

## Example (as JSON)

```json
{
  "PaginationResponse": {
    "RequestedLimit": 22,
    "RequestedOffset": 0,
    "PageSize": 172,
    "TotalResults": 112
  },
  "Clients": [
    {
      "SuspensionInfo": {
        "BookingSuspended": false,
        "SuspensionStartDate": "SuspensionStartDate8",
        "SuspensionEndDate": "SuspensionEndDate2"
      },
      "AppointmentGenderPreference": "Female",
      "BirthDate": "2016-03-13T12:52:32.123Z",
      "Country": "Country4",
      "CreationDate": "2016-03-13T12:52:32.123Z"
    }
  ]
}
```

