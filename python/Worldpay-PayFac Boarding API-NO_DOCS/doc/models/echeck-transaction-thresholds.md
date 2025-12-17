
# Echeck Transaction Thresholds

Transaction thresholds for eCheck processing

## Structure

`EcheckTransactionThresholds`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `single_transaction_amount` | `int` | Required | The maximum amount for a single transaction |
| `daily_transaction_count` | `int` | Required | The maximum number of transactions that can be processed in one business day |
| `daily_transaction_amount` | `int` | Required | The maximum total sum of all transactions processed in one business Day |
| `monthly_transaction_count` | `int` | Required | The maximum number of transactions that can be processed in one Month |
| `monthly_transaction_amount` | `int` | Required | The maximum total sum of all transactions processed in one Month |
| `per_customer` | [`EcheckTransactionThresholdsPerCustomer`](../../doc/models/echeck-transaction-thresholds-per-customer.md) | Required | - |

## Example (as JSON)

```json
{
  "singleTransactionAmount": 248,
  "dailyTransactionCount": 18,
  "dailyTransactionAmount": 148,
  "monthlyTransactionCount": 106,
  "monthlyTransactionAmount": 132,
  "perCustomer": {
    "dailyTransactionCount": 132,
    "dailyTransactionAmount": 6,
    "dailyTransactionDeclineCount": 248
  }
}
```

