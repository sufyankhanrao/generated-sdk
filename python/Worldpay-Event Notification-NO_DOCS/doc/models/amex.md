
# Amex

This aggregate field includes details of Amex

## Structure

`Amex`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `program` | [`Program1Enum`](../../doc/models/program-1-enum.md) | Optional | Name of the program<br><br>**Constraints**: *Maximum Length*: `7` |
| `account_number` | `str` | Optional | Amex account number<br><br>**Constraints**: *Maximum Length*: `21` |

## Example (as JSON)

```json
{
  "program": "OptBlue",
  "accountNumber": "*********9879"
}
```

