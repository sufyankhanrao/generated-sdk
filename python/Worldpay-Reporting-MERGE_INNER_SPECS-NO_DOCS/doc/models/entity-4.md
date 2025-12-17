
# Entity 4

## Structure

`Entity4`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `level` | [`Level1Enum`](../../doc/models/level-1-enum.md) | Optional | Level of merchant hierarchy |
| `values` | `List[str]` | Optional | Id of level<br><br>**Constraints**: *Maximum Length*: `20` |
| `chain_code` | `str` | Optional | Chain code is mandatory to pass when level is passed as store\division.<br><br>**Constraints**: *Maximum Length*: `6` |

## Example (as JSON)

```json
{
  "level": "MERCHANT",
  "values": [
    "4445000123456",
    "4445191034215"
  ],
  "chainCode": "AB1234"
}
```

