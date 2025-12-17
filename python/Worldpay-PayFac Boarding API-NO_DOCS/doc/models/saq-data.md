
# Saq Data

## Structure

`SaqData`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `mtype` | [`Type4Enum`](../../doc/models/type-4-enum.md) | Optional | SAQ type |
| `status` | [`Status2Enum`](../../doc/models/status-2-enum.md) | Required | SAQ status, F-Failed, I-In-Progress, P-Passed, X-Not Started, Y-Passed, N-Failed<br><br>**Constraints**: *Maximum Length*: `15` |
| `complete_date` | `str` | Optional | SAQ completed Date |
| `status_date` | `str` | Required | SAQ status Date |
| `next_due_date` | `str` | Required | Next SAQ required Date |

## Example (as JSON)

```json
{
  "type": "B (applies to merchants with no electronic cardholder data storage and who process payments either by standalone terminals or imprint-only machines)",
  "status": "FAILED",
  "completeDate": "completeDate2",
  "statusDate": "statusDate8",
  "nextDueDate": "nextDueDate6"
}
```

