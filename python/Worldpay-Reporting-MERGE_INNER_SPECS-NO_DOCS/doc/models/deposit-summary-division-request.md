
# Deposit Summary Division Request

## Structure

`DepositSummaryDivisionRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `pagination` | [`PaginationType1`](../../doc/models/pagination-type-1.md) | Optional | Used for pagination. |
| `hierarchy` | [`EntityParentTypeDivision1`](../../doc/models/entity-parent-type-division-1.md) | Required | Refers to merchant hierarchy levels |
| `date_range` | [`DateRangeSearch`](../../doc/models/date-range-search.md) | Required | A range of dates that includes a particular start and end date and all dates in between the range. |

## Example (as JSON)

```json
{
  "hierarchy": {
    "level": "DIVISION",
    "values": [
      "001",
      "002"
    ],
    "chainCode": "172111"
  },
  "dateRange": {
    "fromDate": "2021-12-01",
    "toDate": "2021-12-01"
  },
  "pagination": {
    "pageNumber": 16776215,
    "pageSize": 1000
  }
}
```

