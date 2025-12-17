
# Server Response

## Structure

`ServerResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `passed` | `bool` | Required | - |
| `message` | `str` | Optional | - |
| `input` | `Dict[str, Any]` | Optional | - |

## Example (as JSON)

```json
{
  "passed": false,
  "Message": "Message6",
  "input": {
    "key0": {
      "key1": "val1",
      "key2": "val2"
    }
  }
}
```

