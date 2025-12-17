
# Entity Chain 2

## Structure

`EntityChain2`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `level` | [`Level2Enum`](../../doc/models/level-2-enum.md) | Optional | Level of merchant hierarchy |
| `values` | `List[str]` | Optional | Id of level<br><br>**Constraints**: *Maximum Length*: `20` |

## Example (as JSON)

```json
{
  "level": "CHAIN",
  "values": [
    "OB2345",
    "AB1234"
  ]
}
```

