
# Multi Priced Transaction Request Accounts Items

## Structure

`MultiPricedTransactionRequestAccountsItems`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `payer_id` | `int` | Optional | Payer Id of the selected payer.<br>Optional if PayerNumber is passed else Mandatory<br>Example: 123456 |
| `payer_number` | `str` | Optional | Payer Number (Ex: GB000000123) of the selected payer.<br>Optional if PayerId is passed else Mandatory<br>Example: GB000000123 |
| `account_id` | `int` | Optional | Account Id  of the selected account. |
| `account_number` | `str` | Optional | Account Number (ex: GB000000123) of the selected account. |

## Example (as JSON)

```json
{
  "PayerId": 144,
  "PayerNumber": "PayerNumber2",
  "AccountId": 204,
  "AccountNumber": "AccountNumber4"
}
```

