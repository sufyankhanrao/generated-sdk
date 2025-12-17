
# Summary Request

## Structure

`SummaryRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `hierarchy` | [`Entity3`](../../doc/models/entity-3.md) | Required | Refers to merchant hierarchy levels |
| `date_range` | [`DateRangeSearch`](../../doc/models/date-range-search.md) | Required | A range of dates that includes a particular start and end date and all dates in between the range. |

## Example (as JSON)

```json
{
  "hierarchy": {
    "level": "MERCHANT",
    "values": [
      "4445001234567",
      "4445002345678"
    ],
    "chainCode": "172111"
  },
  "dateRange": {
    "fromDate": "2021-12-01",
    "toDate": "2021-12-01"
  }
}
```

