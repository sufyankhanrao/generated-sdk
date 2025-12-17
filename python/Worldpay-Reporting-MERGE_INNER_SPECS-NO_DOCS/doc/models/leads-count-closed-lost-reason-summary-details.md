
# Leads Count Closed Lost Reason Summary Details

Leads count grouped by lost reason.

## Structure

`LeadsCountClosedLostReasonSummaryDetails`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `closed_lost_reason` | `str` | Optional | Reason due to which leads are lost.<br><br>**Constraints**: *Maximum Length*: `10000` |
| `count` | `float` | Optional | Number of leads lost due to specific reason.<br><br>**Constraints**: `>= 0`, `<= 9999999999` |

## Example (as JSON)

```json
{
  "closedLostReason": "Project Cancelled",
  "count": 741.0
}
```

