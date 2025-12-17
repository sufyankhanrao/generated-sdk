
# Search Auth Transactions Requesttransaction Amount Range 1

## Structure

`SearchAuthTransactionsRequesttransactionAmountRange1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `from_amount` | `float` | Optional | Lowest Transaction value |
| `to_amount` | `float` | Optional | Highest Transaction value |
| `authorization_currency_code` | `str` | Optional | Authorization Currency Code defines alpha codes and numeric codes for the representation of currencies and provides information about the relationships between individual currencies and their minor units.<br><br>**Constraints**: *Maximum Length*: `3` |

## Example (as JSON)

```json
{
  "fromAmount": 5000.89,
  "toAmount": 120000.86,
  "authorizationCurrencyCode": "authorizationCurrencyCode0"
}
```

