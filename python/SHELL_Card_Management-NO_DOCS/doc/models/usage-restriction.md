
# Usage Restriction

Details of the usage restrictions such as day/week/month value and volume restrictions applied on the card.

## Structure

`UsageRestriction`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `level` | `str` | Optional | Usage limit is applied on the card from this level.<br>Valid values –<br>•	Inherited<br>•	Card<br>When Card level usage restrictions are not present, the API will return the inherited restrictions.<br>Note: -This field is deprecated. Instead, use ‘Override’. |
| `daily_spend` | `float` | Optional | Maximum spend value (amount) allowed per day.<br>Card limit ‘0’ represents the value is inherited and inherited limit could be calculated by adding accumulated and balance.<br>However, Inherited limit ‘0’ represents unlimited. |
| `daily_spend_accumulated` | `float` | Optional | Balance spend value (amount) available for rest of the day. |
| `daily_spend_balance` | `float` | Optional | Balance spend value (amount) available for rest of the day. |
| `daily_spend_override` | `bool` | Optional | Indicate if the limit is overridden or default. (False for default).<br>Example: false |
| `daily_spend_threshold` | `float` | Optional | The limit to trigger an alert if the balance after a transaction reaches it or below. 0 indicates no alerts will be sent. Not present if not set (issuer value threshold limit applies if available). Not present for COUNT type velocity.<br>Example: 50.55 |
| `weekly_spend` | `float` | Optional | Maximum spend value (amount) allowed per week.<br>Card limit ‘0’ represents the value is inherited and inherited limit could be calculated by adding accumulated and balance.<br>However, Inherited limit ‘0’ represents unlimited. |
| `weekly_spend_accumulated` | `float` | Optional | Value (amount) spent during the week. |
| `weekly_spend_balance` | `float` | Optional | Balance spend value (amount) available for rest of the week. |
| `weekly_spend_override` | `bool` | Optional | Indicate if the limit is overridden or default. (False for default).<br>Example: false |
| `weekly_spend_threshold` | `float` | Optional | The limit to trigger an alert if the balance after a transaction reaches it or below. 0 indicates no alerts will be sent. Not present if not set (issuer value threshold limit applies if available). Not present for COUNT type velocity.<br>Example: 50.55<br>This is an optional output field. |
| `monthly_spend` | `float` | Optional | Maximum spend value (amount) allowed per month.<br>Card limit ‘0’ represents the value is inherited and inherited limit could be calculated by adding accumulated and balance.<br>However, Inherited limit ‘0’ represents unlimited. |
| `monthly_spend_accumulated` | `float` | Optional | Value (amount) spent during the month. |
| `monthly_spend_balance` | `float` | Optional | Balance spend value (amount) available for rest of the month. |
| `monthly_spend_override` | `bool` | Optional | Indicate if the limit is overridden or default. (False for default).<br>Example: false |
| `per_transaction_spend` | `float` | Optional | Maximum spend value (amount) allowed per transaction.<br>Card limit ‘0’ represents the value is inherited and inherited limit could be calculated by adding accumulated and balance.<br>However, Inherited limit ‘0’ represents unlimited. |
| `per_transaction_spend_override` | `bool` | Optional | Indicate if the limit is overridden or default. (False for default).<br>Example: false |
| `annual_spend` | `float` | Optional | Maximum spend value (amount) allowed per annum.<br>Card limit ‘0’ represents the value is inherited and inherited limit could be calculated by adding accumulated and balance.<br>However, Inherited limit ‘0’ represents unlimited. |
| `annual_spend_accumulated` | `float` | Optional | Value (amount) spent during the year. |
| `annual_spend_balance` | `float` | Optional | Balance spend value (amount) available for rest of the year. |
| `annual_spend_override` | `bool` | Optional | Indicate if the limit is overridden or default. (False for default).<br>Example: false |
| `annual_spend_threshold` | `float` | Optional | The limit to trigger an alert if the balance after a transaction reaches it or below. 0 indicates no alerts will be sent. Not present if not set (issuer value threshold limit applies if available). Not present for COUNT type velocity.<br>Example: 50.55<br>This is an optional output field. |
| `life_time_spend` | `float` | Optional | Maximum spend value (amount) allowed in card’s life time.<br>Card limit ‘0’ represents the value is inherited and inherited limit could be calculated by adding accumulated and balance.<br>However, Inherited limit ‘0’ represents unlimited |
| `life_time_spend_accumulated` | `float` | Optional | Value (amount) spent during the card’s life time |
| `life_time_spend_balance` | `float` | Optional | Balance spend value (amount) available for rest of the card’s life time. |
| `life_time_spend_override` | `bool` | Optional | Indicate if the limit is overridden or default. (False for default).<br>Example: false |
| `life_time_spend_threshold` | `float` | Optional | The limit to trigger an alert if the balance after a transaction reaches it or below. 0 indicates no alerts will be sent. Not present if not set (issuer value threshold limit applies if available). Not present for COUNT type velocity.<br>Example: 50.55<br>This is an optional output field. |
| `daily_volume` | `float` | Optional | Maximum volume (quantity) allowed per day.<br>Card limit ‘0’ represents the value is inherited and inherited limit could be calculated by adding accumulated and balance.<br>However, Inherited limit ‘0’ represents unlimited. |
| `daily_volume_accumulated` | `float` | Optional | Volume (quantity) bought during the day. |
| `daily_volume_balance` | `float` | Optional | Balance volume (quantity) available for rest of the day. |
| `daily_volume_override` | `float` | Optional | Indicate if the limit is overridden or default. (False for default).<br>Example: false |
| `daily_volume_threshold` | `float` | Optional | The limit to trigger an alert if the balance after a transaction reaches it or below. 0 indicates no alerts will be sent. Not present if not set (issuer value threshold limit applies if available). Not present for COUNT type velocity.<br>Example: 50.55<br>This is an optional output field. |
| `weekly_volume` | `float` | Optional | Maximum volume (quantity) allowed per week.<br>Card limit ‘0’ represents the value is inherited and inherited limit could be calculated by adding accumulated and balance.<br>However, Inherited limit ‘0’ represents unlimited. |
| `weekly_volume_accumulated` | `float` | Optional | Volume (quantity) bought during the week. |
| `weekly_volume_balance` | `float` | Optional | Balance volume (quantity) available for rest of the week. |
| `weekly_volume_override` | `bool` | Optional | Indicate if the limit is overridden or default. (False for default).<br>Example: false |
| `weekly_volume_threshold` | `float` | Optional | The limit to trigger an alert if the balance after a transaction reaches it or below. 0 indicates no alerts will be sent. Not present if not set (issuer value threshold limit applies if available). Not present for COUNT type velocity.<br>Example: 50.55<br>This is an optional output field. |
| `monthly_volume` | `float` | Optional | Maximum volume (quantity) allowed per month.<br>Card limit ‘0’ represents the value is inherited and inherited limit could be calculated by adding accumulated and balance.<br>However, Inherited limit ‘0’ represents unlimited. |
| `monthly_volume_accumulated` | `float` | Optional | Volume (quantity) bought during the month. |
| `monthly_volume_balance` | `float` | Optional | Balance volume (quantity) available for rest of the month. |
| `monthly_volume_override` | `bool` | Optional | Indicate if the limit is overridden or default. (False for default). |
| `monthly_volume_threshold` | `float` | Optional | The limit to trigger an alert if the balance after a transaction reaches it or below. 0 indicates no alerts will be sent. Not present if not set (issuer value threshold limit applies if available). Not present for COUNT type velocity.<br>Example: 50.55<br>This is an optional output field. |
| `per_transaction_volume` | `float` | Optional | Maximum volume (quantity) allowed per transaction.<br>Card limit ‘0’ represents the value is inherited and inherited limit could be calculated by adding accumulated and balance.<br>However, Inherited limit ‘0’ represents unlimited. |
| `per_transaction_volume_override` | `bool` | Optional | Indicate if the limit is overridden or default. (False for default).<br>Example: false |
| `annual_volume` | `float` | Optional | Maximum volume (quantity) allowed per annum.<br>Card limit ‘0’ represents the value is inherited and inherited limit could be calculated by adding accumulated and balance.<br>However, Inherited limit ‘0’ represents unlimited. |
| `annual_volume_accumulated` | `float` | Optional | Volume (quantity) bought during the year. |
| `annual_volume_balance` | `float` | Optional | Balance volume (quantity) available for rest of the year. |
| `annual_volume_override` | `bool` | Optional | Indicate if the limit is overridden or default. (False for default).<br>Example: false |
| `annual_volume_threshold` | `float` | Optional | The limit to trigger an alert if the balance after a transaction reaches it or below. 0 indicates no alerts will be sent. Not present if not set (issuer value threshold limit applies if available). Not present for COUNT type velocity.<br>Example: 50.55<br>This is an optional output field. |
| `life_time_volume` | `float` | Optional | Maximum volume (quantity) allowed in the card’s life time.<br>Card limit ‘0’ represents the value is inherited and inherited limit could be calculated by adding accumulated and balance.<br>However, Inherited limit ‘0’ represents unlimited. |
| `life_time_volume_accumulated` | `float` | Optional | Volume (quantity) bought during the card’s life time. |
| `life_time_volume_balance` | `float` | Optional | Balance volume (quantity) available for rest of the card’s life time. |
| `life_time_volume_override` | `bool` | Optional | Indicate if the limit is overridden or default. (False for default).<br>Example: false |
| `life_time_volume_threshold` | `float` | Optional | The limit to trigger an alert if the balance after a transaction reaches it or below. 0 indicates no alerts will be sent. Not present if not set (issuer value threshold limit applies if available). Not present for COUNT type velocity.<br>Example: 50.55<br>This is an optional output field. |
| `daily_transaction_count` | `float` | Optional | Maximum number of transactions allowed per day.<br>Card limit ‘0’ represents the value is inherited and inherited limit could be calculated by adding accumulated and balance.<br>However, Inherited limit ‘0’ represents unlimited |
| `daily_transaction_accumulated` | `float` | Optional | Number of times the card is used during the day. |
| `daily_transaction_balance` | `float` | Optional | Number of times the card could be used in rest of the day. |
| `daily_transaction_override` | `bool` | Optional | Indicate if the limit is overridden or default. (False for default).<br>Example: false |
| `daily_transaction_threshold` | `float` | Optional | The limit to trigger an alert if the balance after a transaction reaches it or below. 0 indicates no alerts will be sent. Not present if not set (issuer value threshold limit applies if available). Not present for COUNT type velocity.<br>Example: 50.55<br>This is an optional output field. |
| `weekly_transaction_count` | `float` | Optional | Maximum number of transactions allowed per week.<br>Card limit ‘0’ represents the value is inherited and inherited limit could be calculated by adding accumulated and balance.<br>However, Inherited limit ‘0’ represents unlimited. |
| `weekly_transaction_accumulated` | `float` | Optional | Number of times the card is used during the week |
| `weekly_transaction_balance` | `float` | Optional | Number of times the card could be used in rest of the week. |
| `weekly_transaction_override` | `bool` | Optional | Indicate if the limit is overridden or default. (False for default).<br>Example: false |
| `weekly_transaction_threshold` | `float` | Optional | The limit to trigger an alert if the balance after a transaction reaches it or below. 0 indicates no alerts will be sent. Not present if not set (issuer value threshold limit applies if available). Not present for COUNT type velocity.<br>Example: 50.55<br>This is an optional output field. |
| `monthly_transaction_count` | `float` | Optional | Maximum number of transactions allowed per month.<br>Card limit ‘0’ represents the value is inherited and inherited limit could be calculated by adding accumulated and balance.<br>However, Inherited limit ‘0’ represents unlimited. |
| `monthly_transaction_accumulated` | `float` | Optional | Number of times the card is used during the month |
| `monthly_transaction_balance` | `float` | Optional | Number of times the card could be used in rest of the month. |
| `monthly_transaction_override` | `bool` | Optional | Indicate if the limit is overridden or default. (False for default).<br>Example: false |
| `monthly_transaction_threshold` | `float` | Optional | The limit to trigger an alert if the balance after a transaction reaches it or below. 0 indicates no alerts will be sent. Not present if not set (issuer value threshold limit applies if available). Not present for COUNT type velocity.<br>Example: 50.55<br>This is an optional output field. |
| `annual_transaction_count` | `float` | Optional | Maximum number of transactions allowed per annum.<br>Card limit ‘0’ represents the value is inherited and inherited limit could be calculated by adding accumulated and balance. |
| `annual_transaction_accumulated` | `float` | Optional | Number of times the card is used during the year. |
| `annual_transaction_balance` | `float` | Optional | Number of times the card could be used in rest of the year. |
| `annual_transaction_override` | `bool` | Optional | Indicate if the limit is overridden or default. (False for default).<br>Example: false |
| `annual_transaction_threshold` | `float` | Optional | The limit to trigger an alert if the balance after a transaction reaches it or below. 0 indicates no alerts will be sent. Not present if not set (issuer value threshold limit applies if available). Not present for COUNT type velocity.<br>Example: 50.55<br>This is an optional output field. |
| `life_time_transaction_count` | `float` | Optional | Maximum number of transactions allowed in the card’s life time.<br>Card limit ‘0’ represents the value is inherited and inherited limit could be calculated by adding accumulated and balance.<br>However, Inherited limit ‘0’ represents unlimited. |
| `life_time_transaction_accumulated` | `float` | Optional | Number of times the card is used during the card’s life time. |
| `life_time_transaction_balance` | `float` | Optional | Number of times the card could be used in rest of the card’s life time. |
| `life_time_transaction_override` | `bool` | Optional | Indicate if the limit is overridden or default. (False for default).<br>Example: false |
| `life_time_transaction_threshold` | `float` | Optional | The limit to trigger an alert if the balance after a transaction reaches it or below. 0 indicates no alerts will be sent. Not present if not set (issuer value threshold limit applies if available). Not present for COUNT type velocity.<br>Example: 50.55<br>This is an optional output field. |

## Example (as JSON)

```json
{
  "Level": "Level8",
  "DailySpend": 43.36,
  "DailySpendAccumulated": 178.28,
  "DailySpendBalance": 56.44,
  "DailySpendOverride": false
}
```

