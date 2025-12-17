
# Entity 2

The hierarchy is required. It supports entities such as:<br> IndependentSalesOrganization/IndependentSalesChannel (limit 1 Entity).<br> National, SuperChain, Partner (maximum limit of 10 entities).<br> Chain, Division, Store and Merchant (maximum limit of 2,000 entities).

## Structure

`Entity2`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `level` | [`Level1Enum`](../../doc/models/level-1-enum.md) | Optional | hierarchy level<br><br>**Constraints**: *Maximum Length*: `30` |
| `values` | `List[str]` | Optional | example values of Entity<br><br>**Constraints**: *Minimum Length*: `0`, *Maximum Length*: `256` |
| `chain_code` | `str` | Optional | Chain Code is mandatory to pass when merchant hierarchy level is store or division.<br><br>**Constraints**: *Minimum Length*: `0`, *Maximum Length*: `256` |

## Example (as JSON)

```json
{
  "level": "MERCHANT",
  "values": [
    "4445000860700",
    "4445000860702"
  ],
  "chainCode": "OA1234"
}
```

