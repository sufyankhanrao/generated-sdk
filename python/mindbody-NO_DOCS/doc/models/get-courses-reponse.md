
# Get Courses Reponse

This is the response class for the get courses API

## Structure

`GetCoursesReponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `pagination_response` | [`PaginationResponse`](../../doc/models/pagination-response.md) | Optional | Contains information about the pagination to use. |
| `courses` | [`List[Course]`](../../doc/models/course.md) | Optional | This is the list course data |

## Example (as JSON)

```json
{
  "PaginationResponse": {
    "RequestedLimit": 22,
    "RequestedOffset": 0,
    "PageSize": 172,
    "TotalResults": 112
  },
  "Courses": [
    {
      "Id": 34,
      "Name": "Name4",
      "Description": "Description8",
      "Notes": "Notes6",
      "StartDate": "2016-03-13T12:52:32.123Z"
    },
    {
      "Id": 34,
      "Name": "Name4",
      "Description": "Description8",
      "Notes": "Notes6",
      "StartDate": "2016-03-13T12:52:32.123Z"
    }
  ]
}
```

