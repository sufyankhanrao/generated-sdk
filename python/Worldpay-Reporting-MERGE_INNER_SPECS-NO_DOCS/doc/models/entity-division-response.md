
# Entity Division Response

Supports entities chain and national.

## Structure

`EntityDivisionResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `chain_code` | `str` | Optional | The Chain Code is the level of the merchant hierarchy that groups merchant identifiers (MIDs) and any related roll-up values under a common identifier for settlement, billing and reporting. Chain Code is the primary identifier for merchants boarded in MDB (Merchant Database) system.<br><br>**Constraints**: *Maximum Length*: `6` |
| `division_number` | `str` | Optional | The Division Number is a hierarchy level that enables merchants to roll-up child entities for Stores / Locations into different groups under a Chain. The Division Code is an optional hierarchy level but if created, is required for all child entities under the Division Number. <br> Supports entities Chain, National.<br><br>**Constraints**: *Maximum Length*: `3` |

## Example (as JSON)

```json
{
  "chainCode": "1X0010",
  "divisionNumber": "088"
}
```

