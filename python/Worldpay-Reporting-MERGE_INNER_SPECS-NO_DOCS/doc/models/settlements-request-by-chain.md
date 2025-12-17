
# Settlements Request by CHAIN

## Structure

`SettlementsRequestByCHAIN`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `pagination` | [`PaginationType2`](../../doc/models/pagination-type-2.md) | Optional | Used for pagination. |
| `hierarchy` | [`EntityChain2`](../../doc/models/entity-chain-2.md) | Required | Merchant hierarchy details |
| `card_type` | [`CardType1Enum`](../../doc/models/card-type-1-enum.md) | Optional | Possible value is Credit and Debit.<br>Default - All Card Type. |
| `card_networks` | [`List[CardNetwork2Enum]`](../../doc/models/card-network-2-enum.md) | Optional | Card Type mandatory when adding Card Network<br>Default - All Card Networks.<br><br>**Constraints**: *Maximum Length*: `13` |
| `date_range` | [`DateRangeSearch`](../../doc/models/date-range-search.md) | Required | Refers to date range. |

## Example (as JSON)

```json
{
  "hierarchy": {
    "level": "CHAIN",
    "values": [
      "OB2345",
      "AB1234"
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
    "DISCOVER"
  ]
}
```

