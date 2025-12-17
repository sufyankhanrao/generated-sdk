
# Goe Simulation Engine Response Body

*This model accepts additional fields of type Any.*

## Structure

`GoeSimulationEngineResponseBody`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `analysis_report` | [`AnalysisReport1`](../../doc/models/analysis-report-1.md) | Required | This section gives details of the GOE run for the original plan. |
| `analysis_report_mod` | `str` | Required | In the event the original plan doesn’t meetnthe desired probability (in line with the priority), <br>                     the plan is modified by dropping less important goal – denoted by lower priority. <br>                     This is not applicable for the 1.0 version of GOE-SOFT. |
| `path_report` | [`PathReportSimulationEngine2`](../../doc/models/path-report-simulation-engine-2.md) | Required | Forward looking estimates of likely portfolios,                     wealth, withdrawals, and taxes |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example (as JSON)

```json
{
  "analysisReport": {
    "advisorDiscretionReport": {
      "10": 0.68
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
      "D": 0,
      "F": 30000,
      "T": 121043
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
                "tradeType": null,
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
                "tradeType": null,
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
    "recommendedPortfolioId": 10,
    "exampleAdditionalProperty": {
      "key1": "val1",
      "key2": "val2"
    }
  },
  "analysisReportMod": null,
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

