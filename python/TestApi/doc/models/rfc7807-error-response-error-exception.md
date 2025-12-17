
# RFC7807 Error Response Error Exception

A description of the error. This value will conform to a RFC 7807 http problem.

## Structure

`RFC7807ErrorResponseErrorException`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `title` | `str` | Optional | A high level description of the problem. This description will not be specific to this instance of the prbolem. |
| `detail` | `str` | Optional | A specific description of the problem and why it occurred. |

## Example (as JSON)

```json
{
  "title": "title0",
  "detail": "detail0"
}
```

