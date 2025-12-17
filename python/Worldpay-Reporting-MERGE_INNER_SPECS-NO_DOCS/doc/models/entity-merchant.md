
# Entity Merchant

## Structure

`EntityMerchant`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `level` | [`Level11Enum`](../../doc/models/level-11-enum.md) | Optional | Refers to hierarchy level |
| `values` | `List[str]` | Optional | Refers to hierarchy id. Accept list of ids.<br><br>**Constraints**: *Maximum Length*: `255` |
| `chain_code` | `str` | Optional | The Chain Code is the level of the merchant hierarchy that groups merchant identifiers (MIDs) and any related roll-up values under a common identifier for settlement, billing and reporting. Chain Code is the primary identifier for merchants boarded in MDB (Merchant Database) system.<br><br>**Constraints**: *Maximum Length*: `6` |

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

