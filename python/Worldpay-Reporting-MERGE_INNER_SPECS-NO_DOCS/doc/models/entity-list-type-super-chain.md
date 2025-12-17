
# Entity List Type Super Chain

Supports entities such as SalesOrganization and SalesChannel with maximum limit of 1 entity<br>National and SuperChain with maximum limit of 10 entities.

## Structure

`EntityListTypeSuperChain`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `level` | [`Level4Enum`](../../doc/models/level-4-enum.md) | Optional | Refers to hierarchy level |
| `values` | `List[str]` | Optional | Refers to hierarchy id. Accept list of ids.<br><br>**Constraints**: *Maximum Length*: `2000` |

## Example (as JSON)

```json
{
  "level": "SUPERCHAIN",
  "values": [
    "733123456",
    "845212345"
  ]
}
```

