
# Entity

Entity details.

## Structure

`Entity`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `level` | [`LevelEnum`](../../doc/models/level-enum.md) | Optional | Support levels such as SalesOrganization/Sales Channel (limit 1 value).<br> National, SuperChain, Partner (maximum limit of 10 values).<br> Chain, Division, Store and Merchant (maximum limit of 2,000 values).<br><br>**Constraints**: *Maximum Length*: `30` |
| `values` | `List[str]` | Optional | Values of hierarchy levels<br><br>**Constraints**: *Maximum Length*: `30` |
| `chain_code` | `str` | Optional | The Chain Code is the level of the merchant hierarchy that groups merchant identifiers (MIDs) and any related roll-up values under a common identifier for settlement, billing and reporting. Chain Code is the primary identifier for merchants boarded in MDB (Merchant Database) system. <br> Chain Code is mandatory to pass when level is store or division.<br><br>**Constraints**: *Maximum Length*: `6` |

## Example (as JSON)

```json
{
  "level": "INDEPENDENT_SALES_ORGANIZATION",
  "values": [
    "4445000860700",
    "4445000860702"
  ],
  "chainCode": "OA1234"
}
```

