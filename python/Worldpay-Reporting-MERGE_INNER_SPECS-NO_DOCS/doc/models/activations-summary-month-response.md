
# Activations Summary Month Response

Activation summary for selected month range.

## Structure

`ActivationsSummaryMonthResponse`

## Inherits From

[`ActivationsMonthCommonSummaryResponse`](../../doc/models/activations-month-common-summary-response.md)

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `summaries` | [`List[ActivationsSummaryMonthDetails]`](../../doc/models/activations-summary-month-details.md) | Optional | Activation summary grouped by month. |

## Example (as JSON)

```json
{
  "totalActivatedAccounts": 84,
  "totalActivationPercentage": 38.68,
  "averageDaysToActivate": 252.32,
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

