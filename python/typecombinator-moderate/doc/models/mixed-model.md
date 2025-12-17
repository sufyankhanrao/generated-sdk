
# Mixed Model

This class contains mix of scalar and non scalar types in oneOf/anyOf cases.

## Structure

`MixedModel`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `single_inner_map` | Dict[str, int] \| [Orbit](../../doc/models/orbit.md) | Required | This is a container for any-of cases. |
| `all_inner_array` | List[bool] \| List[[Vehicle](../../doc/models/vehicle.md)] \| None | Required | This is a container for one-of cases. |
| `outer_array` | List[[Car](../../doc/models/car.md) \| [Morning](../../doc/models/morning.md) \| str] \| None | Optional | This is List of a container for one-of cases. |
| `outer_map` | Dict[str, [Postman](../../doc/models/postman.md) \| [Person](../../doc/models/person.md) \| float] \| None | Optional | This is Dictionary of a container for any-of cases. |

## Example (as JSON)

```json
{
  "singleInnerMap": {
    "key0": 30,
    "key1": 31,
    "key2": 32
  },
  "allInnerArray": [
    false,
    true,
    false
  ],
  "outerArray": [
    {
      "NumberOfTyres": "NumberOfTyres4",
      "HaveTrunk": false
    },
    {
      "NumberOfTyres": "NumberOfTyres4",
      "HaveTrunk": false
    }
  ],
  "outerMap": {
    "key0": {
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
      "joiningDay": "Wednesday",
      "salary": 210,
      "workingDays": [
        "Thursday"
      ]
    },
    "key1": {
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
      "joiningDay": "Wednesday",
      "salary": 210,
      "workingDays": [
        "Thursday"
      ]
    }
  }
}
```

