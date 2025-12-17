
# Mixed Model

This class contains mix of scalar and non scalar types in oneOf/anyOf cases.

## Structure

`MixedModel`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `multi_any_of` | [Car](../../doc/models/car.md) \| str \| [Morning](../../doc/models/morning.md) | Required | This is a container for any-of cases. |
| `multi_one_of_any_of` | [Car](../../doc/models/car.md) \| str \| [Morning](../../doc/models/morning.md) | Required | This is a container for one-of cases. |
| `single_inner_map_of_array` | Dict[str, List[int]] \| Dict[str, [Orbit](../../doc/models/orbit.md)] | Required | This is a container for any-of cases. |
| `outer_map_of_single_inner_array` | Dict[str, List[int] \| [Orbit](../../doc/models/orbit.md)] | Required | This is Dictionary of a container for any-of cases. |
| `all_inner_array_of_map` | List[Dict[str, bool]] \| List[Dict[str, [Vehicle](../../doc/models/vehicle.md)]] \| None | Required | This is a container for one-of cases. |
| `all_inner_array_of_map_2` | Dict[str, List[Dict[str, bool]] \| List[Dict[str, [Vehicle](../../doc/models/vehicle.md)]]] \| None | Required | This is Dictionary of a container for one-of cases. |
| `outer_array_of_map` | List[Dict[str, [Car](../../doc/models/car.md) \| [Morning](../../doc/models/morning.md) \| str]] \| None | Optional | This is List of Dictionary of a container for one-of cases. |
| `outer_array_of_map_2` | List[Dict[str, List[[Car](../../doc/models/car.md)] \| List[[Morning](../../doc/models/morning.md)] \| List[str]]] \| None | Optional | This is List of Dictionary of a container for one-of cases. |
| `outer_map_of_array` | Dict[str, List[[Postman](../../doc/models/postman.md) \| [Person](../../doc/models/person.md) \| float]] \| None | Optional | This is Dictionary of List of a container for any-of cases. |
| `outer_map_of_array_2` | Dict[str, List[Dict[str, [Postman](../../doc/models/postman.md)] \| Dict[str, [Person](../../doc/models/person.md)] \| Dict[str, float]]] \| None | Optional | This is Dictionary of List of a container for any-of cases. |

## Example (as JSON)

```json
{
  "multiAnyOf": {
    "NumberOfTyres": "NumberOfTyres4",
    "HaveTrunk": false
  },
  "multiOneOfAnyOf": {
    "NumberOfTyres": "NumberOfTyres4",
    "HaveTrunk": false
  },
  "singleInnerMapOfArray": {
    "key0": [
      2,
      3
    ]
  },
  "outerMapOfSingleInnerArray": {
    "key0": [
      52,
      53,
      54
    ],
    "key1": [
      53
    ]
  },
  "allInnerArrayOfMap": [
    {
      "key0": true,
      "key1": false,
      "key2": true
    },
    {
      "key0": false
    }
  ],
  "allInnerArrayOfMap2": {
    "key0": [
      {
        "key0": false,
        "key1": true
      }
    ]
  },
  "outerArrayOfMap": [
    {
      "key0": {
        "NumberOfTyres": "NumberOfTyres4",
        "HaveTrunk": false
      },
      "key1": {
        "NumberOfTyres": "NumberOfTyres4",
        "HaveTrunk": false
      }
    }
  ],
  "outerArrayOfMap2": [
    {
      "key0": [
        {
          "NumberOfTyres": "NumberOfTyres4",
          "HaveTrunk": false
        },
        {
          "NumberOfTyres": "NumberOfTyres4",
          "HaveTrunk": false
        }
      ],
      "key1": [
        {
          "NumberOfTyres": "NumberOfTyres4",
          "HaveTrunk": false
        },
        {
          "NumberOfTyres": "NumberOfTyres4",
          "HaveTrunk": false
        },
        {
          "NumberOfTyres": "NumberOfTyres4",
          "HaveTrunk": false
        }
      ]
    },
    {
      "key0": [
        {
          "NumberOfTyres": "NumberOfTyres4",
          "HaveTrunk": false
        },
        {
          "NumberOfTyres": "NumberOfTyres4",
          "HaveTrunk": false
        },
        {
          "NumberOfTyres": "NumberOfTyres4",
          "HaveTrunk": false
        }
      ],
      "key1": [
        {
          "NumberOfTyres": "NumberOfTyres4",
          "HaveTrunk": false
        }
      ],
      "key2": [
        {
          "NumberOfTyres": "NumberOfTyres4",
          "HaveTrunk": false
        },
        {
          "NumberOfTyres": "NumberOfTyres4",
          "HaveTrunk": false
        }
      ]
    }
  ],
  "outerMapOfArray": {
    "key0": [
      {
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
      {
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
    ],
    "key1": [
      {
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
      {
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
      {
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
    ],
    "key2": [
      {
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
    ]
  },
  "outerMapOfArray2": {
    "key0": [
      {
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
        },
        "key2": {
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
      },
      {
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
        }
      }
    ]
  }
}
```

