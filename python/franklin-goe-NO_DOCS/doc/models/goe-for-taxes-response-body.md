
# Goe for Taxes Response Body

*This model accepts additional fields of type Any.*

## Structure

`GoeForTaxesResponseBody`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `analysis_report` | [`GoeToAnalysisReport2`](../../doc/models/goe-to-analysis-report-2.md) | Required | This section gives details of the GOE run for the original plan. |
| `analysis_report_mod` | [`AnalysisReportMod1`](../../doc/models/analysis-report-mod-1.md) | Required | In the event the original plan doesn’t meet the desired probability (in line with the priority), <br>                     the plan is modified by dropping less important goal – denoted by lower priority.- <br>                     This section gives details of the GOE run for the modified plan.<br>                     Please note that the modification of goals is driven by business logic. |
| `path_report` | [`PathReportGoeForTaxes2`](../../doc/models/path-report-goe-for-taxes-2.md) | Required | Forward looking estimates of likely portfolios,                     wealth, withdrawals, and taxes |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example (as JSON)

```json
{
  "analysisReport": {
    "advisorDiscretionReport": {
      "16": 0.6504
    },
    "bankruptcyMsg": "NA",
    "currentGoalProbability": 0.6504,
    "expectedTaxesForCurrentYear": {
      "federalOrdinaryIncomeTaxLiability": 0.0,
      "federalQualifiedDividendsTaxLiability": 0.0,
      "federalCapitalGainsRebalancingLiability": 0.0,
      "federalCapitalGainsWithdrawalLiability": 0.0,
      "federalEarlyDistributionPenalty": 0.15,
      "federalTaxDueToRMD": 0.15,
      "federalTaxDueToSocialSecurity": 0.15,
      "federalTotalTaxLiability": 0.15,
      "exampleAdditionalProperty": {
        "key1": "val1",
        "key2": "val2"
      }
    },
    "isGoalRealistic": false,
    "lossThreshold": 138.94,
    "meetGoalPriority": false,
    "meetLossPriority": false,
    "oneTimeTopUp": {
      "T": 135040
    },
    "pDeltaCurrentGoalProbability": 0.6372,
    "pDeltaCurrentLossThresholdProbability": 193.2,
    "proposedTradesCurrentYear": {
      "endOfCurrentYear": {
        "accounts": [
          {
            "accountID": "T",
            "trades": [
              {
                "direction": "S",
                "symbol": "CASH",
                "cusip": "cusip4",
                "quantity": 29178.0,
                "amount": 10748.399065,
                "phase": "phase2",
                "exampleAdditionalProperty": {
                  "key1": "val1",
                  "key2": "val2"
                }
              }
            ],
            "exampleAdditionalProperty": {
              "key1": "val1",
              "key2": "val2"
            }
          }
        ],
        "exampleAdditionalProperty": {
          "key1": "val1",
          "key2": "val2"
        }
      },
      "today": {
        "accounts": [
          {
            "accountID": "T",
            "trades": [
              {
                "direction": "S",
                "symbol": "CASH",
                "cusip": "cusip4",
                "quantity": 29178.0,
                "amount": 10748.399065,
                "phase": "phase2",
                "exampleAdditionalProperty": {
                  "key1": "val1",
                  "key2": "val2"
                }
              }
            ],
            "exampleAdditionalProperty": {
              "key1": "val1",
              "key2": "val2"
            }
          }
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
    },
    "recommendedPortfolioId": 16,
    "exampleAdditionalProperty": {
      "key1": "val1",
      "key2": "val2"
    }
  },
  "analysisReportMod": {
    "goalsResponse": [
      {
        "goalID": "Goal2",
        "goalAmt": [
          179.05
        ],
        "startDate": "01-12-2023",
        "endDate": "30-11-2025",
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
    "exampleAdditionalProperty": {
      "key1": "val1",
      "key2": "val2"
    }
  },
  "pathReport": {
    "earlyWithdrawalPenalty": 0.0,
    "endingWealth": {
      "expected": 221160,
      "optimistic": 240110,
      "pessimistic": 204004
    },
    "expectedTaxAmount": 0.0,
    "goalAmount": 121.5,
    "period": 2,
    "portfolioId": 16,
    "rmdAmount": [
      {
        "amount": 127.8,
        "memberId": "memberId8",
        "exampleAdditionalProperty": {
          "key1": "val1",
          "key2": "val2"
        }
      }
    ],
    "socialSecurityAmount": [
      {
        "amount": 87.4,
        "memberId": "memberId8",
        "exampleAdditionalProperty": {
          "key1": "val1",
          "key2": "val2"
        }
      }
    ],
    "withdrawalAmount": {
      "D": 0,
      "F": 0,
      "T": 0
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

