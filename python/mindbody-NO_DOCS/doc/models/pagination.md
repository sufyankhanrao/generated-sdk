
# Pagination

Contains information about the pagination used.

## Structure

`Pagination`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `page_number` | `int` | Optional | Page number of results in dataset. |
| `page_size` | `int` | Optional | Number of results returned in this response. |
| `total_result_count` | `int` | Optional | Total number of results in dataset. |
| `total_page_count` | `int` | Optional | Total number of page in dataset. |

## Example (as JSON)

```json
{
  "PageNumber": 54,
  "PageSize": 136,
  "TotalResultCount": 152,
  "TotalPageCount": 222
}
```

