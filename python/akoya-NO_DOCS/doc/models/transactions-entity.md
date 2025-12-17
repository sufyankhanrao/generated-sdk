
# Transactions Entity

Optionally paginated array of transactions

*This model accepts additional fields of type Any.*

## Structure

`TransactionsEntity`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `links` | [`Links`](../../doc/models/links.md) | Optional | - |
| `transactions` | List[[DepositTransactionInfo](../../doc/models/deposit-transaction-info.md) \| [LoanTransactionInfo](../../doc/models/loan-transaction-info.md) \| [LocTransactionInfo](../../doc/models/loc-transaction-info.md) \| [InvestmentTransactionInfo](../../doc/models/investment-transaction-info.md) \| [InsuranceTransactionInfo](../../doc/models/insurance-transaction-info.md)] \| None | Optional | This is List of a container for any-of cases. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example (as JSON)

```json
{
  "links": {
    "next": {
      "href": "href4",
      "exampleAdditionalProperty": {
        "key1": "val1",
        "key2": "val2"
      }
    },
    "prev": {
      "href": "href8",
      "exampleAdditionalProperty": {
        "key1": "val1",
        "key2": "val2"
      }
    },
    "exampleAdditionalProperty": {
      "key1": "val1",
      "key2": "val2"
    }
  },
  "transactions": [
    {
      "depositTransaction": {
        "accountId": "accountId0",
        "amount": 1.72,
        "category": "category8",
        "debitCreditMemo": "DEBIT",
        "description": "description0",
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
  ],
  "exampleAdditionalProperty": {
    "key1": "val1",
    "key2": "val2"
  }
}
```

