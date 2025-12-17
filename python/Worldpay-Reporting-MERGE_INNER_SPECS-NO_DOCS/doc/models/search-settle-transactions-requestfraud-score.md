
# Search Settle Transactions Requestfraud Score

## Structure

`SearchSettleTransactionsRequestfraudScore`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `mfrom` | `float` | Optional | Start fraud score<br><br>**Constraints**: `>= 0.01`, `<= 100` |
| `to` | `float` | Optional | End fraud score<br><br>**Constraints**: `>= 0.01`, `<= 100` |

## Example (as JSON)

```json
{
  "from": 0.13,
  "to": 0.84
}
```

