
# Bundle Restriction Update

## Structure

`BundleRestrictionUpdate`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `reset_day_time_restriction` | `bool` | Optional | True/False<br>A value indicates if the day/time restriction is to be reset for card bundle.<br>Optional<br>Default value is False. |
| `reset_location_restriction` | `bool` | Optional | True/False<br>A value indicates if the location restriction is to be reset for card bundle.<br>Optional<br>Default value is False. |
| `reset_product_restriction` | `bool` | Optional | True/False<br>A value indicates if the product restriction is to be reset for card bundle.<br>Optional<br>Default value is False. |
| `usage_restrictions` | [`UsageRestrictionsCard`](../../doc/models/usage-restrictions-card.md) | Optional | - |
| `day_time_restriction_profile_id` | `str` | Optional | Identifier of the day/time restriction profile to be updated for the bundle in Gateway.<br>Optional |
| `day_time_restrictions` | [`CardDayTimeRestrictions`](../../doc/models/card-day-time-restrictions.md) | Optional | - |
| `product_restrictions` | [`ProductRestrictionCard`](../../doc/models/product-restriction-card.md) | Optional | - |
| `location_restriction_profile_id` | `str` | Optional | Identifier of the location restriction profile to be updated for the bundle in Gateway.<br>Optional |
| `location_restrictions` | [`LocationRestriction`](../../doc/models/location-restriction.md) | Optional | - |

## Example (as JSON)

```json
{
  "ResetDayTimeRestriction": false,
  "ResetLocationRestriction": false,
  "ResetProductRestriction": false,
  "UsageRestrictions": {
    "DailySpend": 7.72,
    "WeeklySpend": 10.22,
    "MonthlySpend": 48.66,
    "PerTransactionSpend": 17.28,
    "AnnualSpend": 223.08
  },
  "DayTimeRestrictionProfileId": "DayTimeRestrictionProfileId2"
}
```

