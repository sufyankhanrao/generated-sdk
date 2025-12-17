
# Pagination Response

Pagination response details

## Structure

`PaginationResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `page_number` | `int` | Optional | This is the page number that you would like to retrieve.<br><br>**Default**: `0`<br><br>**Constraints**: `<= 9999` |
| `page_size` | `int` | Optional | Number of record that you would want to retrieve per page.<br><br>**Default**: `25`<br><br>**Constraints**: `<= 2000` |
| `total_row_count` | `int` | Optional | Total number of records meeting the search criteria<br><br>**Constraints**: `<= 2000` |
| `total_returned_count` | `int` | Optional | Total number of records returned in the response<br><br>**Constraints**: `<= 2000` |

## Example (as JSON)

```json
{
  "pageNumber": 1,
  "pageSize": 50,
  "totalRowCount": 45,
  "totalReturnedCount": 25
}
```

