
# Get Semesters Response

Get Semesters Response Model

## Structure

`GetSemestersResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `pagination_response` | [`PaginationResponse`](../../doc/models/pagination-response.md) | Optional | Contains information about the pagination to use. |
| `semesters` | [`List[Semester]`](../../doc/models/semester.md) | Optional | Contains the Semester objects, each of which describes the semesters for a site. |

## Example (as JSON)

```json
{
  "PaginationResponse": {
    "RequestedLimit": 22,
    "RequestedOffset": 0,
    "PageSize": 172,
    "TotalResults": 112
  },
  "Semesters": [
    {
      "Id": 204,
      "Name": "Name2",
      "Description": "Description6",
      "StartDate": "2016-03-13T12:52:32.123Z",
      "EndDate": "2016-03-13T12:52:32.123Z"
    },
    {
      "Id": 204,
      "Name": "Name2",
      "Description": "Description6",
      "StartDate": "2016-03-13T12:52:32.123Z",
      "EndDate": "2016-03-13T12:52:32.123Z"
    },
    {
      "Id": 204,
      "Name": "Name2",
      "Description": "Description6",
      "StartDate": "2016-03-13T12:52:32.123Z",
      "EndDate": "2016-03-13T12:52:32.123Z"
    }
  ]
}
```

