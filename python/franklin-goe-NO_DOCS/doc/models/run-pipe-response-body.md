
# Run Pipe Response Body

*This model accepts additional fields of type Any.*

## Structure

`RunPipeResponseBody`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `analysis_report` | [`RunPipeAnalysisReport1`](../../doc/models/run-pipe-analysis-report-1.md) | Required | Captures various important recommendations and outputs from the GOE engine. |
| `path_report` | [`PathReport1`](../../doc/models/path-report-1.md) | Required | Captures lookforward portfolio and wealth paths as calcualted by the GOE engine. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example (as JSON)

```json
{
  "analysis_report": {
    "currentGoalProbability": 0.99,
    "currentLossThresholdProbability": 0.99,
    "pDeltaCurrentGoalProbability": 0.99,
    "pDeltaCurrentLossThresholdProbability": 0.99,
    "recommendedPortfolioId": 36,
    "meetGoalPriority": false,
    "isGoalRealistic": false,
    "meetLossPriority": false,
    "oneTimeTopUp": 126.44,
    "yearlyTopUpAccumulation": 100.16,
    "monthlyTopUpAccumulation": 198.96,
    "yearlyTopUpDecumulation": 117.08,
    "monthlyTopUpDecumulation": 32.26,
    "recommendedTenure": "recommendedTenure6",
    "bankruptcyMsg": "bankruptcyMsg4",
    "recommendedFinalWealthAt75": 219.16,
    "recommendedProbAt75": 0.99,
    "recommendedFinalWealthAt50": 26.84,
    "recommendedProbAt50": 0.99,
    "advisorDiscretionReport": {
      "key0": 184.62
    },
    "message": "message2",
    "lossThreshold": 68,
    "exampleAdditionalProperty": {
      "key1": "val1",
      "key2": "val2"
    }
  },
  "path_report": {
    "portfolioPath": [
      219,
      220
    ],
    "wealthPath": {
      "default": [
        94.4
      ],
      "pessimistic": [
        35.74,
        35.75,
        35.76
      ],
      "optimistic": [
        210.96,
        210.97
      ],
      "defaultPercentile": "defaultPercentile6",
      "pessimisticPercentile": "pessimisticPercentile4",
      "optimisticPercentile": "optimisticPercentile6",
      "exampleAdditionalProperty": {
        "key1": "val1",
        "key2": "val2"
      }
    },
    "exampleAdditionalProperty": {
      "key1": "val1",
      "key2": "val2"
    }
  },
  "exampleAdditionalProperty": {
    "key1": "val1",
    "key2": "val2"
  }
}
```

