
# Get Client Account Balances Response

## Structure

`GetClientAccountBalancesResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `pagination_response` | [`PaginationResponse`](../../doc/models/pagination-response.md) | Optional | Contains information about the pagination to use. |
| `clients` | [`List[Client]`](../../doc/models/client.md) | Optional | A list of clients. |

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
      "AppointmentGenderPreference": "Female",
      "BirthDate": "2016-03-13T12:52:32.123Z",
      "Country": "Country4",
      "CreationDate": "2016-03-13T12:52:32.123Z",
      "CustomClientFields": [
        {
          "Value": "Value6",
          "Id": 112,
          "DataType": "DataType2",
          "Name": "Name8"
        },
        {
          "Value": "Value6",
          "Id": 112,
          "DataType": "DataType2",
          "Name": "Name8"
        }
      ]
    },
    {
      "AppointmentGenderPreference": "Female",
      "BirthDate": "2016-03-13T12:52:32.123Z",
      "Country": "Country4",
      "CreationDate": "2016-03-13T12:52:32.123Z",
      "CustomClientFields": [
        {
          "Value": "Value6",
          "Id": 112,
          "DataType": "DataType2",
          "Name": "Name8"
        },
        {
          "Value": "Value6",
          "Id": 112,
          "DataType": "DataType2",
          "Name": "Name8"
        }
      ]
    },
    {
      "AppointmentGenderPreference": "Female",
      "BirthDate": "2016-03-13T12:52:32.123Z",
      "Country": "Country4",
      "CreationDate": "2016-03-13T12:52:32.123Z",
      "CustomClientFields": [
        {
          "Value": "Value6",
          "Id": 112,
          "DataType": "DataType2",
          "Name": "Name8"
        },
        {
          "Value": "Value6",
          "Id": 112,
          "DataType": "DataType2",
          "Name": "Name8"
        }
      ]
    }
  ]
}
```

