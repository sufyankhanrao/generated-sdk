
# Get Contact Log Types Response

## Structure

`GetContactLogTypesResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `pagination_response` | [`PaginationResponse`](../../doc/models/pagination-response.md) | Optional | Contains information about the pagination to use. |
| `contact_log_types` | [`List[ContactLogType]`](../../doc/models/contact-log-type.md) | Optional | The requested Active ContactLogTypes |

## Example (as JSON)

```json
{
  "PaginationResponse": {
    "RequestedLimit": 22,
    "RequestedOffset": 0,
    "PageSize": 172,
    "TotalResults": 112
  },
  "ContactLogTypes": [
    {
      "Id": 34,
      "Name": "Name0",
      "SubTypes": [
        {
          "Id": 102,
          "Name": "Name6"
        },
        {
          "Id": 102,
          "Name": "Name6"
        },
        {
          "Id": 102,
          "Name": "Name6"
        }
      ]
    },
    {
      "Id": 34,
      "Name": "Name0",
      "SubTypes": [
        {
          "Id": 102,
          "Name": "Name6"
        },
        {
          "Id": 102,
          "Name": "Name6"
        },
        {
          "Id": 102,
          "Name": "Name6"
        }
      ]
    },
    {
      "Id": 34,
      "Name": "Name0",
      "SubTypes": [
        {
          "Id": 102,
          "Name": "Name6"
        },
        {
          "Id": 102,
          "Name": "Name6"
        },
        {
          "Id": 102,
          "Name": "Name6"
        }
      ]
    }
  ]
}
```

