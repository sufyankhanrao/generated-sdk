
# Non Scalar Model

This class contains non scalar types in oneOf/anyOf cases.

## Structure

`NonScalarModel`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `any_of_required` | [Atom](../../doc/models/atom.md) \| [Orbit](../../doc/models/orbit.md) | Required | This is a container for any-of cases. |
| `one_of_req_nullable` | [Orbit](../../doc/models/orbit.md) \| [Vehicle](../../doc/models/vehicle.md) \| None | Required | This is a container for one-of cases. |
| `one_of_optional` | [Car](../../doc/models/car.md) \| [Morning](../../doc/models/morning.md) \| [Atom](../../doc/models/atom.md) \| None | Optional | This is a container for one-of cases. |
| `any_of_opt_nullable` | [Morning](../../doc/models/morning.md) \| [Evening](../../doc/models/evening.md) \| [Noon](../../doc/models/noon.md) \| None | Optional | This is a container for any-of cases. |

## Example (as JSON)

```json
{
  "anyOfRequired": {
    "NumberOfElectrons": 224,
    "NumberOfProtons": 134
  },
  "oneOfReqNullable": {
    "NumberOfElectrons": 218
  },
  "oneOfOptional": {
    "NumberOfTyres": "NumberOfTyres4",
    "HaveTrunk": false
  },
  "anyOfOptNullable": {
    "sessionType": "Morning",
    "startsAt": "startsAt6",
    "endsAt": "endsAt2",
    "offerTeaBreak": false
  }
}
```

