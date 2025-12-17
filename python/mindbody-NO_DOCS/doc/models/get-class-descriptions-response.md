
# Get Class Descriptions Response

## Structure

`GetClassDescriptionsResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `pagination_response` | [`PaginationResponse`](../../doc/models/pagination-response.md) | Optional | Contains information about the pagination to use. |
| `class_descriptions` | [`List[ClassDescription]`](../../doc/models/class-description.md) | Optional | Contains information about the class descriptions. |

## Example (as JSON)

```json
{
  "PaginationResponse": {
    "RequestedLimit": 22,
    "RequestedOffset": 0,
    "PageSize": 172,
    "TotalResults": 112
  },
  "ClassDescriptions": [
    {
      "Active": false,
      "Description": "Description0",
      "Id": 112,
      "ImageURL": "ImageURL6",
      "LastUpdated": "2016-03-13T12:52:32.123Z"
    },
    {
      "Active": false,
      "Description": "Description0",
      "Id": 112,
      "ImageURL": "ImageURL6",
      "LastUpdated": "2016-03-13T12:52:32.123Z"
    },
    {
      "Active": false,
      "Description": "Description0",
      "Id": 112,
      "ImageURL": "ImageURL6",
      "LastUpdated": "2016-03-13T12:52:32.123Z"
    }
  ]
}
```

