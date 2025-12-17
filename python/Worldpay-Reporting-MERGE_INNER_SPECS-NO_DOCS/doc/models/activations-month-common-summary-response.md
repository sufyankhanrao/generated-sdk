
# Activations Month Common Summary Response

Activation summary for selected month range.

## Structure

`ActivationsMonthCommonSummaryResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `total_activated_accounts` | `int` | Optional | Total number of accounts activated for selected month range.<br><br>**Constraints**: `>= 0`, `<= 9999999999` |
| `total_activation_percentage` | `float` | Optional | Total activated percentage for selected month range.<br><br>**Constraints**: `>= 0`, `<= 9999999999999.99` |
| `average_days_to_activate` | `float` | Optional | Average days to activate account for selected month range.<br><br>**Constraints**: `>= 0`, `<= 9999999999999.99` |

## Example (as JSON)

```json
{
  "totalActivatedAccounts": 3866,
  "totalActivationPercentage": 89.3,
  "averageDaysToActivate": 51.0,
  "summaries": [
    {
      "processMonth": "processMonth8",
      "activatedAccounts": 206,
      "activationPercentage": 189.94,
      "averageDaysToActivate": 0.06
    },
    {
      "processMonth": "processMonth8",
      "activatedAccounts": 206,
      "activationPercentage": 189.94,
      "averageDaysToActivate": 0.06
    },
    {
      "processMonth": "processMonth8",
      "activatedAccounts": 206,
      "activationPercentage": 189.94,
      "averageDaysToActivate": 0.06
    }
  ]
}
```

