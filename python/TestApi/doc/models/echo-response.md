
# Echo Response

Raw http Request info

## Structure

`EchoResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | `Dict[str, Any]` | Optional | - |
| `headers` | `Dict[str, str]` | Optional | - |
| `method` | `str` | Optional | - |
| `path` | `str` | Optional | relativePath |
| `query` | [`Dict[str, QueryParameter]`](../../doc/models/query-parameter.md) | Optional | - |
| `upload_count` | `int` | Optional | - |

## Example (as JSON)

```json
{
  "body": {
    "key0": {
      "key1": "val1",
      "key2": "val2"
    },
    "key1": {
      "key1": "val1",
      "key2": "val2"
    }
  },
  "headers": {
    "key0": "headers3",
    "key1": "headers4"
  },
  "method": "method6",
  "path": "path4",
  "query": {
    "key0": {
      "key": "key0"
    },
    "key1": {
      "key": "key0"
    },
    "key2": {
      "key": "key0"
    }
  }
}
```

