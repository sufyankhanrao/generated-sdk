
# Funding Accounts

## Structure

`FundingAccounts`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `fast_access_account` | [`FastAccessFundingAccount`](../../doc/models/fast-access-funding-account.md) | Optional | This aggregate field includes details of fast access account |
| `bank_account` | [`BankAccount`](../../doc/models/bank-account.md) | Optional | This aggregate field includes details of bank account |

## Example (as JSON)

```json
{
  "fastAccessAccount": {
    "status": "status6",
    "cardholderName": "cardholderName2",
    "cardNumber": "cardNumber8",
    "cardExpirationDate": "2016-03-13"
  },
  "bankAccount": {
    "ddaType": "CHECKING",
    "achType": "COMMERCIAL CHECKING",
    "accountNumber": "accountNumber4",
    "routingNumber": "routingNumber0",
    "bankName": "bankName6"
  }
}
```

