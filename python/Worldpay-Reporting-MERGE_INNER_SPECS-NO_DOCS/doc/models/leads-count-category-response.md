
# Leads Count Category Response

Leads count for the selected month range.

## Structure

`LeadsCountCategoryResponse`

## Inherits From

[`LeadsCountCategoryCommonResponse`](../../doc/models/leads-count-category-common-response.md)

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `counts` | [`List[LeadsCountCategorySummaryDetails]`](../../doc/models/leads-count-category-summary-details.md) | Optional | Leads count grouped by category. |

## Example (as JSON)

```json
{
  "totalCount": 210,
  "counts": [
    {
      "category": "category8",
      "count": 46
    },
    {
      "category": "category8",
      "count": 46
    }
  ]
}
```

