
# Terminal Details

## Structure

`TerminalDetails`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `terminal_number` | `int` | Optional | The Unique identification number for every terminal of a merchant |
| `terminal_settlement_type` | [`TerminalSettlementTypeEnum`](../../doc/models/terminal-settlement-type-enum.md) | Optional | The type of settlement for a terminal. <br> Possible values are - "UPLOAD","AUTO_CLOSE","MANUAL" |

## Example (as JSON)

```json
{
  "terminalNumber": 5,
  "terminalSettlementType": "UPLOAD"
}
```

