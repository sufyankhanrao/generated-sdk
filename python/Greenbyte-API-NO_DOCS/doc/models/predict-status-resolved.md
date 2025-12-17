
# Predict Status Resolved

Status info for a resolved Predict alert.

## Structure

`PredictStatusResolved`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `timestamp_resolved` | `datetime` | Optional | When the alert was resolved. |
| `action_taken` | `str` | Optional | The action that was taken to resolve the alert. |
| `component_resolved` | [`Component`](../../doc/models/component.md) | Optional | A component of a wind turbine. |
| `resolved_by` | [`PredictActionEnum`](../../doc/models/predict-action-enum.md) | Optional | The action that was taken to resolve the alert. |

## Example (as JSON)

```json
{
  "timestampResolved": "01/01/2021 00:00:00",
  "actionTaken": "repair",
  "resolvedBy": "repair",
  "componentResolved": {
    "componentId": 52,
    "componentName": "componentName2",
    "componentTag": "componentTag2"
  }
}
```

