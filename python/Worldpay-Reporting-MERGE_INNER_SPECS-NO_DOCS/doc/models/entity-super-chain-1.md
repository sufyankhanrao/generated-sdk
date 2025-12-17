
# Entity Super Chain 1

Supports entities independent sales organization, independent sales channel, national and super chain.

## Structure

`EntitySuperChain1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `level` | [`Level4Enum`](../../doc/models/level-4-enum.md) | Optional | Level of merchant hierarchy |
| `values` | `List[str]` | Optional | Id of level<br><br>**Constraints**: *Maximum Length*: `20` |

## Example (as JSON)

```json
{
  "level": "SUPERCHAIN",
  "values": [
    "733123456",
    "845123456"
  ]
}
```

