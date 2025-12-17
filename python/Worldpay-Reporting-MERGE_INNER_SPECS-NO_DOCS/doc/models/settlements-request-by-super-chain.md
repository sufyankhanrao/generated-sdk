
# Settlements Request by Super Chain

## Structure

`SettlementsRequestBySuperChain`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `pagination` | [`PaginationType2`](../../doc/models/pagination-type-2.md) | Optional | Used for pagination. |
| `hierarchy` | [`EntitySuperChain1`](../../doc/models/entity-super-chain-1.md) | Required | Merchant hierarchy details |
| `card_type` | [`CardType1Enum`](../../doc/models/card-type-1-enum.md) | Optional | Possible value is Credit and Debit.<br>Default - All Card Type. |
| `card_networks` | [`List[CardNetwork2Enum]`](../../doc/models/card-network-2-enum.md) | Optional | Card Type mandatory when adding Card Network<br>Default - All Card Networks.<br><br>**Constraints**: *Maximum Length*: `13` |
| `date_range` | [`DateRangeSearch`](../../doc/models/date-range-search.md) | Required | Refers to date range. |

## Example (as JSON)

```json
{
  "hierarchy": {
    "level": "SUPERCHAIN",
    "values": [
      "733123456",
      "845123456"
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
    "VISA",
    "COBRAND",
    "FLEETONE"
  ]
}
```

