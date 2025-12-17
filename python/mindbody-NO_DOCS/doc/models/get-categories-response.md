
# Get Categories Response

Get Categories Response Model

## Structure

`GetCategoriesResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `pagination_response` | [`PaginationResponse`](../../doc/models/pagination-response.md) | Optional | Contains information about the pagination to use. |
| `categories` | [`List[Category]`](../../doc/models/category.md) | Optional | Contains the Category objects, each of which describes the categories for a site. |

## Example (as JSON)

```json
{
  "PaginationResponse": {
    "RequestedLimit": 22,
    "RequestedOffset": 0,
    "PageSize": 172,
    "TotalResults": 112
  },
  "Categories": [
    {
      "Id": 240,
      "CategoryName": "CategoryName6",
      "Description": "Description2",
      "Service": false,
      "Active": false
    },
    {
      "Id": 240,
      "CategoryName": "CategoryName6",
      "Description": "Description2",
      "Service": false,
      "Active": false
    },
    {
      "Id": 240,
      "CategoryName": "CategoryName6",
      "Description": "Description2",
      "Service": false,
      "Active": false
    }
  ]
}
```

