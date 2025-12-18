
# Response Async Processing

## Structure

`ResponseAsyncProcessing`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `mtype` | [`Type5Enum`](../../doc/models/type-5-enum.md) | Optional | Resource Type<br><br>**Default**: `'AsyncProcessing'` |
| `data` | [`Data1`](../../doc/models/data-1.md) | Optional | - |

## Example (as JSON)

```json
{
  "type": "AsyncProcessing",
  "data": {
    "async": {
      "code": "00000038-0000-0000-0000-000000000000",
      "link": "link8"
    }
  }
}
```

