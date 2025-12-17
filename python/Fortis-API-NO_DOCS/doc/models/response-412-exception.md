
# Response 412 Exception

## Structure

`Response412Exception`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `mtype` | `str` | Optional | - |
| `id` | `str` | Optional | - |
| `status_code` | `int` | Optional | Response code |
| `title` | `str` | Optional | Error description |
| `detail` | `str` | Optional | Error details |
| `meta` | [`Meta`](../../doc/models/meta.md) | Optional | - |

## Example (as JSON)

```json
{
  "type": "clj4ge1234004t9ptdoz34567",
  "id": "clj4ge1234004t9ptdoz34567",
  "statusCode": 412,
  "title": "Precondition Failed",
  "detail": "\"fieldName\" is required"
}
```

