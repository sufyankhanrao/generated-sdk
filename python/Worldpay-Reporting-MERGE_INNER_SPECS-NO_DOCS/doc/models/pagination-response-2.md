
# Pagination Response 2

## Structure

`PaginationResponse2`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `page_number` | `int` | Optional | Current page number returned.<br><br>**Constraints**: `>= 0`, `<= 10000000000000000` |
| `page_size` | `int` | Optional | Total number of records returned per page.<br><br>**Constraints**: `>= 0`, `<= 10000000000000000` |
| `total_row_count` | `int` | Optional | Total number of records meeting the search criteria.<br><br>**Constraints**: `>= 0`, `<= 10000000000000000` |
| `total_returned_count` | `int` | Optional | Total number of records returned in the response.<br><br>**Constraints**: `>= 0`, `<= 10000000000000000` |

## Example (as JSON)

```json
{
  "pageNumber": 1,
  "pageSize": 50,
  "totalRowCount": 85,
  "totalReturnedCount": 25
}
```

