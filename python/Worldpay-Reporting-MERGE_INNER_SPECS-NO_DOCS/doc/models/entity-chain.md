
# Entity Chain

Supports entities IndependentSalesOrganization, IndependentSalesChannel, National, Chain.

## Structure

`EntityChain`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `level` | [`Level2Enum`](../../doc/models/level-2-enum.md) | Optional | Refers to hierarchy level |
| `values` | `List[str]` | Optional | Refers to hierarchy id. Accept list of ids.<br><br>**Constraints**: *Maximum Length*: `255` |

## Example (as JSON)

```json
{
  "level": "CHAIN",
  "values": [
    "1X0010",
    "BA0234"
  ]
}
```

