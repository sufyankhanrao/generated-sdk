
# Auth Transactions Summary Request by Transaction Date

## Structure

`AuthTransactionsSummaryRequestByTransactionDate`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `pagination` | [`PaginationType2`](../../doc/models/pagination-type-2.md) | Optional | Used for pagination. |
| `hierarchy` | [`Entity1`](../../doc/models/entity-1.md) | Required | Refers to merchant hierarchy levels |
| `card_type` | `str` | Optional | Default - Credit.<br><br>**Constraints**: *Minimum Length*: `0`, *Maximum Length*: `255` |
| `card_networks` | [`List[CardNetworkTypeEnum]`](../../doc/models/card-network-type-enum.md) | Optional | Indicates the network of the cards which is associated with facilitating the payment.<br>Default - All Card Networks. |
| `date_range` | [`DateRangeSearch`](../../doc/models/date-range-search.md) | Required | A range of dates that includes a particular start and end date and all dates in between the range. |

## Example (as JSON)

```json
{
  "hierarchy": {
    "level": "MERCHANT",
    "values": [
      "4445000123456",
      "4445000234567"
    ],
    "chainCode": "1X0010"
  },
  "cardType": "CREDIT",
  "dateRange": {
    "fromDate": "2021-12-01",
    "toDate": "2021-12-01"
  },
  "pagination": {
    "pageNumber": 106,
    "pageSize": 134
  },
  "cardNetworks": [
    "WRIGHT_EXPRESS",
    "DINERS",
    "AMEX"
  ]
}
```

