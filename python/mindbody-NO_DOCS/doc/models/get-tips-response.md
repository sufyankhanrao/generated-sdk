
# Get Tips Response

## Structure

`GetTipsResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `pagination_response` | [`PaginationResponse`](../../doc/models/pagination-response.md) | Optional | Contains information about the pagination to use. |
| `tips` | [`List[Tip]`](../../doc/models/tip.md) | Optional | Contains information about tips given to staff members within the given date range. Results are ordered by StaffId. |

## Example (as JSON)

```json
{
  "PaginationResponse": {
    "RequestedLimit": 22,
    "RequestedOffset": 0,
    "PageSize": 172,
    "TotalResults": 112
  },
  "Tips": [
    {
      "StaffId": 92,
      "SaleId": 254,
      "SaleDateTime": "2016-03-13T12:52:32.123Z",
      "Earnings": 148.4
    }
  ]
}
```

