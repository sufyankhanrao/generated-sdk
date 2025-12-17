
# Entity Super Chain

Supports entities Independent Sales Oragnization, Independent Sales Channel, Super Chain.

## Structure

`EntitySuperChain`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `level` | [`Level4Enum`](../../doc/models/level-4-enum.md) | Optional | Refers to hierarchy level |
| `values` | `List[str]` | Optional | Refers to hierarchy id. Accept list of ids.<br><br>**Constraints**: *Maximum Length*: `255` |

## Example (as JSON)

```json
{
  "level": "SUPERCHAIN",
  "values": [
    "731234567",
    "841234567"
  ]
}
```

