
# Predict Status Dismissed

Status info for a dismissed Predict alert.

## Structure

`PredictStatusDismissed`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `timestamp_dismissed` | `datetime` | Optional | When the alert was dismissed. |
| `dismissed_by` | `str` | Optional | The user who dismissed the alert |

## Example (as JSON)

```json
{
  "timestampDismissed": "01/01/2021 00:00:00",
  "dismissedBy": "Jane Doe"
}
```

