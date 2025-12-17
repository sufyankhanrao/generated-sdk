
# Entity Merchant 2

## Structure

`EntityMerchant2`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `level` | [`Level11Enum`](../../doc/models/level-11-enum.md) | Optional | Level of merchant hierarchy |
| `values` | `List[str]` | Optional | Id of level<br><br>**Constraints**: *Maximum Length*: `20` |
| `chain_code` | `str` | Optional | CHAIN Code is mandatory to pass when entity type is STORE\DIVISION.<br><br>**Constraints**: *Maximum Length*: `6` |

## Example (as JSON)

```json
{
  "level": "MERCHANT",
  "values": [
    "4445000123456",
    "4445000234567"
  ],
  "chainCode": "AB1234"
}
```

