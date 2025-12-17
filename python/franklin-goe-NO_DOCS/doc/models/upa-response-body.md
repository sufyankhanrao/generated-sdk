
# Upa Response Body

*This model accepts additional fields of type Any.*

## Structure

`UpaResponseBody`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `analysis_report` | [`UpaAnalysisReport1`](../../doc/models/upa-analysis-report-1.md) | Required | <b>For the Original Plan:</b><br>            GOE’s outputs including probability, portfolio advice, etc. |
| `path_report` | [`UpaPathReport1`](../../doc/models/upa-path-report-1.md) | Required | <b>For the Original Plan:</b>            GOE’s outputs including estimated portfolio path, wealth path, etc. |
| `analysis_report_mod` | [`UpaAnalysisReportMod1`](../../doc/models/upa-analysis-report-mod-1.md) | Required | <b>For the modified Plan:</b><br>            GOE’s outputs including probability, portfolio advice, etc. |
| `path_report_mod` | [`UpaPathReportMod1`](../../doc/models/upa-path-report-mod-1.md) | Required | <b>For the Modified Plan:</b><br>            GOE’s outputs including estimated portfolio path, wealth path, etc. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example (as JSON)

```json
{
  "analysisReport": {
    "currentGoalProbability": 10000.0,
    "currentLossThresholdProbability": 0.4233,
    "pDeltaCurrentGoalProbability": 0.3288,
    "pDeltaCurrentLossThresholdProbability": 0.4175,
    "recommendedPortfolioId": 6,
    "meetGoalPriority": false,
    "isGoalRealistic": false,
    "meetLossPriority": false,
    "oneTimeTopUp": 38859.0,
    "cashflowRecommendation": {
      "cashFlowMonthly": null,
      "cashFlowYearly": 2503.0,
      "startDate": "01-01-2022",
      "endDate": "01-01-2036",
      "newPlanProb": 0.85,
      "exampleAdditionalProperty": {
        "key1": "val1",
        "key2": "val2"
      }
    },
    "bankruptcyMsg": "NA",
    "advisorDiscretionReport": {
      "6": 0.3344
    },
    "lossThreshold": 11500,
    "tenureRecommendation": {
      "goalID": "Goal1",
      "goalStartDate": "13-01-2021",
      "goalEndDate": "01-01-2031",
      "newPlanProbability": 0.3648,
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
  "pathReport": {
    "portfolioPath": [
      123,
      124,
      125
    ],
    "wealthPath": [
      195.65,
      195.66
    ],
    "worstCasePath": [
      182.68
    ],
    "bestCasePath": [
      238.1,
      238.09,
      238.08
    ],
    "exampleAdditionalProperty": {
      "key1": "val1",
      "key2": "val2"
    }
  },
  "analysisReportMod": {
    "currentGoalProbability": 10000.0,
    "currentLossThresholdProbability": 15.58,
    "pDeltaCurrentGoalProbability": 0.3288,
    "pDeltaCurrentLossThresholdProbability": 0.4175,
    "recommendedPortfolioId": 6,
    "meetGoalPriority": false,
    "isGoalRealistic": false,
    "meetLossPriority": false,
    "oneTimeTopUp": 38859.0,
    "cashflowRecommendation": {
      "cashFlowMonthly": null,
      "cashFlowYearly": 2503.0,
      "startDate": "01-01-2022",
      "endDate": "01-01-2036",
      "newPlanProb": 0.85,
      "exampleAdditionalProperty": {
        "key1": "val1",
        "key2": "val2"
      }
    },
    "bankruptcyMsg": "NA",
    "advisorDiscretionReport": {
      "6": 0.3344
    },
    "lossThreshold": 11500,
    "goalsResponse": [
      {
        "goalID": "Goal1",
        "goalAmt": [
          179.05
        ],
        "startDate": "01-01-2021",
        "endDate": "01-01-2031",
        "priority": "Dream",
        "modifiedGoalAmt": [
          72.68,
          72.69
        ],
        "exampleAdditionalProperty": {
          "key1": "val1",
          "key2": "val2"
        }
      }
    ],
    "comments": "To meet all goals optimally as per their assigned priorities Goal1 has been reduced by 100.0%, Goal2 has been reduced by 50.0% of its original value. The allocated portfolio has an 94.316% probability of meeting the modified goals",
    "exampleAdditionalProperty": {
      "key1": "val1",
      "key2": "val2"
    }
  },
  "pathReportMod": {
    "portfolioPath": [
      233,
      234,
      235
    ],
    "wealthPath": [
      223.59
    ],
    "worstCasePath": [
      210.62,
      210.63,
      210.64
    ],
    "bestCasePath": [
      198.16,
      198.17,
      198.18
    ],
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

