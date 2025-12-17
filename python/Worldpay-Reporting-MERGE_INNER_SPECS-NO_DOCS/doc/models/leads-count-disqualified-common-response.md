
# Leads Count Disqualified Common Response

Leads count for selected month range.

## Structure

`LeadsCountDisqualifiedCommonResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `total_count` | `int` | Optional | Total number of leads for the selected month range<br><br>**Constraints**: `>= 0`, `<= 9999999999` |
| `counts` | [`List[LeadsCountDisqualifiedSummaryDetails]`](../../doc/models/leads-count-disqualified-summary-details.md) | Optional | Leads count grouped by disqualification reason. |

## Example (as JSON)

```json
{
  "totalCount": 35781,
  "counts": [
    {
      "disqualificationReason": "disqualificationReason2",
      "count": 36.3
    }
  ]
}
```

