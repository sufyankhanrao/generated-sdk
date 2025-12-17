
# Non Scalar Model

This class contains non scalar types in oneOf/anyOf cases.

## Structure

`NonScalarModel`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `single_inner_map` | Dict[str, [Atom](../../doc/models/atom.md)] \| [Orbit](../../doc/models/orbit.md) | Required | This is a container for any-of cases. |
| `all_inner_array` | List[[Orbit](../../doc/models/orbit.md)] \| List[[Vehicle](../../doc/models/vehicle.md)] \| None | Required | This is a container for one-of cases. |
| `outer_array` | List[[Car](../../doc/models/car.md) \| [Morning](../../doc/models/morning.md) \| [Atom](../../doc/models/atom.md)] \| None | Optional | This is List of a container for one-of cases. |
| `outer_map` | Dict[str, [Morning](../../doc/models/morning.md) \| [Evening](../../doc/models/evening.md) \| [Noon](../../doc/models/noon.md)] \| None | Optional | This is Dictionary of a container for any-of cases. |
| `inner_collection_with_nullable` | [Atom](../../doc/models/atom.md) \| None \| List[[Atom](../../doc/models/atom.md)] \| Dict[str, [Atom](../../doc/models/atom.md)] | Optional | This is a container for any-of cases. |

## Example (as JSON)

```json
{
  "singleInnerMap": {
    "key0": {
      "NumberOfElectrons": 224,
      "NumberOfProtons": 134
    },
    "key1": {
      "NumberOfElectrons": 224,
      "NumberOfProtons": 134
    }
  },
  "allInnerArray": [
    {
      "NumberOfElectrons": 218
    }
  ],
  "outerArray": [
    {
      "NumberOfTyres": "NumberOfTyres4",
      "HaveTrunk": false
    }
  ],
  "outerMap": {
    "key0": {
      "sessionType": "Morning",
      "startsAt": "startsAt6",
      "endsAt": "endsAt2",
      "offerTeaBreak": false
    }
  },
  "innerCollectionWithNullable": {
    "NumberOfElectrons": 224,
    "NumberOfProtons": 134
  }
}
```

