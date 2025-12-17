
# Server Response

## Structure

`ServerResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `passed` | `bool` | Required | - |
| `message` | `str` | Optional | - |
| `input` | `Dict[str, dict]` | Optional | - |
| `nullable_number_map` | `Dict[str, float]` | Optional | - |
| `nullable_number_array` | `List[float]` | Optional | - |

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
  },
  "nullableNumberMap": {
    "key0": 117.45,
    "key1": 117.46
  },
  "nullableNumberArray": [
    216.38,
    216.39,
    216.4
  ]
}
```

