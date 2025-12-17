
# Pagination Type

## Structure

`PaginationType`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `page_number` | `float` | Optional | This is the page number that you would like to retrieve.<br> Default is page number 0<br><br>**Default**: `0` |
| `page_size` | `float` | Optional | Number of record that you would want to retrieve per page. <br> Default is 25 times per page.<br><br>**Default**: `25` |

## Example (as JSON)

```json
{
  "pageNumber": 2.0,
  "pageSize": 10.0
}
```

