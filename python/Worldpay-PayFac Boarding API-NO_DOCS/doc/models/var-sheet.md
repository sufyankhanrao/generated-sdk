
# Var Sheet

## Structure

`VarSheet`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Optional | Terminal ID associated with the VAR sheet |
| `tid` | `str` | Optional | TID associated with the VAR sheet |
| `date_created` | `str` | Optional | The date the VAR Sheet was created |
| `date_last_modified` | `str` | Optional | The date the VAR Sheet was last modified |
| `content` | `str` | Optional | A base 64 encoded byte string of the VAR Sheet pdf |

## Example (as JSON)

```json
{
  "id": "12345",
  "tid": "1",
  "dateCreated": "01/28/2019 00:00:00",
  "dateLastModified": "01/28/2019 00:00:00",
  "content": "content8"
}
```

