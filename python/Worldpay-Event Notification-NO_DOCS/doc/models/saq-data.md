
# Saq Data

## Structure

`SaqData`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `mtype` | `str` | Optional | Type<br><br>**Constraints**: *Maximum Length*: `8` |
| `status` | `str` | Optional | Status<br><br>**Constraints**: *Maximum Length*: `1` |
| `completed_date` | `str` | Optional | Completed Date<br><br>**Constraints**: *Maximum Length*: `10`, *Pattern*: `[0-9]{4}-[0-2]{2}-[0-2]{2}` |
| `status_date` | `str` | Optional | status Date<br><br>**Constraints**: *Maximum Length*: `10`, *Pattern*: `[0-9]{4}-[0-2]{2}-[0-2]{2}` |
| `next_due_date` | `str` | Optional | Next Due Date<br><br>**Constraints**: *Maximum Length*: `10`, *Pattern*: `[0-9]{4}-[0-2]{2}-[0-2]{2}` |

## Example (as JSON)

```json
{
  "type": "B",
  "status": "P",
  "completedDate": "completedDate8",
  "statusDate": "statusDate8",
  "nextDueDate": "nextDueDate6"
}
```

