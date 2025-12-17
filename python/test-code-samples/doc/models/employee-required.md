
# Employee Required

## Structure

`EmployeeRequired`

## Inherits From

[`Person`](../../doc/models/person.md)

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `department` | `str` | Required | - |
| `boolean_var` | `bool` | Required | - |
| `object_var` | `Any` | Required | - |
| `dynamic_var` | `Any` | Required | - |
| `date_time_unix_var` | `datetime` | Required | - |
| `r_fc_1123_var` | `datetime` | Required | - |
| `r_fc_3339_var` | `datetime` | Required | - |
| `date_var` | `date` | Required | - |
| `dependents` | [`List[Person]`](../../doc/models/person.md) | Required | - |
| `hired_at` | `datetime` | Required | - |
| `joining_day` | [`Days`](../../doc/models/days.md) | Required | **Default**: `'Monday'` |
| `salary` | `int` | Required | - |
| `boss` | [`Person`](../../doc/models/person.md) | Required | - |

## Example (as JSON)

```json
{
  "department": "department4",
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
  "rFC1123Var": "Mon, 15 Jun 2009 20:45:30 GMT",
  "rFC3339Var": "2016-03-13T12:52:32.123Z",
  "dateVar": "2016-03-13",
  "hiredAt": "Mon, 15 Jun 2009 20:45:30 GMT",
  "joiningDay": "Monday",
  "salary": 112,
  "personType": "Empl",
  "address": "address0",
  "age": 122,
  "birthday": "2016-03-13",
  "birthtime": "2016-03-13T12:52:32.123Z",
  "name": "name4",
  "uid": "uid4",
  "dependents": [
    {
      "personType": "Per",
      "address": "address4",
      "age": 28,
      "birthday": "2016-03-13",
      "birthtime": "2016-03-13T12:52:32.123Z",
      "name": "name8",
      "uid": "uid8"
    },
    {
      "personType": "Per",
      "address": "address4",
      "age": 28,
      "birthday": "2016-03-13",
      "birthtime": "2016-03-13T12:52:32.123Z",
      "name": "name8",
      "uid": "uid8"
    },
    {
      "personType": "Per",
      "address": "address4",
      "age": 28,
      "birthday": "2016-03-13",
      "birthtime": "2016-03-13T12:52:32.123Z",
      "name": "name8",
      "uid": "uid8"
    }
  ],
  "boss": {
    "personType": "Per",
    "address": "address8",
    "age": 94,
    "birthday": "2016-03-13",
    "birthtime": "2016-03-13T12:52:32.123Z",
    "name": "name2",
    "uid": "uid2"
  }
}
```

