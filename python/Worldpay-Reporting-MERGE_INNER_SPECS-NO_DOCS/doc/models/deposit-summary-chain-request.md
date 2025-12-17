
# Deposit Summary Chain Request

## Structure

`DepositSummaryChainRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `pagination` | [`PaginationType1`](../../doc/models/pagination-type-1.md) | Optional | Used for pagination. |
| `hierarchy` | [`EntityChain1`](../../doc/models/entity-chain-1.md) | Required | Refers to merchant hierarchy levels |
| `date_range` | [`DateRangeSearch`](../../doc/models/date-range-search.md) | Required | A range of dates that includes a particular start and end date and all dates in between the range. |

## Example (as JSON)

```json
{
  "hierarchy": {
    "level": "CHAIN",
    "values": [
      "0B2345",
      "AB1234"
    ]
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

