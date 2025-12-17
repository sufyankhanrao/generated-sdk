
# Mixed Model

This class contains mix of scalar and non scalar types in oneOf/anyOf cases.

## Structure

`MixedModel`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `any_of_required` | int \| [Orbit](../../doc/models/orbit.md) | Required | This is a container for any-of cases. |
| `one_of_req_nullable` | bool \| [Vehicle](../../doc/models/vehicle.md) \| None | Required | This is a container for one-of cases. |
| `one_of_optional` | [Car](../../doc/models/car.md) \| [Morning](../../doc/models/morning.md) \| str \| None | Optional | This is a container for one-of cases. |
| `any_of_opt_nullable` | [Postman](../../doc/models/postman.md) \| [Person](../../doc/models/person.md) \| float \| None | Optional | This is a container for any-of cases. |

## Example (as JSON)

```json
{
  "anyOfRequired": 172,
  "oneOfReqNullable": true,
  "oneOfOptional": {
    "NumberOfTyres": "NumberOfTyres4",
    "HaveTrunk": false
  },
  "anyOfOptNullable": {
    "joiningDay": "Monday",
    "personType": "Post",
    "address": "address0",
    "age": 122,
    "birthday": "2016-03-13",
    "birthtime": "2016-03-13T12:52:32.123Z",
    "name": "name4",
    "uid": "uid4",
    "department": "department6",
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
    "salary": 210,
    "workingDays": [
      "Thursday"
    ]
  }
}
```

