
# Leads Count Source Response

Leads count for selected month range.

## Structure

`LeadsCountSourceResponse`

## Inherits From

[`LeadsCountSourceCommonResponse`](../../doc/models/leads-count-source-common-response.md)

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `counts` | [`List[LeadsCountSourceSummaryDetails]`](../../doc/models/leads-count-source-summary-details.md) | Optional | Leads count grouped by source. |

## Example (as JSON)

```json
{
  "totalCount": 110,
  "counts": [
    {
      "source": "source0",
      "count": 46
    },
    {
      "source": "source0",
      "count": 46
    }
  ]
}
```

