
# Additional Accepted Card Info

## Structure

`AdditionalAcceptedCardInfo`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `amex` | [`Amex`](../../doc/models/amex.md) | Optional | This aggregate field includes details of Amex |
| `discover` | [`Discover`](../../doc/models/discover.md) | Optional | This aggregate field includes details of discover |
| `pin_or_debit` | `bool` | Optional | Indicator for Pin or Debit |
| `wic` | `bool` | Optional | Indicator for WIC |
| `valutec` | [`Valutec`](../../doc/models/valutec.md) | Optional | This aggregate field includes details of valutec gift cards |
| `ebt` | [`NetworkDetails`](../../doc/models/network-details.md) | Optional | This aggregate field includes details of EBT |
| `jcb` | [`NetworkDetails`](../../doc/models/network-details.md) | Optional | This aggregate field includes details of JCB |
| `master_card` | [`NetworkDetails`](../../doc/models/network-details.md) | Optional | This aggregate field includes details of master card |
| `visa` | [`NetworkDetails`](../../doc/models/network-details.md) | Optional | This aggregate field includes details of visa |

## Example (as JSON)

```json
{
  "pinOrDebit": true,
  "WIC": true,
  "amex": {
    "program": "OptBlue",
    "accountNumber": "accountNumber6"
  },
  "discover": {
    "discoveredAcquired": false,
    "accountNumber": "accountNumber0"
  },
  "valutec": {
    "groupId": "groupId2",
    "billingAccountNumber": "billingAccountNumber4",
    "billingRoutingNumber": "billingRoutingNumber4",
    "settlementAccountNumber": "settlementAccountNumber6",
    "settlementRoutingNumber": "settlementRoutingNumber6",
    "lastUpdatedDateTime": "lastUpdatedDateTime4"
  }
}
```

