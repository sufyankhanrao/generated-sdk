
# Detail

## Structure

`Detail`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `message` | `str` | Optional | - |
| `path` | `List[str]` | Optional | - |
| `mtype` | `str` | Optional | - |
| `context` | [`Context`](../../doc/models/context.md) | Optional | - |

## Example (as JSON)

```json
{
  "message": "\"fieldName\" is required",
  "type": "any.required",
  "path": [
    "path8",
    "path9"
  ],
  "context": {
    "key": "key2",
    "label": "label2"
  }
}
```

