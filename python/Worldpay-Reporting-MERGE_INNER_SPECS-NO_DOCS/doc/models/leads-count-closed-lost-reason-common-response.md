
# Leads Count Closed Lost Reason Common Response

Leads count for selected month range.

## Structure

`LeadsCountClosedLostReasonCommonResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `total_count` | `int` | Optional | Total number of leads for the selected month range<br><br>**Constraints**: `>= 0`, `<= 9999999999` |

## Example (as JSON)

```json
{
  "totalCount": 35781,
  "counts": [
    {
      "closedLostReason": "closedLostReason0",
      "count": 36.3
    },
    {
      "closedLostReason": "closedLostReason0",
      "count": 36.3
    }
  ]
}
```

