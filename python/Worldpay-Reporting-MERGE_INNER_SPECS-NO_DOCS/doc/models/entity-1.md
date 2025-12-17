
# Entity 1

## Structure

`Entity1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `level` | [`Level1Enum`](../../doc/models/level-1-enum.md) | Optional | Supports entities such as Independent Sales Organization/Independent Sales Channel limit 1 Entity<br>National, SuperChain, Partner with maximum limit of 10 entities<br>Chain, Division, Store and Merchant with maximum limit of 2000 entities. |
| `values` | `List[str]` | Optional | Refers to hierarchy id. Accept list of ids.<br><br>**Constraints**: *Maximum Length*: `255` |
| `chain_code` | `str` | Optional | The Chain Code is the level of the merchant hierarchy that groups merchant identifiers (MIDs) and any related roll-up values under a common identifier for settlement, billing and reporting. Chain Code is the primary identifier for merchants boarded in MDB (Merchant Database) system. <br> Chain code is mandatory to pass when hierarchy level is selected as store/division.<br><br>**Constraints**: *Maximum Length*: `6` |

## Example (as JSON)

```json
{
  "level": "MERCHANT",
  "values": [
    "4445000123456",
    "4445000234567"
  ],
  "chainCode": "1X0010"
}
```

