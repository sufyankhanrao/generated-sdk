
# Pagination Type 1

Used for pagination.

## Structure

`PaginationType1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `page_number` | `int` | Optional | This is the page number that you would like to retrieve.<br><br>**Default**: `1`<br><br>**Constraints**: `<= 16777215` |
| `page_size` | `int` | Optional | Number of record that you would want to retrieve per page.<br><br>**Default**: `25`<br><br>**Constraints**: `<= 2000` |

## Example (as JSON)

```json
{
  "pageNumber": 2,
  "pageSize": 10
}
```

