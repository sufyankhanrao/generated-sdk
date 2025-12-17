
# Boss

Testing circular reference.

## Structure

`Boss`

## Inherits From

[`EmployeeRequired`](../../doc/models/employee-required.md)

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `promoted_at` | `datetime` | Required | - |
| `assistant` | [`EmployeeRequired`](../../doc/models/employee-required.md) | Required | - |

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
  "promotedAt": 1480809600,
  "assistant": {
    "joiningDay": "Monday",
    "personType": "Empl",
    "address": "address0",
    "age": 122,
    "birthday": "2016-03-13",
    "birthtime": "2016-03-13T12:52:32.123Z",
    "name": "name4",
    "uid": "uid4",
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
    "hiredAt": "Mon, 15 Jun 2009 20:45:30 GMT",
    "salary": 198,
    "boss": {
      "personType": "Per",
      "address": "address8",
      "age": 94,
      "birthday": "2016-03-13",
      "birthtime": "2016-03-13T12:52:32.123Z",
      "name": "name2",
      "uid": "uid2"
    }
  },
  "personType": "Boss",
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

