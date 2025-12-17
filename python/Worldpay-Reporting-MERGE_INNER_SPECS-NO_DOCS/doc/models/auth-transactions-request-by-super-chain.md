
# Auth Transactions Request by Super Chain

## Structure

`AuthTransactionsRequestBySuperChain`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `pagination` | [`PaginationType2`](../../doc/models/pagination-type-2.md) | Optional | Used for pagination. |
| `hierarchy` | [`EntitySuperChain`](../../doc/models/entity-super-chain.md) | Required | Refers to merchant hierarchy levels |
| `card_type` | `str` | Optional | Default - Credit.<br><br>**Constraints**: *Minimum Length*: `0`, *Maximum Length*: `255` |
| `card_networks` | [`List[CardNetworkTypeEnum]`](../../doc/models/card-network-type-enum.md) | Optional | Indicates the network of the cards which is associated with facilitating the payment.<br>Default - All Card Networks. |
| `date_range` | [`DateRangeSearch`](../../doc/models/date-range-search.md) | Required | A range of dates that includes a particular start and end date and all dates in between the range. |

## Example (as JSON)

```json
{
  "hierarchy": {
    "level": "SUPERCHAIN",
    "values": [
      "731234567",
      "841234567"
    ]
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
    "BILL_ME_LATER",
    "VISA",
    "MASTERCARD"
  ]
}
```

