
# Value Container

## Structure

`ValueContainer`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `name` | `str` | Required | - |
| `id` | `str` | Required | - |
| `value` | `Any` | Required | - |
| `value_array` | `List[Any]` | Optional | - |
| `value_map` | `Dict[str, Any]` | Optional | - |

## Example (as JSON)

```json
{
  "name": "a name",
  "id": "definition-123",
  "value": {
    "key1": "val1",
    "key2": "val2"
  },
  "valueArray": [
    {
      "key1": "val1",
      "key2": "val2"
    },
    {
      "key1": "val1",
      "key2": "val2"
    }
  ],
  "valueMap": {
    "key0": {
      "key1": "val1",
      "key2": "val2"
    }
  }
}
```

