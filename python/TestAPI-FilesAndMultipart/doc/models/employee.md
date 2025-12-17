
# Employee

## Structure

`Employee`

## Inherits From

[`Person`](../../doc/models/person.md)

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `department` | `str` | Required | - |
| `dependents` | [`List[Person]`](../../doc/models/person.md) | Required | - |
| `hired_at` | `datetime` | Required | - |
| `joining_day` | [`Days`](../../doc/models/days.md) | Required | **Default**: `"Monday"` |
| `salary` | `int` | Required | - |
| `working_days` | [`List[Days]`](../../doc/models/days.md) | Required | - |
| `boss` | [`Person`](../../doc/models/person.md) | Required | - |

## Example (as JSON)

```json
{
  "department": "department4",
  "dependents": [
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
  "hiredAt": "Mon, 15 Jun 2009 20:45:30 GMT",
  "joiningDay": "Monday",
  "salary": 160,
  "workingDays": [
    "Friday"
  ],
  "boss": {
    "personType": "Per",
    "address": "address8",
    "age": 94,
    "birthday": "2016-03-13",
    "birthtime": "2016-03-13T12:52:32.123Z",
    "name": "name2",
    "uid": "uid2"
  },
  "personType": "Empl",
  "address": "address0",
  "age": 122,
  "birthday": "2016-03-13",
  "birthtime": "2016-03-13T12:52:32.123Z",
  "name": "name4",
  "uid": "uid4"
}
```

