
# Entity Parent Type Store 1

## Structure

`EntityParentTypeStore1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `level` | [`Level3Enum`](../../doc/models/level-3-enum.md) | Optional | Refers to hierarchy level |
| `values` | `List[str]` | Optional | Refers to hierarchy id. Accept list of ids.<br><br>**Constraints**: *Maximum Length*: `2000` |
| `chain_code` | `str` | Optional | The Chain Code is the level of the merchant hierarchy that groups merchant identifiers (MIDs) and any related roll-up values under a common identifier for settlement, billing and reporting. Chain Code is the primary identifier for merchants boarded in MDB (Merchant Database) system. <br> Chain code is mandatory to pass when hierarchy level is selected as store/division.<br><br>**Constraints**: *Maximum Length*: `6` |

## Example (as JSON)

```json
{
  "level": "STORE",
  "values": [
    "000000001",
    "000000002"
  ],
  "chainCode": "172111"
}
```

