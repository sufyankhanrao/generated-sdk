
# Auth Transactions Request

## Structure

`AuthTransactionsRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `hierarchy` | [`Entity1`](../../doc/models/entity-1.md) | Required | Refers to merchant hierarchy levels |
| `card_type` | `str` | Optional | Default - Credit<br>Debit not supported in this release.<br><br>**Constraints**: *Minimum Length*: `0`, *Maximum Length*: `255` |
| `card_networks` | [`List[CardNetworkTypeEnum]`](../../doc/models/card-network-type-enum.md) | Optional | Indicates the network of the cards which is associated with facilitating the payment.<br>Default - All Card Networks.s. |
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
  "cardNetworks": [
    "AMEX",
    "DISCOVER"
  ]
}
```

