
# Entity Parent Type Division 2

Supports entitiy as CHAIN with maximum limit of 2000 entities.

## Structure

`EntityParentTypeDivision2`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `level` | [`Level5Enum`](../../doc/models/level-5-enum.md) | Optional | Level of merchant hierarchy |
| `values` | `List[str]` | Optional | Id of level<br><br>**Constraints**: *Maximum Length*: `20` |
| `chain_code` | `str` | Optional | Chain Code is mandatory to pass when entity type is Store\Division.<br><br>**Constraints**: *Maximum Length*: `6` |

## Example (as JSON)

```json
{
  "level": "DIVISION",
  "values": [
    "001",
    "002"
  ],
  "chainCode": "AB1234"
}
```

