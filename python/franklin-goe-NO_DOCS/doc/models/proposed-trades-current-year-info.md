
# Proposed Trades Current Year Info

*This model accepts additional fields of type Any.*

## Structure

`ProposedTradesCurrentYearInfo`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `end_of_current_year` | [`GoeToEndOfCurrentYear`](../../doc/models/goe-to-end-of-current-year.md) | Required | - |
| `today` | [`TodayTradesInfo`](../../doc/models/today-trades-info.md) | Required | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example (as JSON)

```json
{
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
}
```

