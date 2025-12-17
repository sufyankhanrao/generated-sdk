
# Problem Details Exception

An object describing the problem with the request, following the [RFC 7807](https://tools.ietf.org/html/rfc7807) format.

## Structure

`ProblemDetailsException`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `status` | `int` | Required | - |
| `title` | `str` | Required | - |

## Example (as JSON)

```json
{
  "status": 132,
  "title": "title4"
}
```

