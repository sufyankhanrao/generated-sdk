
# Debit Card Activity Summary Request

This object is used to retrieve card activity summary.

## Structure

`DebitCardActivitySummaryRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `hierarchy` | [`Hierarchy`](../../doc/models/hierarchy.md) | Required | Merchant hierarchy details |
| `card_network` | [`DebitCardNetworkEnum`](../../doc/models/debit-card-network-enum.md) | Required | Indicates the network of the cards which is associated with facilitating the payment.Card Type mandatory when adding card network.<br>Default - all card networks.<br><br>**Constraints**: *Maximum Length*: `9` |
| `card_number` | `str` | Required | This is the number found on the card used to make a purchase, also referred to as the bank card number.<br>Searches can be done on the full card number, on the first 6 and last 4 digits, or on the last 4 digit searches.<br><br>**Constraints**: *Maximum Length*: `19` |
| `date_range` | [`SearchAuthTransactionsRequestRealTimeTransactionDateRange`](../../doc/models/search-auth-transactions-request-real-time-transaction-date-range.md) | Required | Refers to date range. |

## Example (as JSON)

```json
{
  "hierarchy": {
    "level": "MERCHANT",
    "values": [
      "4445000123456",
      "4445191034215"
    ],
    "chainCode": "AB1234"
  },
  "cardNetwork": "INTERLINK",
  "cardNumber": "************4353",
  "dateRange": {
    "fromDate": "2021-12-01",
    "toDate": "2021-12-01"
  }
}
```

