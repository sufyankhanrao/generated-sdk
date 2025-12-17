
# Complex Type

## Structure

`ComplexType`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `number_list_type` | `List[int]` | Required | - |
| `number_map_type` | `Dict[str, int]` | Required | - |
| `inner_complex_type` | [`InnerComplexType`](../../doc/models/inner-complex-type.md) | Required | - |
| `inner_complex_list_type` | [`List[InnerComplexType]`](../../doc/models/inner-complex-type.md) | Required | - |

## Example (as JSON)

```json
{
  "numberListType": [
    166
  ],
  "numberMapType": {
    "key0": 35,
    "key1": 36,
    "key2": 37
  },
  "innerComplexType": {
    "stringType": "stringType8",
    "booleanType": false,
    "dateTimeType": "2016-03-13T12:52:32.123Z",
    "dateType": "2016-03-13",
    "uuidType": "00001742-0000-0000-0000-000000000000",
    "longType": 40,
    "precisionType": 8.18,
    "objectType": {
      "key1": "val1",
      "key2": "val2"
    },
    "stringListType": [
      "stringListType8"
    ]
  },
  "innerComplexListType": [
    {
      "stringType": "stringType0",
      "booleanType": false,
      "dateTimeType": "2016-03-13T12:52:32.123Z",
      "dateType": "2016-03-13",
      "uuidType": "00001992-0000-0000-0000-000000000000",
      "longType": 88,
      "precisionType": 70.1,
      "objectType": {
        "key1": "val1",
        "key2": "val2"
      },
      "stringListType": [
        "stringListType0",
        "stringListType1",
        "stringListType2"
      ]
    }
  ]
}
```

