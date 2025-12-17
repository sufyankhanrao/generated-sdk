
# Entity Parent Type Store 2

Supports entitiy as CHAIN with maximum limit of 2000 entities.

## Structure

`EntityParentTypeStore2`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `level` | [`Level51Enum`](../../doc/models/level-51-enum.md) | Optional | Level of merchant hierarchy |
| `values` | `List[str]` | Optional | Id of level<br><br>**Constraints**: *Maximum Length*: `20` |
| `chain_code` | `str` | Optional | Chain code is mandatory to pass when entity type is store\division.<br><br>**Constraints**: *Maximum Length*: `6` |

## Example (as JSON)

```json
{
  "level": "STORE",
  "values": [
    "000000001",
    "000000002"
  ],
  "chainCode": "AB1234"
}
```

