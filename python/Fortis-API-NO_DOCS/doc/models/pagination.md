
# Pagination

Pagination info

## Structure

`Pagination`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `mtype` | [`Type3Enum`](../../doc/models/type-3-enum.md) | Optional | Object type |
| `total_count` | `int` | Optional | Total records count |
| `page_count` | `int` | Optional | Total page count |
| `page_number` | `int` | Optional | Current page |
| `page_size` | `int` | Optional | Page size |

## Example (as JSON)

```json
{
  "type": "Pagination",
  "total_count": 423,
  "page_count": 42,
  "page_number": 6,
  "page_size": 10
}
```

