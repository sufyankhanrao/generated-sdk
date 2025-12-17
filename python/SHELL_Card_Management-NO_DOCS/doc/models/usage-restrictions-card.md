
# Usage Restrictions Card

## Structure

`UsageRestrictionsCard`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `daily_spend` | `float` | Optional | Maximum spend value (amount) allowed per day.<br>Optional<br>It allows null in the input field. If Values is passed as null, apply the card type limit. However, if the card type limit is NULL for the same field then No limit will be applied in Gateway. |
| `weekly_spend` | `float` | Optional | Maximum spend value (amount) allowed per week.<br>Optional |
| `monthly_spend` | `float` | Optional | Maximum spend value (amount) allowed per month.<br>Optional |
| `per_transaction_spend` | `float` | Optional | Maximum spend value (amount) allowed per transaction.<br>Optional |
| `annual_spend` | `float` | Optional | Maximum spend value (amount) allowed per annum.<br>Optional |
| `life_time_spend` | `float` | Optional | Maximum spend value (amount) allowed in card’s life time.<br>Optional |
| `daily_volume` | `float` | Optional | Maximum volume (quantity) allowed per day.<br>Optional |
| `weekly_volume` | `float` | Optional | Maximum volume (quantity) allowed per week.<br>Optional |
| `monthly_volume` | `float` | Optional | Maximum volume (quantity) allowed per month.<br>Optional |
| `per_transaction_volume` | `float` | Optional | Maximum volume (quantity) allowed per transaction.<br>Optional |
| `annual_volume` | `float` | Optional | Maximum volume (quantity) allowed per annum.<br>Optional |
| `life_time_volume` | `float` | Optional | Maximum volume (quantity) allowed in card’s life time.<br>Optional |
| `daily_transaction_count` | `float` | Optional | Maximum number of transactions allowed per day.<br>Optional |
| `weekly_transaction_count` | `float` | Optional | Maximum number of transactions allowed per week.<br>Optional |
| `monthly_transaction_count` | `float` | Optional | Maximum number of transactions allowed per month.<br>Optional. |
| `annual_transaction_count` | `float` | Optional | Maximum number of transactions allowed per annum. |
| `life_time_transaction_count` | `float` | Optional | Maximum number of transactions allowed in card’s lifetime.<br>Optional |

## Example (as JSON)

```json
{
  "DailySpend": 76.58,
  "WeeklySpend": 181.92,
  "MonthlySpend": 132.96,
  "PerTransactionSpend": 101.58,
  "AnnualSpend": 51.38
}
```

