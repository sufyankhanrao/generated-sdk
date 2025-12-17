
# Search Auth Transactions Request Transaction Amount Range

Allows searches on transaction amount ranges and when a currency code is used, the search will only include transactions for that currency code.

## Structure

`SearchAuthTransactionsRequestTransactionAmountRange`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `from_amount` | `float` | Optional | Lowest Transaction value<br><br>**Constraints**: `>= 0`, `<= 9999999999999.99` |
| `to_amount` | `float` | Optional | Highest Transaction value<br><br>**Constraints**: `>= 0`, `<= 9999999999999.99` |
| `authorization_currency_code` | `str` | Optional | Authorization Currency Code defines alpha codes and numeric codes for the representation of currencies and provides information about the relationships between individual currencies and their minor units.<br><br>**Constraints**: *Maximum Length*: `3` |

## Example (as JSON)

```json
{
  "fromAmount": 5000.89,
  "toAmount": 120000.86,
  "authorizationCurrencyCode": "authorizationCurrencyCode2"
}
```

