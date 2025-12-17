
# Non Scalar Model

This class contains non scalar types in oneOf/anyOf cases.

## Structure

`NonScalarModel`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `multi_any_of` | [Car](../../doc/models/car.md) \| [Atom](../../doc/models/atom.md) \| [Morning](../../doc/models/morning.md) | Required | This is a container for any-of cases. |
| `multi_one_of_any_of` | [Car](../../doc/models/car.md) \| [Atom](../../doc/models/atom.md) \| [Morning](../../doc/models/morning.md) | Required | This is a container for one-of cases. |
| `single_inner_map_of_array` | Dict[str, List[[Atom](../../doc/models/atom.md)]] \| Dict[str, [Atom](../../doc/models/atom.md)] | Required | This is a container for any-of cases. |
| `outer_map_of_single_inner_array` | Dict[str, List[[Atom](../../doc/models/atom.md)] \| [Atom](../../doc/models/atom.md)] | Required | This is Dictionary of a container for any-of cases. |
| `all_inner_array_of_map` | List[Dict[str, [Orbit](../../doc/models/orbit.md)]] \| List[Dict[str, [Vehicle](../../doc/models/vehicle.md)]] \| None | Required | This is a container for one-of cases. |
| `all_inner_array_of_map_2` | Dict[str, List[Dict[str, [Orbit](../../doc/models/orbit.md)]] \| List[Dict[str, [Vehicle](../../doc/models/vehicle.md)]]] \| None | Required | This is Dictionary of a container for one-of cases. |
| `outer_array_of_map` | List[Dict[str, [Car](../../doc/models/car.md) \| [Morning](../../doc/models/morning.md) \| [Atom](../../doc/models/atom.md)]] \| None | Optional | This is List of Dictionary of a container for one-of cases. |
| `outer_array_of_map_2` | List[Dict[str, List[[Car](../../doc/models/car.md)] \| List[[Morning](../../doc/models/morning.md)] \| List[[Atom](../../doc/models/atom.md)]]] \| None | Optional | This is List of Dictionary of a container for one-of cases. |
| `outer_map_of_array` | Dict[str, List[[Morning](../../doc/models/morning.md) \| [Evening](../../doc/models/evening.md) \| [Noon](../../doc/models/noon.md)]] \| None | Optional | This is Dictionary of List of a container for any-of cases. |
| `outer_map_of_array_2` | Dict[str, List[Dict[str, [Morning](../../doc/models/morning.md)] \| Dict[str, [Evening](../../doc/models/evening.md)] \| Dict[str, [Noon](../../doc/models/noon.md)]]] \| None | Optional | This is Dictionary of List of a container for any-of cases. |

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
      {
        "NumberOfElectrons": 224,
        "NumberOfProtons": 134
      },
      {
        "NumberOfElectrons": 224,
        "NumberOfProtons": 134
      }
    ]
  },
  "outerMapOfSingleInnerArray": {
    "key0": [
      {
        "NumberOfElectrons": 224,
        "NumberOfProtons": 134
      },
      {
        "NumberOfElectrons": 224,
        "NumberOfProtons": 134
      }
    ]
  },
  "allInnerArrayOfMap": [
    {
      "key0": {
        "NumberOfElectrons": 218
      },
      "key1": {
        "NumberOfElectrons": 218
      },
      "key2": {
        "NumberOfElectrons": 218
      }
    },
    {
      "key0": {
        "NumberOfElectrons": 218
      }
    },
    {
      "key0": {
        "NumberOfElectrons": 218
      },
      "key1": {
        "NumberOfElectrons": 218
      }
    }
  ],
  "allInnerArrayOfMap2": {
    "key0": [
      {
        "key0": {
          "NumberOfElectrons": 218
        },
        "key1": {
          "NumberOfElectrons": 218
        }
      },
      {
        "key0": {
          "NumberOfElectrons": 218
        }
      },
      {
        "key0": {
          "NumberOfElectrons": 218
        },
        "key1": {
          "NumberOfElectrons": 218
        },
        "key2": {
          "NumberOfElectrons": 218
        }
      }
    ],
    "key1": [
      {
        "key0": {
          "NumberOfElectrons": 218
        }
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
    },
    {
      "key0": {
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
        }
      ]
    }
  ],
  "outerMapOfArray": {
    "key0": [
      {
        "sessionType": "Morning",
        "startsAt": "startsAt6",
        "endsAt": "endsAt2",
        "offerTeaBreak": false
      }
    ],
    "key1": [
      {
        "sessionType": "Morning",
        "startsAt": "startsAt6",
        "endsAt": "endsAt2",
        "offerTeaBreak": false
      },
      {
        "sessionType": "Morning",
        "startsAt": "startsAt6",
        "endsAt": "endsAt2",
        "offerTeaBreak": false
      }
    ]
  },
  "outerMapOfArray2": {
    "key0": [
      {
        "key0": {
          "sessionType": "Morning",
          "startsAt": "startsAt6",
          "endsAt": "endsAt2",
          "offerTeaBreak": false
        },
        "key1": {
          "sessionType": "Morning",
          "startsAt": "startsAt6",
          "endsAt": "endsAt2",
          "offerTeaBreak": false
        },
        "key2": {
          "sessionType": "Morning",
          "startsAt": "startsAt6",
          "endsAt": "endsAt2",
          "offerTeaBreak": false
        }
      }
    ],
    "key1": [
      {
        "key0": {
          "sessionType": "Morning",
          "startsAt": "startsAt6",
          "endsAt": "endsAt2",
          "offerTeaBreak": false
        }
      },
      {
        "key0": {
          "sessionType": "Morning",
          "startsAt": "startsAt6",
          "endsAt": "endsAt2",
          "offerTeaBreak": false
        },
        "key1": {
          "sessionType": "Morning",
          "startsAt": "startsAt6",
          "endsAt": "endsAt2",
          "offerTeaBreak": false
        }
      }
    ],
    "key2": [
      {
        "key0": {
          "sessionType": "Morning",
          "startsAt": "startsAt6",
          "endsAt": "endsAt2",
          "offerTeaBreak": false
        },
        "key1": {
          "sessionType": "Morning",
          "startsAt": "startsAt6",
          "endsAt": "endsAt2",
          "offerTeaBreak": false
        }
      },
      {
        "key0": {
          "sessionType": "Morning",
          "startsAt": "startsAt6",
          "endsAt": "endsAt2",
          "offerTeaBreak": false
        },
        "key1": {
          "sessionType": "Morning",
          "startsAt": "startsAt6",
          "endsAt": "endsAt2",
          "offerTeaBreak": false
        },
        "key2": {
          "sessionType": "Morning",
          "startsAt": "startsAt6",
          "endsAt": "endsAt2",
          "offerTeaBreak": false
        }
      },
      {
        "key0": {
          "sessionType": "Morning",
          "startsAt": "startsAt6",
          "endsAt": "endsAt2",
          "offerTeaBreak": false
        }
      }
    ]
  }
}
```

