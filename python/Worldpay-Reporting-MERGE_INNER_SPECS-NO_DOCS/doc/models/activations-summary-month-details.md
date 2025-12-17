
# Activations Summary Month Details

Activation summary grouped by month.

## Structure

`ActivationsSummaryMonthDetails`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `process_month` | `str` | Optional | Process month.<br><br>**Constraints**: *Minimum Length*: `7`, *Maximum Length*: `7`, *Pattern*: `^[0-9]{4}-[0-9]{2}$` |
| `activated_accounts` | `int` | Optional | Number of accounts activated for the month.<br><br>**Constraints**: `>= 0`, `<= 9999999999` |
| `activation_percentage` | `float` | Optional | Activation percentage for the month.<br><br>**Constraints**: `>= 0`, `<= 9999999999999.99` |
| `average_days_to_activate` | `float` | Optional | Average day to activate account for the month.<br><br>**Constraints**: `>= 0`, `<= 9999999999999.99` |

## Example (as JSON)

```json
{
  "processMonth": "2021-02",
  "activatedAccounts": 124,
  "activationPercentage": 68.75,
  "averageDaysToActivate": 32.0
}
```

