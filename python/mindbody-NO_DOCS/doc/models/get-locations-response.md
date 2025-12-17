
# Get Locations Response

## Structure

`GetLocationsResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `pagination_response` | [`PaginationResponse`](../../doc/models/pagination-response.md) | Optional | Contains information about the pagination to use. |
| `locations` | [`List[Location]`](../../doc/models/location.md) | Optional | Contains information about the locations. |

## Example (as JSON)

```json
{
  "PaginationResponse": {
    "RequestedLimit": 22,
    "RequestedOffset": 0,
    "PageSize": 172,
    "TotalResults": 112
  },
  "Locations": [
    {
      "AdditionalImageURLs": [
        "AdditionalImageURLs2"
      ],
      "Address": "Address6",
      "Address2": "Address28",
      "Amenities": [
        {
          "Id": 214,
          "Name": "Name8"
        },
        {
          "Id": 214,
          "Name": "Name8"
        },
        {
          "Id": 214,
          "Name": "Name8"
        }
      ],
      "BusinessDescription": "BusinessDescription2"
    },
    {
      "AdditionalImageURLs": [
        "AdditionalImageURLs2"
      ],
      "Address": "Address6",
      "Address2": "Address28",
      "Amenities": [
        {
          "Id": 214,
          "Name": "Name8"
        },
        {
          "Id": 214,
          "Name": "Name8"
        },
        {
          "Id": 214,
          "Name": "Name8"
        }
      ],
      "BusinessDescription": "BusinessDescription2"
    },
    {
      "AdditionalImageURLs": [
        "AdditionalImageURLs2"
      ],
      "Address": "Address6",
      "Address2": "Address28",
      "Amenities": [
        {
          "Id": 214,
          "Name": "Name8"
        },
        {
          "Id": 214,
          "Name": "Name8"
        },
        {
          "Id": 214,
          "Name": "Name8"
        }
      ],
      "BusinessDescription": "BusinessDescription2"
    }
  ]
}
```

