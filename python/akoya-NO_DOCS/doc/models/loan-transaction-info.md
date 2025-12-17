
# Loan Transaction Info

*This model accepts additional fields of type Any.*

## Structure

`LoanTransactionInfo`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `loan_transaction` | [`LoanTransaction`](../../doc/models/loan-transaction.md) | Optional | Loan Transaction |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example (as JSON)

```json
{
  "loanTransaction": {
    "accountId": "accountId6",
    "amount": 163.78,
    "category": "category4",
    "debitCreditMemo": "DEBIT",
    "description": "description6",
    "exampleAdditionalProperty": {
      "key1": "val1",
      "key2": "val2"
    }
  },
  "exampleAdditionalProperty": {
    "key1": "val1",
    "key2": "val2"
  }
}
```

