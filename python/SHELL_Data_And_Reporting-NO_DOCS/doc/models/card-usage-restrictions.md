
# Card Usage Restrictions

## Structure

`CardUsageRestrictions`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `level` | `str` | Optional | Describes at which level the restriction is set at.<br>Possible values:<br>OU = Restriction set at ColCo card type<br>Customer = Restriction set at customer card type |
| `daily_spend_limit` | `float` | Optional | Maximum amount that can be spend on the card in a day. |
| `weekly_spend_limit` | `float` | Optional | Maximum amount that can be spend on the card in a week. |
| `monthly_spend_limit` | `float` | Optional | Maximum amount that can be spend on the card in a month. |
| `annual_spend_limit` | `float` | Optional | Maximum amount that can be spend on the card in a year. |
| `life_time_spend_limit` | `float` | Optional | Maximum amount that can be spend on the card in the card’s life time. |
| `daily_volume_limit` | `float` | Optional | Maximum volume of fuel that can be bought on the card in a day. |
| `weekly_volume_limit` | `float` | Optional | Maximum volume of fuel that can be bought on the card in a week. |
| `monthly_volume_limit` | `float` | Optional | Maximum volume of fuel that can be bought on the card in a month. |
| `annual_volume_limit` | `float` | Optional | Maximum volume of fuel that can be bought on the card in a year.<br><br>**Default**: `0` |
| `life_time_volume_limit` | `float` | Optional | Maximum volume of fuel that can be bought on the card in the card’s life time. |
| `transaction_spend_limit` | `float` | Optional | Maximum amount that can be spend on the card in a transaction. |
| `transaction_volume_limit` | `float` | Optional | Maximum volume of fuel that can be bought on the card in a transaction. |
| `daily_transaction_count` | `float` | Optional | Maximum number of transactions allowed on a card in a day. |
| `weekly_transaction_count` | `float` | Optional | Maximum number of transactions allowed on a card in a week. |
| `monthly_transaction_count` | `float` | Optional | Maximum number of transactions allowed on a card in a month. |
| `annual_transaction_count` | `float` | Optional | Maximum number of transactions allowed on the card in a year. |
| `life_time_transaction_count` | `float` | Optional | Maximum number of transactions allowed on the card in the card’s life time. |
| `is_velocity_ceiling` | `bool` | Optional | IsVelocityCeiling flag<br>Note: When "True", the velocity defaults configured in MS DB will be considered as the Max Limits for velocity changes. When ‘false’ max allowed limits will be 999999999999 for Type “Count” and 9999999999.99 for Type ‘Value’. |

## Example (as JSON)

```json
{
  "Level": "OU",
  "DailySpendLimit": 120.0,
  "WeeklySpendLimit": 56.07,
  "MonthlySpendLimit": 0.0,
  "AnnualSpendLimit": 0.0,
  "LifeTimeSpendLimit": 0,
  "DailyVolumeLimit": 0,
  "WeeklyVolumeLimit": 0,
  "MonthlyVolumeLimit": 0,
  "AnnualVolumeLimit": 0,
  "LifeTimeVolumeLimit": 0,
  "TransactionSpendLimit": 0,
  "TransactionVolumeLimit": 0,
  "DailyTransactionCount": 100,
  "WeeklyTransactionCount": 100,
  "MonthlyTransactionCount": 100,
  "AnnualTransactionCount": 100,
  "LifeTimeTransactionCount": 100
}
```

