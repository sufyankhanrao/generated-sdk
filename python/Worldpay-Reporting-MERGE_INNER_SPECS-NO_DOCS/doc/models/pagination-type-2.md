
# Pagination Type 2

Use for pagination.

## Structure

`PaginationType2`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `page_number` | `int` | Optional | This is the page number that you would like to retrieve<br>Default is page number 01.<br><br>**Default**: `1`<br><br>**Constraints**: `>= 0`, `<= 10000000000000000` |
| `page_size` | `int` | Optional | Number of record that you would want to retrieve per page<br>Default is 25 items per page.<br><br>**Default**: `25`<br><br>**Constraints**: `>= 0`, `<= 10000000000000000` |

## Example (as JSON)

```json
{
  "pageNumber": 2,
  "pageSize": 10
}
```

