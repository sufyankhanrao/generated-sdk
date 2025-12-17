
# Entity Chain 1

Supports entities such as SalesOrganization and SalesChannel limit 1 Entity<br>National and SuperChain with maximum limit of 10 entities<br>Chain with maximum limit of 2000 entities.

## Structure

`EntityChain1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `level` | [`Level2Enum`](../../doc/models/level-2-enum.md) | Optional | Refers to hierarchy level |
| `values` | `List[str]` | Optional | Refers to hierarchy id. Accept list of ids.<br><br>**Constraints**: *Maximum Length*: `2000` |

## Example (as JSON)

```json
{
  "level": "CHAIN",
  "values": [
    "0B2345",
    "AB1234"
  ]
}
```

