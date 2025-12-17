
# Deposit Summary Merchant Request

## Structure

`DepositSummaryMerchantRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `pagination` | [`PaginationType1`](../../doc/models/pagination-type-1.md) | Optional | Used for pagination. |
| `hierarchy` | [`EntityMerchant1`](../../doc/models/entity-merchant-1.md) | Required | Refers to merchant hierarchy levels |
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
  },
  "pagination": {
    "pageNumber": 16776215,
    "pageSize": 1000
  }
}
```

