
# Leads Count Closed Lost Reason Response

Leads count for selected month range.

## Structure

`LeadsCountClosedLostReasonResponse`

## Inherits From

[`LeadsCountClosedLostReasonCommonResponse`](../../doc/models/leads-count-closed-lost-reason-common-response.md)

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `counts` | [`List[LeadsCountClosedLostReasonSummaryDetails]`](../../doc/models/leads-count-closed-lost-reason-summary-details.md) | Optional | Leads count grouped by lost reason. |

## Example (as JSON)

```json
{
  "totalCount": 82,
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

