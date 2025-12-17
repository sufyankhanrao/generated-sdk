
# Entity Parent Type Division

Supports entities Chain, National.

## Structure

`EntityParentTypeDivision`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `level` | [`Level5Enum`](../../doc/models/level-5-enum.md) | Optional | Refers to hierarchy level |
| `values` | `List[str]` | Optional | Refers to hierarchy id. Accept list of ids.<br><br>**Constraints**: *Maximum Length*: `255` |
| `chain_code` | `str` | Optional | The Chain Code is the level of the merchant hierarchy that groups merchant identifiers (MIDs) and any related roll-up values under a common identifier for settlement, billing and reporting. Chain Code is the primary identifier for merchants boarded in MDB (Merchant Database) system. <br> Chain code is mandatory to pass when hierarchy level is selected as store/division.<br><br>**Constraints**: *Maximum Length*: `6` |

## Example (as JSON)

```json
{
  "level": "DIVISION",
  "values": [
    "001",
    "002"
  ],
  "chainCode": "1X0010"
}
```

