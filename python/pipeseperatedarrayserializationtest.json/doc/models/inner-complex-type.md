
# Inner Complex Type

## Structure

`InnerComplexType`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `string_type` | `str` | Required | - |
| `boolean_type` | `bool` | Required | - |
| `date_time_type` | `datetime` | Required | - |
| `date_type` | `date` | Required | - |
| `uuid_type` | `uuid\|str` | Required | - |
| `long_type` | `int` | Required | - |
| `precision_type` | `float` | Required | - |
| `object_type` | `Any` | Required | - |
| `string_list_type` | `List[str]` | Required | - |

## Example (as JSON)

```json
{
  "stringType": "stringType0",
  "booleanType": false,
  "dateTimeType": "2016-03-13T12:52:32.123Z",
  "dateType": "2016-03-13",
  "uuidType": "00001640-0000-0000-0000-000000000000",
  "longType": 6,
  "precisionType": 61.6,
  "objectType": {
    "key1": "val1",
    "key2": "val2"
  },
  "stringListType": [
    "stringListType0",
    "stringListType1"
  ]
}
```

