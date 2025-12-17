
# Deposit Settlement Summary Request

## Structure

`DepositSettlementSummaryRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `pagination` | [`PaginationType1`](../../doc/models/pagination-type-1.md) | Optional | Used for pagination. |
| `hierarchy` | [`Entity3`](../../doc/models/entity-3.md) | Required | Refers to merchant hierarchy levels |
| `date_range` | [`DateRangeSearch`](../../doc/models/date-range-search.md) | Required | A range of dates that includes a particular start and end date and all dates in between the range. |
| `settlement_type` | [`List[SettlementType]`](../../doc/models/settlement-type.md) | Optional | Type of settlement. |

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
  },
  "settlementType": [
    {
      "type": "FLEET_DISC"
    }
  ]
}
```

