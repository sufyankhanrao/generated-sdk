
# Data

## Structure

`Data`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `code` | `uuid\|str` | Optional | A [UUID v4](https://datatracker.ietf.org/doc/html/rfc4122) that's unique for the Async Request |
| `mtype` | `str` | Optional | The @type from the original request. |
| `id` | `str` | Optional | After a sucessfully processing, the system will fill with the final ID for the document |
| `progress` | `int` | Optional | The current percentage progress<br><br>**Constraints**: `>= 0`, `<= 100` |
| `error` | `str` | Optional | In case of error processing, it will contain the error details |
| `ttl` | `int` | Optional | The date (in [Epoch Time](https://en.wikipedia.org/wiki/Unix_time)) this status register is set to expire. Usually 30 days after the request. |

## Example (as JSON)

```json
{
  "code": "406c66c3-21cb-47fb-80fc-843bc42507fb",
  "type": "Transaction",
  "id": "11e95f8ec39de8fbdb0a4f1a",
  "progress": 100,
  "ttl": 7956886942,
  "error": "error8"
}
```

