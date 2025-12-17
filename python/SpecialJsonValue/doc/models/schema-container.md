
# Schema Container

## Structure

`SchemaContainer`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `name` | `str` | Required | - |
| `id` | `str` | Required | - |
| `schema` | `dict` | Required | - |
| `schema_array` | `List[dict]` | Optional | - |
| `schema_map` | `Dict[str, dict]` | Optional | - |

## Example (as JSON)

```json
{
  "name": "a name",
  "id": "definition-123",
  "schema": {
    "key1": "val1",
    "key2": "val2"
  },
  "schemaArray": [
    {
      "key1": "val1",
      "key2": "val2"
    },
    {
      "key1": "val1",
      "key2": "val2"
    },
    {
      "key1": "val1",
      "key2": "val2"
    }
  ],
  "schemaMap": {
    "key0": {
      "key1": "val1",
      "key2": "val2"
    }
  }
}
```

