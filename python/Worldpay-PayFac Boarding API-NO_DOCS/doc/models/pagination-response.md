
# Pagination Response

## Structure

`PaginationResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `page_number` | `int` | Optional | Page number as per the request |
| `page_size` | `int` | Optional | Number of records retrieved per page as per the request |
| `total_row_count` | `int` | Optional | Total number of records meeting the search criteria |
| `total_returned_count` | `int` | Optional | Total number of records returned in the response. This would have the same value as Page Size when Total Row count is greater than the Page Size. |

## Example (as JSON)

```json
{
  "pageNumber": 1,
  "pageSize": 50,
  "totalRowCount": 85,
  "totalReturnedCount": 25
}
```

