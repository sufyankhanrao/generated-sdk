
# Predict Status Active

Status info for an active Predict alert.

## Structure

`PredictStatusActive`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `recommendations` | [`List[PredictRecommendation]`](../../doc/models/predict-recommendation.md) | Optional | Recommended actions for resolving the alert. Will be null if not calculated yet. |

## Example (as JSON)

```json
{
  "recommendations": [
    {
      "component": "component6",
      "action": "action4",
      "confidence": 68
    },
    {
      "component": "component6",
      "action": "action4",
      "confidence": 68
    }
  ]
}
```

