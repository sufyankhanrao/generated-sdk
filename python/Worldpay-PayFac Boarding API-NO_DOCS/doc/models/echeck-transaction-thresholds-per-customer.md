
# Echeck Transaction Thresholds Per Customer

## Structure

`EcheckTransactionThresholdsPerCustomer`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `daily_transaction_count` | `int` | Required | The maximum number of transactions that can be processed to a consumer/business bank account in one business day |
| `daily_transaction_amount` | `int` | Required | The maximum total sum of all transactions processed to a consumer/business bank account in one business day |
| `daily_transaction_decline_count` | `int` | Required | The maximum number of declined transactions attempted to process to a consumer/business bank account in one business day |

## Example (as JSON)

```json
{
  "dailyTransactionCount": 232,
  "dailyTransactionAmount": 150,
  "dailyTransactionDeclineCount": 164
}
```

