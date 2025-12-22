
# Employee Optional

## Structure

`EmployeeOptional`

## Inherits From

[`Person`](../../doc/models/person.md)

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `department` | `str` | Optional | - |
| `boolean_var` | `bool` | Optional | - |
| `object_var` | `Any` | Optional | - |
| `dynamic_var` | `Any` | Optional | - |
| `date_time_unix_var` | `datetime` | Optional | - |
| `r_fc_1123_var` | `datetime` | Optional | - |
| `r_fc_3339_var` | `datetime` | Optional | - |
| `date_var` | `date` | Optional | - |
| `dependents` | [`List[Person]`](../../doc/models/person.md) | Optional | - |
| `hired_at` | `datetime` | Optional | - |
| `joining_day` | [`Days`](../../doc/models/days.md) | Optional | **Default**: `"Monday"` |
| `salary` | `int` | Optional | - |
| `boss` | [`Person`](../../doc/models/person.md) | Optional | - |

## Example (as JSON)

```json
{
  "department": "department2",
  "booleanVar": false,
  "objectVar": {
    "key1": "val1",
    "key2": "val2"
  },
  "dynamicVar": {
    "key1": "val1",
    "key2": "val2"
  },
  "dateTimeUnixVar": 1480809600,
  "rFC1123Var": null,
  "rFC3339Var": null,
  "dateVar": null,
  "hiredAt": null,
  "joiningDay": "Monday",
  "salary": null,
  "personType": "Empl",
  "address": "address0",
  "age": 122,
  "birthday": "2016-03-13",
  "birthtime": "2016-03-13T12:52:32.123Z",
  "name": "name4",
  "uid": "uid4"
}
```

