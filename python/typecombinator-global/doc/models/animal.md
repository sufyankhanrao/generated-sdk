
# Animal

## Structure

`Animal`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `pet_type` | `str` | Optional | - |
| `id` | str \| int \| None | Optional | AnyOf with primitive types and metadata. |
| `friend` | [Lion](../../doc/models/lion.md) \| [Deer](../../doc/models/deer.md) \| None | Optional | OneOf (Lion, Deer) with "type" discriminator of mapping (hunter:Lion, Hunted:Deer) |
| `enemy` | [Lion](../../doc/models/lion.md) \| [Squirrel](../../doc/models/squirrel.md) \| None | Optional | OneOf (Lion, Squirrel) with an additional "kind" property discriminator of mapping (northener:Lion, westener:Squirrel) |
| `kind` | `str` | Optional | - |

## Example (as JSON)

```json
{
  "pet_type": "Animal",
  "id": 2,
  "friend": {
    "name": "deer22",
    "weight": "20 kg",
    "type": "Hunted"
  },
  "enemy": {
    "id": "23",
    "weight": "100 kg",
    "type": "hunter",
    "kind": "northener"
  },
  "kind": null
}
```

